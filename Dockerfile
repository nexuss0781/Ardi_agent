# Root Dockerfile for Ardi Agent
# Multi-stage build for both frontend and backend

# Stage 1: Build Frontend
FROM node:20-alpine AS frontend-builder

WORKDIR /app/frontend

# Copy frontend package files
COPY ardi_chat_frontend/package.json ardi_chat_frontend/pnpm-lock.yaml ./

# Install pnpm
RUN npm install -g pnpm

# Install frontend dependencies
RUN pnpm install

# Copy frontend source code
COPY ardi_chat_frontend/ ./

# Build the frontend application
RUN pnpm run build

# Stage 2: Build Backend
FROM python:3.11-slim AS backend-builder

WORKDIR /app/backend

# Copy backend requirements
COPY ardi_chat_api/requirements.txt ./

# Install backend dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY ardi_chat_api/ ./

# Stage 3: Production - Nginx + Python
FROM python:3.11-slim AS production

# Install nginx and supervisor
RUN apt-get update && apt-get install -y \
    nginx \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Create application directory
WORKDIR /app

# Copy backend from builder stage
COPY --from=backend-builder /app/backend ./backend
COPY --from=backend-builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=backend-builder /usr/local/bin /usr/local/bin

# Copy frontend build from builder stage
COPY --from=frontend-builder /app/frontend/dist /var/www/html

# Copy nginx configuration
COPY ardi_chat_frontend/nginx.conf /etc/nginx/sites-available/default

# Create supervisor configuration
RUN mkdir -p /var/log/supervisor

# Copy supervisor configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Create sessions directory
RUN mkdir -p /app/backend/sessions

# Expose ports
EXPOSE 80 5000

# Set environment variables
ENV FLASK_APP=src/main.py
ENV FLASK_ENV=production

# Start supervisor to manage both nginx and flask
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

