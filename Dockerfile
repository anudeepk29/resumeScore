# Use the official Ubuntu image as the base image
FROM ubuntu:latest

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install Python, pip, and any necessary dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Create a working directory
WORKDIR /app

# Copy the Python application code into the container
COPY . /app

# (Optional) Install Python dependencies from requirements.txt
# If you have a requirements.txt file, uncomment the following line
RUN pip3 install --no-cache-dir -r requirements.txt

# Specify the command to run your Python application
# Replace 'app.py' with the name of your Python script
CMD ["python3", "main.py"]
