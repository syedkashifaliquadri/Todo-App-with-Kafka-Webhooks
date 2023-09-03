# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container at /app
COPY . .

# Install Requirements
RUN pip install -r requirements.txt

# Expose port for gRPC server
EXPOSE 50051

# Command to run the gRPC server
CMD ["python", "main.py"]
