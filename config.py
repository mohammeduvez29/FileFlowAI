import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Azure Blob Storage Config
BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

# Azure OCR Config
AZURE_OCR_ENDPOINT = os.getenv("AZURE_OCR_ENDPOINT")
AZURE_OCR_KEY = os.getenv("AZURE_OCR_KEY")

COSMOS_DATABASE = os.getenv("COSMOS_DATABASE")
COSMOS_CONTAINER = os.getenv("COSMOS_CONTAINER")
COSMOS_URL = os.getenv("COSMOS_URL") 
COSMOS_KEY = os.getenv("COSMOS_KEY") 

# Validate Required Variables
required_env_vars = {
    "BLOB_CONNECTION_STRING": BLOB_CONNECTION_STRING,
    "CONTAINER_NAME": CONTAINER_NAME,
    "AZURE_OCR_ENDPOINT": AZURE_OCR_ENDPOINT,
    "AZURE_OCR_KEY": AZURE_OCR_KEY,
}

# Raise an error if any required environment variable is missing
for key, value in required_env_vars.items():
    if not value:
        raise ValueError(f"❌ ERROR: Missing required environment variable: {key}")
