import re
import streamlit as st
import pycountry
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
    """Extracts Name from OCR text for various document types."""
    # Aadhaar-specific name extraction
    aadhaar_name_match = re.search(r"\n([A-Za-z\s]+)\n", text)
    if aadhaar_name_match:
        return aadhaar_name_match.group(1).strip()

    # PAN-specific name extraction
    pan_name_match = re.search(r"Name\s*[:\-]*\s*([A-Z\s]+)\b", text, re.IGNORECASE)
    if pan_name_match:
        return pan_name_match.group(1).strip()

    # Passport-specific name extraction
    given_name_match = re.search(r"Given Name\s*[:\-]*\s*([A-Za-z\s]+)", text, re.IGNORECASE)
    surname_match = re.search(r"Surname\s*[:\-]*\s*([A-Za-z\s]+)", text, re.IGNORECASE)

    if given_name_match and surname_match:
        return f"{given_name_match.group(1).strip()} {surname_match.group(1).strip()}"

    # MRZ Zone Fallback (Highly Accurate for Passport OCR)
    mrz_match = re.search(r"P<IND([A-Z]+)<<([A-Z]+)", text)
    if mrz_match:
        full_name = f"{mrz_match.group(2).strip()} {mrz_match.group(1).strip()}"
        return full_name.strip()

    return None

def upload_to_blob(file):
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.name)
    blob_client.upload_blob(file.getvalue(), overwrite=True)
    return blob_client.url

def get_account_by_name(name):
    query = f"SELECT * FROM c WHERE LOWER(c.name) = '{name.lower()}'"
    items = list(container.query_items(query, enable_cross_partition_query=True))
    return items[0] if items else None

def add_new_account(account_id, name, document_type, document_url):
    new_account = {"id": account_id, "name": name, "documents": [{"type": document_type, "url": document_url}]}
    container.create_item(new_account)
    return new_account

def link_document_to_account(account_id, document_type, document_url):
    account = container.read_item(item=account_id, partition_key=account_id)
    account["documents"].append({"type": document_type, "url": document_url})
    container.replace_item(item=account_id, body=account)

def get_documents_by_account(account_id):
    try:
        account = container.read_item(item=account_id, partition_key=account_id)
        return account["documents"], account["name"]
    except:
        return None, None

# Set page configuration
st.set_page_config(
    page_title="FileFlow AI",
    layout="wide",
    page_icon="📑",
    initial_sidebar_state="expanded"
)

# Custom CSS for improved UI with professional color scheme
st.markdown("""
<style>
    :root {
        --primary-color: #0F4C81;
        --primary-light: #E6EFF6;
        --secondary-color: #3A6EA5;
        --accent-color: #FF6B6B;
        --text-color: #333333;
        --text-light: #6E7C87;
        --bg-light: #F8FAFC;
        --bg-medium: #EEF2F6;
        --success-color: #2E7D32;
        --success-light: #E8F5E9;
        --warning-color: #ED6C02;
        --warning-light: #FFF4E5;
        --error-color: #D32F2F;
        --error-light: #FDECEA;
        --info-color: #0288D1;
        --info-light: #E6F4FA;
        --border-color: #E2E8F0;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--primary-color);
        margin-bottom: 0;
    }
    
    .sub-header {
        font-size: 1.2rem;
        color: var(--text-light);
        margin-top: 0;
    }
    
    .card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: white;
        border: 1px solid var(--border-color);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
    }
    
    .success-card {
        background-color: var(--success-light);
        border: 1px solid #C8E6C9;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .info-card {
        background-color: var(--info-light);
        border: 1px solid #B3E5FC;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .warning-card {
        background-color: var(--warning-light);
        border: 1px solid #FFE0B2;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .error-card {
        background-color: var(--error-light);
        border: 1px solid #FFCDD2;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .upload-section {
        background-color: var(--bg-light);
        border-radius: 0.5rem;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
        box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.05);
    }
    
    /* Other existing styles... */
</style>
""", unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    st.image("fileflow.png", width=100)
    st.markdown("<p class='main-header'>FileFlow AI</p>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Document Management System</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation
    selected_tab = st.radio(
        "Navigation",
        options=["📤 Upload Document", "🔍 Search Account", "ℹ️ About"],
        index=0
    )
    
    st.markdown("---")
    st.markdown("### Document Types Supported")
    st.markdown("• Aadhaar Card")
    st.markdown("• PAN Card")
    st.markdown("• Passport")
    st.markdown("• Invoices")
    st.markdown("• Applications")

# Main content area
if selected_tab == "📤 Upload Document":
    st.markdown("<h1>Upload & Process Documents</h1>", unsafe_allow_html=True)
    st.markdown("Upload your document for automatic analysis and account linking.")
    
    # Create a card-like container for the upload section
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # File uploader with improved styling
    st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Drag and drop your document here", type=["pdf", "jpg", "png", "jpeg"])
    st.markdown("Supported formats: PDF, JPG, PNG")
    st.markdown("</div>", unsafe_allow_html=True)
    
    if uploaded_file:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(uploaded_file, caption="Uploaded Document", use_container_width=True)
        
        with col2:
            with st.spinner("🔍 Analyzing document..."):
                # Process the document
                poller = ocr_client.begin_analyze_document("prebuilt-layout", uploaded_file.getvalue())
                result = poller.result()
                extracted_text = " ".join([line.content for page in result.pages for line in page.lines]).lower()

                # Determine document type
                doc_type = (
                    'PAN Card' if 'permanent account number' in extracted_text
                    else 'Aadhaar Card' if 'aadhaar' in extracted_text or 'आधार' in extracted_text or 'VID' in extracted_text or 'Government of India' in extracted_text or 'DOB' in extracted_text
                    else 'Passport' if 'passport no.' in extracted_text or 'republic of india' in extracted_text
                    else 'Invoice' if 'invoice number' in extracted_text
                    else 'Application' if 'application number' in extracted_text
                    else 'Unknown Document Type'
                )

                # Extract name
                extracted_name = extract_name(extracted_text)
                
                # Upload to blob storage
                doc_url = upload_to_blob(uploaded_file)
                
                # Display results in a nice format
                st.markdown("<div class='success-card'>", unsafe_allow_html=True)
                st.markdown(f"### Analysis Results")
                st.markdown(f"**Document Type:** {doc_type}")
                
                if extracted_name:
                    extracted_name = extracted_name.title().strip()
                    st.markdown(f"**Extracted Name:** {extracted_name}")
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    # Check if account exists
                    existing_account = get_account_by_name(extracted_name)
                    
                    if existing_account:
                        st.markdown("<div class='info-card'>", unsafe_allow_html=True)
                        st.markdown(f"### Account Found")
                        st.markdown(f"Account ID: **{existing_account['id']}**")
                        st.markdown(f"Account Holder: **{existing_account['name']}**")
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                        # Option to link document
                        st.markdown("### Link Document")
                        confirm_link = st.radio(
                            "Do you want to link this document to the existing account?",
                            options=["Yes", "No"],
                            horizontal=True
                        )
                        
                        if confirm_link == "Yes":
                            if st.button("Confirm Link"):
                                link_document_to_account(existing_account["id"], doc_type, doc_url)
                                st.markdown("<div class='success-card'>", unsafe_allow_html=True)
                                st.markdown(f"✅ Document successfully linked to Account ID: **{existing_account['id']}**")
                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.markdown("<div class='warning-card'>", unsafe_allow_html=True)
                        st.markdown("### No Account Found")
                        st.markdown(f"No existing account found for **{extracted_name}**")
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                        # Option to create new account
                        st.markdown("### Create New Account")
                        create_new = st.radio(
                            "Would you like to create a new account?",
                            options=["Yes", "No"],
                            horizontal=True
                        )
                        
                        if create_new == "Yes":
                            with st.form("new_account_form"):
                                st.markdown("### Account Details")
                                account_id = st.text_input("Enter a unique Account Number:")
                                
                                submit_button = st.form_submit_button("Create Account & Link Document")
                                
                                if submit_button and account_id:
                                    add_new_account(account_id, extracted_name, doc_type, doc_url)
                                    st.markdown("<div class='success-card'>", unsafe_allow_html=True)
                                    st.markdown(f"✅ New account created with Account ID: **{account_id}**")
                                    st.markdown(f"✅ Document successfully linked to the account")
                                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.markdown("**Extracted Name:** Unable to extract name")
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    st.markdown("<div class='error-card'>", unsafe_allow_html=True)
                    st.markdown("❌ Could not extract a valid name from the document.")
                    st.markdown("Please ensure the document is clear and contains readable text.")
                    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close the card for the upload section

elif selected_tab == "🔍 Search Account":
    st.markdown("<h1>Search Account</h1>", unsafe_allow_html=True)
    st.markdown("Search for an account to view linked documents.")
    
    # Create a card-like container for the search section
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # Search form
    with st.form("search_form"):
        account_id = st.text_input("Enter Account Number:")
        search_button = st.form_submit_button("🔍 Search")
        
        if search_button and account_id:
            documents, account_name = get_documents_by_account(account_id)
            
            if documents:
                st.markdown("<div class='success-card'>", unsafe_allow_html=True)
                st.markdown(f"### Account Information")
                st.markdown(f"**Account ID:** {account_id}")
                st.markdown(f"**Account Holder:** {account_name.title()}")
                st.markdown("</div>", unsafe_allow_html=True)
                
                st.markdown("### Linked Documents")
                
                for doc in documents:
                    st.markdown(f"""
                    <div class='document-card'>
                        <div class='document-icon'>📄</div>
                        <div class='document-info'>
                            <strong>{doc['type']}</strong>
                        </div>
                        <a href='{doc['url']}' target='_blank' class='document-link'>View Document</a>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("<div class='error-card'>", unsafe_allow_html=True)
                st.markdown("❌ No records found. Please ensure the account ID is correct.")
                st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # Close the search section card

elif selected_tab == "ℹ️ About":
    st.markdown("<h1>About FileFlow AI</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("""
    ### Document Management Made Simple
    
    FileFlow AI is an intelligent document management system that helps you:
    
    - **Automatically analyze** documents using OCR technology
    - **Extract key information** like names and document types
    - **Link documents** to customer accounts
    - **Securely store** documents in the cloud
    - **Easily retrieve** documents when needed
    
    ### Supported Document Types
    
    - Aadhaar Cards
    - PAN Cards
    - Passports
    - Invoices
    - Application Forms
    - And more!
    
    ### Technology Stack
    
    - **Frontend:** Streamlit
    - **OCR Engine:** Azure Form Recognizer
    - **Storage:** Azure Blob Storage
    - **Database:** Azure Cosmos DB
    """)
    st.markdown("</div>", unsafe_allow_html=True)  # Close the about section card

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #6E7C87;'>© 2025 FileFlow AI. All rights reserved.</p>", unsafe_allow_html=True)
