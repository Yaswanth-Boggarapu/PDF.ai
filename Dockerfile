FROM python:3.11-slim-buster

# Install dependencies
RUN pip install streamlit pinecone cohere sentence-transformers PyPDF2

# Copy application code
COPY . /bot

# Set working directory
WORKDIR /bot

# Expose the Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "bot.py"]