# Use an official Python runtime as a base image
FROM python:3.11-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    NLTK_DATA=/user/share/nltk_data

# Set working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install system dependencies required by NLTK and pip packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download required NLTK resources
RUN python -m nltk.downloader -d $NLTK_DATA stopwords punkt wordnet

# Expose port for the application
EXPOSE 8000

# Run the application using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]