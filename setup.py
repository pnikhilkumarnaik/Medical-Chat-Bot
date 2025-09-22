from setuptools import setup, find_packages

setup(
    name="medicalchatbot",
    version="0.1.0",
    author="P NIKHIL KUMAR NAIK",
    description="A medical chatbot using GenAI and LangChain",
    packages=find_packages(),
    install_requires=[
        "pypdf>=3.10.0,<4.0",  # Replaces PyMuPDF
        "ctransformers>=0.2.27,<1.0",
        "sentence-transformers>=3.1.1,<4.0",
        "langchain>=0.2.14,<0.3",
        "langchain-community>=0.0.200",
        "pinecone>=6.0.0,<7.0",
        "flask>=3.0.3,<4.0",
        "groq",                    # Groq SDK
<<<<<<< HEAD
        "numpy>=1.26,<3.0",
=======
        "numpy",
>>>>>>> 6eaed58a2d2daf2afe61a3e19435ab76b80d8f72
        "scikit-learn>=1.5.2,<2.0",
        "tqdm",
    ],
    python_requires=">=3.9",
)
