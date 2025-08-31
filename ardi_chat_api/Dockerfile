# Backend Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=src/main.py
ENV FLASK_ENV=production

# Run the application
CMD ["python", "src/main.py"]

