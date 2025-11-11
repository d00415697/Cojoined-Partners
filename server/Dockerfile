# Backend Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py db.py ./

RUN touch messages.db && chmod 777 messages.db

# Expose port (default Flask port, but configurable via env)
EXPOSE 5000

# Set environment variable for Flask to listen on all interfaces
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Run the application
CMD ["python", "app.py"]

