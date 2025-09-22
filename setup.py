from setuptools import setup, find_packages

setup(
    name="medicalchatbot",
    version="0.1.0",
    author="P NIKHIL KUMAR NAIK",
    description="A medical chatbot using GenAI and LangChain",
    packages=find_packages(),
    install_requires=[
        # --- Core AI / ML & Embeddings ---
        "torch>=2.2.2,<3.0",
        "transformers>=4.42.2,<5.0",
        "sentence-transformers>=3.1.1,<4.0",
        "ctransformers>=0.2.27,<1.0",

        # --- Vector Database ---
        "pinecone",
        "pinecone>=6.0.0,<7.0",
        #"pinecone-client>=6.0.0,<7.0",
        "langchain-pinecone==0.1.3",



        # --- LLMs & LangChain ---
        "groq",
        "langchain>=0.2.14,<0.3",
        "langchain-community>=0.0.200",
        "langchain-huggingface",

        # --- PDF & File Utilities ---
        "pypdf>=3.10.0,<4.0",
        "tqdm",
        "numpy>=1.26,<3.0",
        "scikit-learn>=1.5.2,<2.0",
        "python-dotenv",

        # --- Web Framework ---
        "flask>=3.0.3,<4.0",
    ],
    python_requires=">=3.9",
)
