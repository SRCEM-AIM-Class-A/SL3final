# Flask and Django Docker Application

This project demonstrates a containerized web application setup using both Flask and Django frameworks. The application consists of two separate services that run simultaneously:

1. **Flask Application**: A simple web app that handles user input (name and age) and displays personalized greetings.
2. **Django Application**: A task management system that allows users to create, view, and delete items through a web interface.

## Prerequisites

- Docker
- Docker Compose
- Git

## Project Structure

```
project_root/
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
```

## Quick Start

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Build and run the containers:
```bash
docker-compose up --build
```

3. Access the applications:
- Flask app: http://localhost:5000
- Django app: http://localhost:8000
- Django admin: http://localhost:8000/admin

4. For Django admin access:
```bash
docker-compose run django_app python manage.py createsuperuser
```

## Features

### Flask Application
- Homepage with a greeting
- Form to collect user information
- Display personalized greeting based on user input
- CSRF protection
- Form validation

### Django Application
- List view of items
- Add new items through a form
- Delete existing items
- Admin interface for managing items
- Database persistence

## Docker Configuration

The project uses Docker Compose to manage two containers:

1. Flask Container:
   - Python 3.9
   - Flask web framework
   - WTForms for form handling
   - Development server on port 5000

2. Django Container:
   - Python 3.9
   - Django web framework
   - SQLite database
   - Development server on port 8000

## Environment Variables

### Flask App
- FLASK_ENV: development
- FLASK_DEBUG: 1
- SECRET_KEY: Custom secret key for security
- PYTHONUNBUFFERED: 1

### Django App
- DEBUG: 1
- PYTHONUNBUFFERED: 1

## Development

To make changes to the application:

1. The code is mounted as volumes, so changes will reflect immediately
2. Both applications have debug mode enabled for development
3. Auto-reload is enabled for both services

## Production Deployment

For production deployment:

1. Change debug settings to False
2. Use proper secret keys
3. Configure proper database settings for Django
4. Use production-grade servers instead of development servers

## Docker Hub Images

The Docker images are available at:
- Flask App: [Docker Hub URL for Flask App]
- Django App: [Docker Hub URL for Django App]

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 