# Use official Python 3.11 slim image
FROM python:3.11

# Set working directory
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# Copy all project files
COPY . .

# Install dependencies if you have a requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Set memory limit to 2MB and run the script
CMD ["/bin/sh", "-c", "ulimit -v 1048576 && python test.py"] 