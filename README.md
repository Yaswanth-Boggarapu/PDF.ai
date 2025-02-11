# PDF.ai - Powered by Pinecone, Cohere, and Sentence Transformers

This application leverages the power of Pinecone for efficient vector storage and retrieval, Cohere for generating insightful answers, and Sentence Transformers for semantic text embeddings. It allows users to upload a PDF document, ask questions related to its content, and receive answers generated by a language model based on the document's context.

## Functionalities:

*   **PDF Upload:**
    *   Accepts PDF documents as input.
    *   ![PDF Upload](https://www.geekinstructor.com/wp-content/uploads/2024/12/Add-links-in-PDF-document-for-free.webp)

*   **Text Extraction:**
    *   Extracts text content from the uploaded PDF file.

*   **Semantic Embedding:**
    *   Utilizes the Sentence Transformer model to generate semantic embeddings of the extracted text.  These embeddings capture the meaning of the text.
    *   ![Embedding](https://media.geeksforgeeks.org/wp-content/uploads/cbow-1.png)

*   **Vector Storage (Pinecone):**
    *   Stores the text embeddings and the corresponding document name in a Pinecone vector database for fast and efficient similarity searches.
    *   If the pinecone index does not exits it automatically creates it.
    *   ![Pinecone](https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/file-uploads/blogs/2147721897/images/85ecfc8-5f3-86f8-5be6-cd27ff01c41_pinecone.jpeg)

*   **Question Answering:**
    *   Accepts user questions as input.
    *   Generates an embedding of the user's query using the Sentence Transformer model.
    *   Performs a similarity search in the Pinecone database to find relevant document snippets.
    *   Uses the Cohere language model to generate an answer based on the retrieved document snippets and the user's question.
    *   ![Cohere](https://cohere.com/logo.svg)



## Usage:

1.  Install the required Python libraries:

    ```bash
    pip install streamlit sentence-transformers pinecone-client cohere PyPDF2
    ```

2.  Obtain API keys for Cohere and Pinecone and configure your Pinecone environment. You need to add those in the script.

3.  Run the Streamlit app:

    ```bash
    streamlit run your_script_name.py
    ```

4.  Upload a PDF file, ask a question, and click "Submit" to receive the answer.
