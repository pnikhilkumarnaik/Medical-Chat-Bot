from setuptools import setup, find_packages

setup(
    name="medicalchatbot",
    version="0.1.0",
    author="P NIKHIL KUMAR NAIK",
    description="A medical chatbot using GenAI and LangChain",
    packages=find_packages(),
    install_requires=[
        "openai>=1.40.6,<2.0",
        "ctransformers>=0.2.27,<1.0",
        "sentence-transformers>=3.1.1,<4.0",
        "langchain>=0.2.14,<0.3",
        "langchain-community>=0.0.200",
        "pinecone>=6.0.0,<7.0",
        "flask>=3.0.3,<4.0",
        "groq",                    # Groq SDK
        "numpy",
        "scikit-learn>=1.5.2,<2.0",
        "tqdm",
    ],
    python_requires=">=3.9",
)
