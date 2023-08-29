# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container at /app
COPY app /app/

# Install gRPC dependencies
RUN pip install grpcio grpcio-tools

# Install Kafka dependencies
RUN pip install confluent-kafka

# Install PostgreSQL client
RUN pip install psycopg2-binary

# Install Flask dependencies
RUN pip install flask

# Expose port for gRPC server
EXPOSE 50051

# Command to run the gRPC server
CMD ["python", "main.py"]
