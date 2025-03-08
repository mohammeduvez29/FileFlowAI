import os
import re
import streamlit as st
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient
from azure.cosmos import CosmosClient
from config import *

# Initialize Azure Clients using imported config
ocr_client = DocumentAnalysisClient(AZURE_OCR_ENDPOINT, AzureKeyCredential(AZURE_OCR_KEY))
blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
cosmos_client = CosmosClient(COSMOS_URL, COSMOS_KEY)
database = cosmos_client.get_database_client(COSMOS_DATABASE)
container = database.get_container_client(COSMOS_CONTAINER)

def extract_name(text):
    """Extracts Name from OCR text."""
    name_match = re.search(r"नाम\s*[/]*\s*name\s*[:\-]*\s*([A-Za-z\s]+)\s*पिता", text, re.IGNORECASE)
    return name_match.group(1).strip() if name_match else None

def upload_to_blob(file):
    """Uploads file to Azure Blob Storage and returns the URL."""
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.name)
    blob_client.upload_blob(file.getvalue(), overwrite=True)
    return blob_client.url

def get_account_by_name(name):
    """Checks if an account exists for the given name in CosmosDB."""
    query = f"SELECT * FROM c WHERE c.name = '{name}'"
    items = list(container.query_items(query, enable_cross_partition_query=True))
    return items[0] if items else None

def add_new_account(account_id, name, document_type, document_url):
    """Creates a new account in CosmosDB and links the document."""
    new_account = {
        "id": account_id,
        "name": name,
        "documents": [{"type": document_type, "url": document_url}]
    }
    container.create_item(new_account)
    return new_account

def link_document_to_account(account_id, document_type, document_url):
    """Links a new document to an existing account in CosmosDB."""
    account = container.read_item(item=account_id, partition_key=account_id)
    account["documents"].append({"type": document_type, "url": document_url})
    container.replace_item(item=account_id, body=account)

def get_documents_by_account(account_id):
    """Retrieves all linked documents for a given account ID and the account holder's name."""
    try:
        account = container.read_item(item=account_id, partition_key=account_id)
        return account["documents"], account["name"]
    except:
        return None, None

# Streamlit UI
st.set_page_config(page_title="OCR & Document Storage", layout="centered", page_icon="📑")
st.title("📄 FileFlow AI")
st.markdown("**Upload a document or search by account number!**")

option = st.radio("Choose an option:", ["📤 Upload Document", "🔍 Search by Account Number"])

if option == "📤 Upload Document":
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "jpg", "png"])

    if uploaded_file:
        with st.spinner("Analyzing..."):
            poller = ocr_client.begin_analyze_document("prebuilt-layout", uploaded_file.getvalue())
            result = poller.result()
            extracted_text = " ".join([line.content for page in result.pages for line in page.lines]).lower()

            doc_type = "PAN Card" if "permanent account number" in extracted_text else "Unknown Document Type"
            extracted_name = extract_name(extracted_text)
            doc_url = upload_to_blob(uploaded_file)

            st.success(f"📑 Extracted Document Type: **{doc_type}**")
            if extracted_name:
                extracted_name = extracted_name.lower().strip()
                st.success(f"🆔 Extracted Name: **{extracted_name}**")
                existing_account = get_account_by_name(extracted_name)

                if existing_account:
                    link_document_to_account(existing_account["id"], doc_type, doc_url)
                    st.success(f"✅ Document successfully linked to Account ID: {existing_account['id']}")
                else:
                    create_new = st.radio("Account not found. Create a new one?", ["Yes", "No"])
                    if create_new == "Yes":
                        account_id = st.text_input("Enter a unique Account Number:")
                        if st.button("Create Account & Link Document") and account_id:
                            add_new_account(account_id, extracted_name, doc_type, doc_url)
                            st.success(f"✅ New account created with Account ID: {account_id}")
                    else:
                        st.warning("⚠️ Document not linked as no account was chosen.")
            else:
                st.error("❌ Could not extract a valid name.")

elif option == "🔍 Search by Account Number":
    account_id = st.text_input("Enter Account Number:")
    if st.button("🔍 Search"):
        documents, account_name = get_documents_by_account(account_id)
        if documents:
            st.success(f"🆔 **Account ID:** {account_id}")
            st.info(f"👤 Account Holder: **{account_name}**")
            for doc in documents:
                st.info(f"📑 {doc['type']}: [View Document]({doc['url']})")
        else:
            st.error("❌ No records found.")
