# Dockerfile
# Use the official Python image as the base image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 10000

# Install the required packages
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the container
COPY . /app/

# Add execute permissions to start.sh
RUN chmod +x ./start.sh

EXPOSE 10000
CMD ["bash", "-c", "./start.sh"]