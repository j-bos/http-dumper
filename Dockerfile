# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY dumper.py /app

# Install Flask
RUN pip install flask

# Expose the application's port
EXPOSE 8080

# Run the application
CMD ["python", "dumper.py"]
