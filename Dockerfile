# Use an official Python runtime as a parent image
FROM python:3.11.3

# Set the working directory
WORKDIR /code

# Copy only the requirements file and install dependencies
COPY requirements.txt .
RUN cat requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "evacuation_management_system/manage.py", "runserver", "0.0.0.0:8000"]