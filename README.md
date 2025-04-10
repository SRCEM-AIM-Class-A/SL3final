🚀 Flask + Django Dockerized Web App
This project showcases a containerized setup combining both Flask and Django applications. Each runs in its own Docker container, allowing for a seamless and modular development experience.

🧩 Overview
Flask App: A lightweight web app that collects a user's name and age, then greets them with a personalized message.

Django App: A simple task manager that lets users create, view, and delete tasks through a web interface.

📋 Prerequisites
Docker

Docker Compose

Git

📁 Project Structure
arduino
Copy
Edit
ShubhamSL3Final/
├── docker-compose.yml
├── flask_app/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       ├── form.html
│       ├── greeting.html
│       └── home.html
└── django_app/
    ├── Dockerfile
    ├── manage.py
    ├── requirements.txt
    ├── project/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── items/
        ├── models.py
        ├── views.py
        ├── urls.py
        └── templates/
            └── items/
                └── home.html
⚙️ Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/SRCEM-AIM-Class-A/ShubhamSL3Final.git
cd ShubhamSL3Final
2. Build & launch the containers
bash
Copy
Edit
docker-compose up --build
3. Open in browser
Flask App: http://localhost:5000

Django App: http://localhost:8000

Django Admin: http://localhost:8000/admin

4. Create a Django superuser (for admin access)
bash
Copy
Edit
docker-compose run django_app python manage.py createsuperuser
🌟 Features
🔸 Flask App
Welcome homepage

Form for name & age

Personalized greeting

Form validation with CSRF protection

🔹 Django App
Create, view, and delete tasks

User-friendly interface

Admin dashboard

SQLite database support

🐳 Dockerized Services
Service	Framework	Port	Key Tools
Flask App	Flask 2.x	5000	WTForms, Jinja2
Django App	Django 4.x	8000	Admin, ORM, Templates
🔐 Environment Variables
Flask
FLASK_ENV=development

FLASK_DEBUG=1

SECRET_KEY=your-secret

PYTHONUNBUFFERED=1

Django
DEBUG=1

PYTHONUNBUFFERED=1

🛠 Development Notes
Changes reflect immediately due to mounted volumes

Debug mode & auto-reload are enabled for both apps

🚀 Production Tips
Set DEBUG=False

Replace development secret keys

Use a production-ready database (e.g. PostgreSQL)

Serve with a WSGI server (e.g. Gunicorn, uWSGI)

📦 Docker Hub Images
You can pull the latest images here:

Flask App: [Docker Hub Flask App URL]

Django App: [Docker Hub Django App URL]

🤝 Contributing
Fork this repo

Create a feature branch

Commit your changes

Push your branch

Open a pull request!

📝 License
This project is licensed under the MIT License. See the LICENSE file for more details.