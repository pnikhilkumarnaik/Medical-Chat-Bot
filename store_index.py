import os
from dotenv import load_dotenv
from src.helper import load_pdf, text_split, download_hugging_face_embedding
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import Pinecone
import pinecone


# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

# --- Load and preprocess data ---
extracted_data = load_pdf("data")  # Load PDFs
text_chunks = text_split(extracted_data)  # Split into smaller chunks
embeddings = download_hugging_face_embedding()  # HuggingFace embeddings

# --- Initialize Pinecone ---
pc = Pinecone(api_key=PINECONE_API_KEY)

# Ensure the index exists
index_name = PINECONE_INDEX
index = pc.Index(index_name)

# --- Store embeddings in Pinecone ---
docsearch = PineconeVectorStore.from_texts(
    texts=[t.page_content for t in text_chunks],
    embedding=embeddings,
    index_name=index_name,
    namespace="default" 
)

print(f"✅ Successfully stored {len(text_chunks)} chunks in Pinecone index '{index_name}'")



