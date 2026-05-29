from setuptools import setup, find_packages

setup(
    name="medicalchatbot",
    version="0.1.0",
    author="P NIKHIL KUMAR NAIK",
    description="A medical chatbot using GenAI and LangChain",

    packages=find_packages(),

    install_requires=[
        # -------------------------------
        # Core AI / ML & Embeddings
        # -------------------------------
        "torch==2.5.1",
        "transformers==4.46.2",
        "sentence-transformers==3.2.1",
        "ctransformers==0.2.27",

        # -------------------------------
        # Vector Database
        # -------------------------------
        "pinecone-client==5.0.1",
        "langchain-pinecone==0.1.3",

        # -------------------------------
        # LLMs & LangChain (STRICT COMPATIBILITY)
        # -------------------------------
        "groq>=0.11.0,<1.0",
        "langchain-groq==0.1.10",

        "langchain==0.2.16",
        "langchain-community==0.2.16",
        "langchain-core==0.2.39",
        "langchain-huggingface==0.0.3",

        # -------------------------------
        # PDF & Utilities
        # -------------------------------
        "pypdf==5.1.0",
        "tqdm==4.67.1",
        "numpy==1.26.4",
        "scikit-learn==1.5.2",
        "python-dotenv==1.0.1",

        # -------------------------------
        # Web Framework
        # -------------------------------
        "flask==3.0.3",
    ],

    python_requires=">=3.10",
)