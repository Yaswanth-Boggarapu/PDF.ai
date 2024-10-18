# pinecone = pinecone.Pinecone(api_key="8f1ebcff-82ce-4d59-9cff-f35680fab870", environment="us-west1-gcp")
# co = cohere.Client("epOVT4qDQZjw2fmUxFts1ilaOyivjIOO8AqocChT") 
import streamlit as st
import pandas as pd
import numpy as np
import cohere
from sentence_transformers import SentenceTransformer
import pinecone  # Import the Pinecone library
from pinecone import exceptions  # Import the exceptions submodule
import PyPDF2

# Initialize Pinecone
# Replace with your actual API key and environment

pinecone = pinecone.Pinecone(api_key="8f1ebcff-82ce-4d59-9cff-f35680fab870", environment="us-west1-gcp")
# Load the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize Cohere
co = cohere.Client("epOVT4qDQZjw2fmUxFts1ilaOyivjIOO8AqocChT")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    # Access the file path from the UploadedFile object
    file_path = pdf_file.name

    # Check if the file extension is .pdf
    if not file_path.endswith(".pdf"):
        st.error("Please upload a PDF file.")
        return None

    try:
        with open(file_path, 'rb') as pdf_reader:
            reader = PyPDF2.PdfReader(pdf_reader)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except FileNotFoundError:
        st.error("An error occurred while processing the file.")
        return None

# Function to preprocess and store PDF content
def preprocess_and_store_pdf(pdf_file):
    text = extract_text_from_pdf(pdf_file)

    if text is not None:
        # Check if the index exists
        try:
            index = pinecone.Index("default")
        except exceptions.NotFoundException:
            # Create the index if it doesn't exist
            index = pinecone.Index.create("default")

        # Convert text to embedding
        embedding = model.encode(text)

        # Store in Pinecone
        index.upsert([(pdf_file.name, embedding.tolist())])

# Function to retrieve and generate answer
def get_answer(query):
    query_embedding = model.encode(query)

    # Convert query embedding to list
    query_embedding_list = query_embedding.tolist()

    # Use the index object for querying
    index = pinecone.Index("default")  # Use a specific index name
    results = index.query(vector=query_embedding_list, top_k=5, include_metadata=True)

    retrieved_docs = [result["id"] for result in results["matches"]]
    prompt = "Based on these documents, answer the question:\n" + query + "\nDocuments:\n" + "\n".join(retrieved_docs)

    try:
        # Use the client instance to generate text
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=50,
            temperature=0.8,
            k=0,
            p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=[],
            return_likelihoods='NONE'
        )
        answer = response.generations[0].text
        return answer
    except cohere.CohereError as e:
        print(f"Error generating answer with Cohere: {e}")
        return "Failed to generate answer using Cohere API."

# Streamlit app
def main():
    st.title("QA Bot")

    # Upload PDF
    uploaded_file = st.file_uploader("Upload a PDF")

    if uploaded_file is not None:
        # Process and store PDF
        preprocess_and_store_pdf(uploaded_file)

        # Input query
        query = st.text_input("Ask a question:")

        if st.button("Submit"):
            # Get answer
            answer = get_answer(query)
            st.write(answer)



if __name__ == "__main__":
    main()