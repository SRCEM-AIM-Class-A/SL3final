FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY="dev-secret-key-change-in-production"

EXPOSE 5000

# Run with a non-root user for better security
RUN adduser --disabled-password --gecos '' flaskuser
USER flaskuser

CMD ["python", "app.py"] 