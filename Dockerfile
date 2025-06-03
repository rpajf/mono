# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies if you have a requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Set memory limit to 2MB and run the script
CMD ["/bin/sh", "-c", "ulimit -v 2048 && python test.py"] 