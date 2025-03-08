from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from config import AZURE_OCR_ENDPOINT, AZURE_OCR_KEY

# Initialize Azure OCR Client
ocr_client = DocumentAnalysisClient(AZURE_OCR_ENDPOINT, AzureKeyCredential(AZURE_OCR_KEY))

def analyze_document(file_bytes):
    """Extracts text from the document using Azure OCR."""
    try:
        poller = ocr_client.begin_analyze_document("prebuilt-layout", file_bytes)
        result = poller.result()

        # Extract full text from all lines in the document
        extracted_text = " ".join([line.content for page in result.pages for line in page.lines])
        
        print("🔍 Extracted Text Debug:", extracted_text)  # Debugging output

        return extracted_text

    except Exception as e:
        return str(e)
