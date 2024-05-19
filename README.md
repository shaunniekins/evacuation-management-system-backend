# Development Setup

Before starting, make sure to create a `.env` file in your project root directory with the following variables:

```bash
# Django settings
SECRET_KEY=[your-secret-key]
DEBUG=True
DJANGO_ALLOWED_HOSTS=*

# Django superuser settings
CREATE_SUPERUSER=True
DJANGO_SUPERUSER_USERNAME=[your-admin-username]
DJANGO_SUPERUSER_EMAIL=[your-admin-email]
DJANGO_SUPERUSER_PASSWORD=[your-admin-password]

POSTGRES_DB=[your-postgres-database]
POSTGRES_USER=[your-postgres-user]
POSTGRES_PASSWORD=[your-postgres-password]
POSTGRES_HOST=[your-postgres-host]
POSTGRES_PORT=[your-postgres-port]

# Database URL
# External database URL for outside Render (local development)
# Internal database URL for inside Render (eg. web service)

# External database URL (use the Internal for the env variable in Render)
DATABASE_URL=[your-postgresql-db-url]
```

1. Navigate to the project directory:

   ```bash
   cd evacuation-management-system-backend
   ```

   Alternatively, if you're using Visual Studio Code, you can open the project directory with:

   ```bash
   code evacuation-management-system-backend
   ```

2. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

   If not yet created

   ```bash
   python3 -m venv venv
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   If the tables are not yet created, create a new migration file for your model (replace 'backend' with your app name):

   ```bash
   python manage.py makemigrations backend
   ```

   Then, apply the migration to create the table in the database:

   ```bash
   python manage.py migrate
   ```

   If the tables are already created, you only need to make migrations:

   ```bash
   python manage.py makemigrations
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

Now, your development environment is set up and running. You can access the application at `http://localhost:8000`.