# 🔬 **FileFlow AI: Your Smart Document Classification Solution**

[Presentation Deck](https://stdntpartners-my.sharepoint.com/:p:/g/personal/mohammeduvez_khan_studentambassadors_com/EeAd0pirnMdEpSf9fBtbskkBb8YsHqWJEan8DRCqXSb6hg?e=YQO0yI)

---

## 🔧 **Overview**

FileFlow AI is an **intelligent document classification system** designed to streamline the document handling workflow for institutions using a combination of **OCR** (Optical Character Recognition) technology and **Cosmos DB** to store and retrieve documents. The solution is built with **Azure AI** integration for OCR and storage functionality leveraging **Azure Blob Storage** and **Cosmos DB** for managing user account data and their associated documents.

**Core Capabilities:**
- **OCR Text Extraction:** Utilizing Azure’s prebuilt document models, we extract text from images and PDFs for further processing.
- **Document Storage:** Secure storage of documents in **Azure Blob Storage** with metadata associated in **Cosmos DB**.
- **User Account Association:** Accounts are linked with documents, ensuring easy access and retrieval based on user data like names.

---

## 🎯 **Key Features**

- 🖥️ **Document Classification:** Extracts document type and extracts user-specific data (e.g., names).
- 📑 **OCR Integration:** Uses Azure AI Document Intelligence to extract structured text from documents.
- 🔐 **Cosmos DB Storage:** All account data and document links are securely stored in **Azure Cosmos DB**.
- 🔗 **Seamless Document Upload:** Upload documents to Azure Blob Storage and link them to user accounts in Cosmos DB.
- 📡 **Account Lookup and Linking:** Search by account number and manage linked documents.

---

## 🛠️ **Installation Guide**

### **Prerequisites**

Ensure the following are installed:
- **Python 3.8+**
- **pip** (Python package installer)
- **Streamlit** for the frontend.

### **Installation Steps**

1. **Clone the Repository:**
   `git clone https://github.com/mohammeduvez29/FileFlowAI/`
   `cd FileFlowAI`

2. **Set Up Virtual Environment:**
   `python -m venv venv`
   `source venv/bin/activate  # On Windows: venv\Scripts\activate`

3. **Install Dependencies:**
   `pip install -r requirements.txt`

4. **Run the Application:**
   `python app.py`

   This will start the Streamlit application and allow you to upload documents, extract text, and link them to accounts.

---

## 📘 **Usage Instructions**

### **Upload and Classify Documents**

1. Launch the application using:
   `streamlit run app.py`

2. In the Streamlit UI, you will be presented with two options:
   - **Upload Document**: Upload a document to analyze its contents using Azure’s OCR and either create a new account or link it to an existing one.
   - **Search by Account Number**: Search and view documents already linked to an existing account.

3. The app will display:
   - Extracted document type.
   - Extracted name (if available).
   - Options to either link to an existing account or create a new one.

4. **Account Management:**
   - Users can link documents to existing accounts based on extracted names.
   - If no account is found, the system allows you to create a new account and associate the document with it.

---

## 🤖 **Technology Stack**

### **Frontend**
- **Streamlit**: For building the web interface where users can upload documents and view results.

### **Backend & Document Handling**
- **Azure Form Recognizer (OCR)**: For extracting text from documents.
- **Azure Blob Storage**: For storing the uploaded documents securely.
- **Azure Cosmos DB**: For storing user account information and linked document metadata.

### **Security**
- **Azure Key Vault**: (Optional) For securely managing credentials and keys.

---

## 🔄 **Project Structure**

```
FileFlowAI/
├── app.py                      # Main Streamlit application
├── config.py                   # Environment configuration and Azure credentials setup
├── azure_blob.py               # Logic for interacting with Azure Blob Storage
├── azure_ocr.py                # OCR text extraction logic using Azure AI
├── requirements.txt            # Required Python dependencies
├── .env                        # Environment variables for configuration (BLOB_CONNECTION_STRING, COSMOS_URL, etc.)
```

---

## 📦 **Requirements**

- **Python 3.8+**
- **Streamlit**
- **azure-ai-formrecognizer**
- **azure-storage-blob**
- **azure-cosmos**
- **python-dotenv** for managing environment variables

You can install all required dependencies by running:

`pip install -r requirements.txt`

---

## ⚙️ **How it Works**

### **Upload Document & Analyze**
- Users can upload a document (PDF, JPG, PNG).
- The system uses Azure OCR to extract text and recognize the document type (e.g., PAN Card).
- The extracted data (such as name) is used to check if an account already exists in **Cosmos DB**.
- If the account exists, the document is linked to the existing account.
- If no account exists, the user can create a new account, and the document will be linked to it.

---
