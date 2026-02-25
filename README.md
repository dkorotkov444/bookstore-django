# Bookstore Django Application

This repository contains a Django-based Bookstore web application with authentication, catalog browsing, customer/salesperson sections, and searchable sales records with chart visualization.

## Tech Stack

- Python 3
- Django 6
- SQLite (`db.sqlite3`)
- Pandas + Matplotlib (sales table/chart generation)
- Bootstrap 5 (UI)

## Features

- Authentication with custom login/logout views
- Protected pages using `login_required` and `LoginRequiredMixin`
- Book catalog list and book detail pages with image support
- Sales records search by book title and chart type (bar, pie, line)
- Customer and salesperson sections
- Django admin registrations for all core models (`Book`, `Sale`, `Customer`, `Salesperson`)

## URL Map

- `/` → Home page
- `/login/` and `/logout/` → Authentication
- `/books/list/` and `/books/detail/<pk>/` → Catalog
- `/sales/` → Sales records search and chart output
- `/customers/` → Customers section
- `/salespersons/` → Salespersons section
- `/admin/` → Django admin

## Setup (Windows PowerShell)

From the project root (`bookstore-py`):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install django pandas matplotlib pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Project Structure

```text
bookstore-py/
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
├── bookstore/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── books/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── books/
│           ├── detail.html
│           └── main.html
├── sales/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── sales/
│           └── records.html
├── customers/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── customers/
│           └── home.html
├── salespersons/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── salespersons/
│           └── salesperson.html
├── templates/
│   ├── base.html
│   ├── home.html
│   └── auth/
│       └── login.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── data/
│   │   └── test-books.json
│   ├── images/
│   │   └── bookstore.jpg
│   └── js/
│       └── home.js
└── media/
    ├── no_image.png
    ├── books/
    └── customers/
```

## Data Model Summary

- `Book`: title, author, genre, type, price, cover image
- `Sale`: linked `Book`, quantity, total amount, timestamp
- `Customer`: name, notes, image
- `Salesperson`: linked Django `User`, name, bio, image

## Notes

- Static files are served from `static/`; uploaded media is served from `media/`.
- Default login redirect goes to sales records (`sales:records`).

## Securioty considerations for cloud deployment

- Start from `.env.example` and create your local `.env` per environment.
- Keep `SECRET_KEY` in environment variables (never in source control).
- Set `DEBUG=False` in production.
- Define `ALLOWED_HOSTS` explicitly (comma-separated), for example: `yourdomain.com,www.yourdomain.com`.
- Define `CSRF_TRUSTED_ORIGINS` with full scheme, for example: `https://yourdomain.com,https://www.yourdomain.com`.
- Keep HTTPS and secure cookies enabled in production (`SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`).
- Add HSTS in production:
    - `SECURE_HSTS_SECONDS=31536000`
    - `SECURE_HSTS_INCLUDE_SUBDOMAINS=True`
    - `SECURE_HSTS_PRELOAD=True`
- Add explicit browser hardening headers:
    - `SECURE_CONTENT_TYPE_NOSNIFF=True`
    - `X_FRAME_OPTIONS=DENY`
    - `SECURE_REFERRER_POLICY=same-origin`
- Run deployment checks before release:

```powershell
python manage.py check --deploy
```

- If your cloud platform terminates TLS at a proxy/load balancer, also set:
    - `SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')`
