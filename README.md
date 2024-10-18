# StreamlitQABot
This application allows you to upload PDFs and ask questions about their content. The bot provides informative answers based on the information in the documents.

Streamlit QA Bot
Overview

This Streamlit application serves as a question-answering bot that leverages Pinecone and Cohere to process PDFs and provide informative responses.

Prerequisites

Python 3.11 or later
Docker (for deployment)
Pinecone account with API key
Cohere account with API key
Streamlit
Installation

Clone the Repository:

Bash
git clone https://github.com/your-username/your-repo-name.git
Use code with caution.

Install Dependencies:

Bash
cd your-repo-name   

pip install -r requirements.txt
Use code with caution.

If you don't have a requirements.txt file, create one with the following content:

streamlit
pinecone
cohere
sentence-transformers
PyPDF2
Usage

Set API Keys:
Replace the placeholders in the code with your actual Pinecone and Cohere API keys.

Run the Application:

Locally:
Bash
streamlit run app.py
Use code with caution.

Using Docker: Build the Docker image:
Bash
docker build -t your-app-name .
Use code with caution.

Run the container:
Bash
docker run -e PINECONE_API_KEY=your_pinecone_api_key -e COHERE_API_KEY=your_cohere_api_key -p 8501:8501 your-app-name
Use code with caution.

Access the app at http://localhost:8501/.
How to Use

Upload PDF: Click the "Upload a PDF" button and select the PDF file you want to analyze.
Ask Questions: Enter your question in the text input field and click "Submit."
View Response: The bot will process the query and provide a relevant answer based on the uploaded PDF.
Configuration

Pinecone Index: The code uses the default index name "default". You can customize this by modifying the pinecone.Index("default") line in the preprocess_and_store_pdf function.
Cohere Model: Adjust the model parameter in the co.generate call to use a different Cohere model if desired.
Additional Notes

Ensure you have a Pinecone index created and your API keys configured correctly.
For production deployment, consider using a container orchestration platform like Docker Compose or Kubernetes.
Customize the code to fit your specific requirements, such as adding more features or improving the response generation.
Contributing

Feel free to contribute to this project by submitting pull requests or raising issues.
