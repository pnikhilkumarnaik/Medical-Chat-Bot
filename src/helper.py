

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

from langchain_huggingface import HuggingFaceEmbeddings


#load pdf files from a folder
def load_pdf(data_folder):
    loader = DirectoryLoader(data_folder, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

#create chunks of text from the loaded documents
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks= text_splitter.split_documents(extracted_data)
    return text_chunks

#download embedding model
def download_hugging_face_embedding():
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

