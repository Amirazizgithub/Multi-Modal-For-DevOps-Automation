# Start with your base Python image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data directly into the image
# It's good practice to set NLTK_DATA to a known path within the image
ENV NLTK_DATA /usr/local/nltk_data
RUN mkdir -p $NLTK_DATA \
    && python -m nltk.downloader -d $NLTK_DATA stopwords punkt wordnet punkt_tab

# Copy the rest of your application code
COPY . .

# Expose the port your FastAPI application listens on (e.g., 8000)
EXPOSE 8000

# Command to run your FastAPI application with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]