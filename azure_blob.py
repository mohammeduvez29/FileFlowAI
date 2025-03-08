from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
from config import BLOB_CONNECTION_STRING, CONTAINER_NAME

# Initialize Blob Service Client
blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

def upload_to_blob(file_name, file_bytes, account_number):
    """Uploads a file to Azure Blob Storage with account metadata."""
    try:
        blob_client = container_client.get_blob_client(f"{account_number}/{file_name}")
        blob_client.upload_blob(file_bytes, overwrite=True)

        return f"✅ File uploaded successfully! Stored as: {file_name}"
    except Exception as e:
        return f"❌ Upload Error: {str(e)}"

def get_files_by_account(account_number):
    """Fetch all files related to a given account number."""
    try:
        blobs = container_client.list_blobs(name_starts_with=f"{account_number}/")
        file_list = [blob.name.split("/")[-1] for blob in blobs]

        if not file_list:
            return "❌ No files found for this account."
        
        return file_list
    except Exception as e:
        return f"❌ Fetch Error: {str(e)}"
