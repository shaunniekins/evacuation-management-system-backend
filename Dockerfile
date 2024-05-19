# Use the official Python image as the base image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY . /app/

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the Django application
EXPOSE 8000

# Start the Django application using Gunicorn
CMD ["gunicorn", "evacuation_management_system.wsgi:application", "--bind", "0.0.0.0:8000"]