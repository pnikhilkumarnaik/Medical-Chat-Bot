
import re
from flask import Flask, jsonify, request,render_template
from src.helper import download_hugging_face_embedding
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from pinecone import Pinecone
import pinecone
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import CTransformers
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from src.prompt import prompt_template

import os


app=Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

embeddings = download_hugging_face_embedding()

pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = PINECONE_INDEX
index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_existing_index(index_name=index_name,
    embedding=embeddings, namespace="default" )

PROMPT=PromptTemplate(template=prompt_template,input_variables=["context","question"])
chain_type_kwargs={"prompt":PROMPT}

llm = ChatGroq(model="Gemma2-9b-It",  
       api_key=GROQ_API_KEY, temperature=0.8 )


qa=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={"k":2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs)

@app.route('/')
def index():
    return render_template('home.html')




@app.route("/get", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        msg = data.get("message", "")
        print("User:", msg)

        # Use your QA chain (invoke)
        result = qa.invoke({"query": msg})
        answer = result["result"]
        print("Response:", answer)

        return jsonify({"response": answer})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)})




if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0',port=8080)