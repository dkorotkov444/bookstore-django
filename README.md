# Bookstore Django Application

A Django-based bookstore app with authentication, catalog browsing, customer/salesperson sections, and sales record search with chart visualization.

## Tech Stack

- Python 3
- Django 6
- SQLite by default (`db.sqlite3`) with optional `DATABASE_URL` override
- Pandas + Matplotlib (sales table + charts)
- Bootstrap 5 (UI)
- WhiteNoise + Gunicorn (production serving)

## What This Project Includes

- Custom login/logout views (`/login/`, `/logout/`)
- Auth-protected catalog and sales pages
- Book list + detail pages with uploaded cover images
- Sales records filtering by book title with chart output:
  - Bar chart
  - Pie chart
  - Line chart
- Basic customers and salespersons pages
- Django admin registrations for:
  - `Book`
  - `Sale`
  - `Customer`
  - `Salesperson`

## App Overview

- `bookstore/` (project config)
  - Global URL routing
  - Authentication/home views
  - Environment-based settings (`django-environ`)
- `books/`
  - `Book` model
  - Class-based list/detail views (`LoginRequiredMixin`)
- `sales/`
  - `Sale` model
  - Search form + records view (`@login_required`)
  - Pandas DataFrame rendering + Matplotlib chart generation
- `customers/`
  - `Customer` model
  - Basic customers home view
- `salespersons/`
  - `Salesperson` model linked to Django `User`
  - Basic salespersons home view

## URL Map

- `/` → Home
- `/login/` and `/logout/` → Authentication
- `/books/list/` and `/books/detail/<pk>/` → Catalog
- `/sales/` → Sales records search + chart
- `/customers/` → Customers home
- `/salespersons/` → Salespersons home
- `/admin/` → Django admin

## Project Structure

```text
bookstore-django/
├── manage.py
├── requirements.txt
├── Procfile
├── db.sqlite3
├── .env.example
├── README.md
├── bookstore/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
│   └── asgi.py
├── books/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   └── templates/books/
├── sales/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── utils.py
│   ├── admin.py
│   ├── migrations/
│   └── templates/sales/
├── customers/
│   ├── models.py
│   ├── views.py
│   └── templates/customers/
├── salespersons/
│   ├── models.py
│   ├── views.py
│   └── templates/salespersons/
├── templates/
│   ├── base.html
│   ├── home.html
│   └── auth/login.html
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── data/
└── media/
  ├── books/
  ├── customers/
  └── salespersons/
```

## Data Model Summary

- `Book`
  - `title`, `author`, `genre`, `book_type`, `price`, `pic`
- `Sale`
  - `book` (FK to `Book`), `quantity`, `amount`, `date_created`
- `Customer`
  - `name`, `notes`, `pic`
- `Salesperson`
  - `user` (OneToOne to Django `User`), `name`, `bio`, `pic`

## Setup (Windows PowerShell)

From the project root (`bookstore-django`):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
# Environment Setup: "Copy .env.example to .env and update your SECRET_KEY".
# Then open .env and set SECRET_KEY to a strong unique value.

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Environment Variables

The app reads configuration from `.env` via `django-environ`.

Minimum local settings:

```dotenv
SECRET_KEY=replace-with-your-own-value
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000
```

You can start from `.env.example` and adjust values per environment.

## Static and Media

- Static source: `static/`
- Collected static output: `staticfiles/` (used in production)
- Uploaded media root: `media/`

## Production Notes

- `Procfile` runs: `gunicorn bookstore.wsgi --log-file -`
- WhiteNoise is enabled in middleware for static files
- Security settings are applied when `DEBUG=False` (SSL redirect, secure cookies, HSTS, hardening headers)
- Run deployment checks before release:

```powershell
python manage.py check --deploy
```
