# Event Registration System

A Django application for simple event registration with custom validation.

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Optional - for admin panel)
```bash
python manage.py createsuperuser
```

### 5. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Access the Registration Form
- **Registration Form**: http://127.0.0.1:8000/events/register/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Validation Rules
- **Full Name**: Minimum 5 characters
- **Email**: Must end with @gmail.com
- **Age**: Must be 18 or above
- **Password**: Minimum 8 characters

## Project Structure
```
.
├── manage.py
├── requirements.txt
├── config/              # Main project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── events/              # Event registration app
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── templates/
        └── events/
            ├── register.html
            └── success.html
```
