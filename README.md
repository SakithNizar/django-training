# Django Providers Management API

A Django REST Framework (DRF) project for managing service providers
with authentication, owner-based permissions, filtering, and automated
testing.

------------------------------------------------------------------------

## 🚀 Project Overview

This project allows users to:

-   Register an account
-   Authenticate using Token Authentication
-   Create and manage service providers
-   View providers with filtering, search, and ordering
-   Restrict updates/deletes to provider owners or admin
-   Run automated tests 

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python
-   Django
-   Django REST Framework (DRF)
-   SQLite (Default Database)
-   django-filter

------------------------------------------------------------------------

## 📂 Project Structure

django_training/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
│
├── training_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── providers/
    ├── models.py
    ├── views.py
    ├── serializers.py
    ├── permissions.py
    ├── api_urls.py
    ├── urls.py
    └── tests/
        ├── __init__.py
        ├── test_models.py
        ├── test_api.py
        └── test_permissions.py

------------------------------------------------------------------------

## ⚙️ Installation & Setup

1.  Clone Repository git clone `<your-repository-url>`{=html} cd
    django_training

2.  Create Virtual Environment python -m venv venv
    venv`\Scripts`{=tex}`\activate`{=tex}

3.  Install Dependencies pip install -r requirements.txt

4.  Apply Migrations python manage.py migrate

5.  Create Superuser python manage.py createsuperuser

6.  Run Server python manage.py runserver

Open in browser: http://127.0.0.1:8000/

------------------------------------------------------------------------

## 🔐 Authentication

Get Token: POST /api/token/

Example Body: { "username": "admin", "password": "yourpassword" }

Use in Header: Authorization: Token your_token_here

------------------------------------------------------------------------

## 🏢 Providers API Endpoints

| Method | Endpoint             | Description                           |
| ------ | -------------------- | ------------------------------------- |
| GET    | /api/providers/      | List providers                        |
| POST   | /api/providers/      | Create provider (owner auto-assigned) |
| GET    | /api/providers/{id}/ | View single provider                  |
| PUT    | /api/providers/{id}/ | Update provider (Owner/Admin only)    |
| DELETE | /api/providers/{id}/ | Delete provider (Owner/Admin only)    |


------------------------------------------------------------------------

## 🧪 Running Tests

From project root:

python manage.py test providers --verbosity=2

Expected Output: Ran 3 tests OK

------------------------------------------------------------------------

## 📌 Author

Mohamed Sakith M.N.

------------------------------------------------------------------------

## 📄 License

Testing purposes only.
