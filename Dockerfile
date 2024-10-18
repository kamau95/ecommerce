# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables
ENV FLASK_APP=web:create_app
ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=8080

# Expose the port on which the app will listen
EXPOSE $PORT

# Copy the script and make it executable
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Use JSON syntax for CMD
CMD ["/app/start.sh"]

