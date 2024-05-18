# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY . /app/

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Collect the static files
RUN python manage.py collectstatic --no-input

# Expose the port for the Django application
EXPOSE 8000

# Set the environment variables for Django and MySQL
ENV SECRET_KEY='django-insecure-_64x)^%!axvbhgxm%qt7#tnobo-@c#5^zor$lc05s(9+=otrl3'
ENV DEBUG=True
ENV DJANGO_ALLOWED_HOSTS='*'
ENV MYSQL_DATABASE=evacuation_management_system
ENV MYSQL_ROOT_PASSWORD=Hello_World123
ENV MYSQL_PASSWORD=Hello_World123
ENV MYSQL_USER=root

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]