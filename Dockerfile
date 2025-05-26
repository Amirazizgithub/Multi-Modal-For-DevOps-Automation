# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set environment variable to avoid interactive prompts
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download necessary NLTK data
RUN python -m nltk.downloader stopwords punkt wordnet

# Make port 8000 available to the world outside this container
EXPOSE 8000 

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]