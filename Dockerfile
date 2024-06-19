# Use the official Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY producer_consumer.py .

# Run the Python script
CMD ["python", "-u", "producer_consumer.py"]
