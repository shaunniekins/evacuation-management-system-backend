# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set the working directory
WORKDIR /code

# Copy only the requirements file
COPY requirements.txt /code/

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /code/

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]