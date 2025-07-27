# damage-inspection-system

This backend API simulates a vehicle damage inspection workflow built using Django, postgreSQL, and JWT authentication.

##  Features Implemented

- JWT-based user authentication (Signup/Login)
- CRUD operations for vehicle inspections
- Inspection status updates: pending, reviewed, completed
- Image URL validation (.jpg, .jpeg, .png)
- Protected API endpoints using JWT
- Logging of all requests and error handling

---

##  Tech Stack

- Python (globally installed)
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Logging

---

## API Endpoints

### Authentication
- `POST /signup/` – Register a user
- `POST /login/` – Login and receive a JWT token

### Inspection (JWT Protected)
- `POST /inspection/` – Create a new inspection
- `GET /inspection/<id>/` – Retrieve inspection by ID
- `PATCH /inspection/<id>/` – Update inspection status
- `GET /inspection/?status=pending` – Filter inspections by status

---

##  How to Run Locally

```bash
# Clone the repository
git clone https://github.com/praveenkumar122002/damage-inspection-system.git
cd damage-inspection-system

# Install Python (if not already installed)
# On Windows, download from https://www.python.org/downloads/
# Then continue with the commands below

# Install dependencies globally (without virtual environment)
pip install django
pip install djangorestframework
pip install psycopg2
pip install djangorestframework-simplejwt
pip install bcrypt
pip install python # (Note: only required if using it in code as a package)

# If you're using extra packages like dj-database-url or pillow, install them too:
# pip install dj-database-url pillow

# Make sure PostgreSQL is installed and running locally
# Create a database (manually in pgAdmin or psql)

# In settings.py inside 'inspektlabs_project/':
# Set DATABASES like this (example):
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'your_db_name',
#         'USER': 'your_db_user',
#         'PASSWORD': 'your_db_password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver