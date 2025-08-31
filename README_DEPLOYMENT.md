# Ardi Agent Deployment Guide

This repository now includes a root Docker configuration that allows you to deploy both the frontend and backend components together in a single container.

## Deployment Options

### Option 1: Single Container Deployment (Recommended)

This approach uses a multi-stage Docker build to create a single container that runs both the frontend (served by Nginx) and backend (Flask API) using Supervisor.

#### Build and Run

```bash
# Build the image
docker build -t ardi-agent .

# Run the container
docker run -d \
  --name ardi-agent \
  -p 80:80 \
  -p 5000:5000 \
  -v $(pwd)/sessions:/app/backend/sessions \
  -v $(pwd)/logs:/var/log/supervisor \
  ardi-agent
```

#### Using Docker Compose (Production)

```bash
# Start the application
docker-compose -f docker-compose.prod.yml up -d

# Stop the application
docker-compose -f docker-compose.prod.yml down

# View logs
docker-compose -f docker-compose.prod.yml logs -f
```

### Option 2: Separate Containers (Development)

Use the original docker-compose.yml for development with separate containers:

```bash
# Start development environment
docker-compose up -d

# Stop development environment
docker-compose down
```

## Access Points

- **Frontend**: http://localhost (port 80)
- **Backend API**: http://localhost:5000
- **Logs**: Available in `./logs` directory (when using volume mount)
- **Sessions**: Persisted in `./sessions` directory

## Architecture

The single container deployment includes:

1. **Nginx**: Serves the React frontend on port 80
2. **Flask API**: Runs the backend service on port 5000
3. **Supervisor**: Manages both services within the container
4. **Volume Mounts**: For session persistence and log access

## Configuration Files

- `Dockerfile`: Multi-stage build for production deployment
- `docker-compose.prod.yml`: Production docker-compose configuration
- `supervisord.conf`: Supervisor configuration for managing services
- `docker-compose.yml`: Original development configuration (separate containers)

## Troubleshooting

### View Container Logs
```bash
# For single container deployment
docker logs ardi-agent

# For docker-compose deployment
docker-compose -f docker-compose.prod.yml logs
```

### Access Container Shell
```bash
docker exec -it ardi-agent /bin/bash
```

### Check Service Status
```bash
# Inside the container
supervisorctl status
```

## Environment Variables

The following environment variables are set in the container:
- `FLASK_APP=src/main.py`
- `FLASK_ENV=production`

You can override these by modifying the docker-compose.prod.yml file or passing them during docker run.

