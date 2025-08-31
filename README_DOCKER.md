# Docker Setup for Ardi Agent

This Docker configuration allows you to run both the backend (Flask API) and frontend (React app) components of the Ardi Agent application in containers.

## Prerequisites

- Docker and Docker Compose installed on your system
- Git (to clone the repository)

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nexuss0781/Ardi_agent.git
   cd Ardi_agent
   ```

2. **Build and start the containers:**
   ```bash
   docker compose up --build -d
   ```

3. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

## Services

### Backend (Flask API)
- **Port:** 5000
- **Container:** ardi_backend
- **Technology:** Python 3.11 with Flask
- **Features:**
  - CORS enabled for frontend communication
  - SQLite database with automatic initialization
  - Session management
  - RESTful API endpoints

### Frontend (React App)
- **Port:** 3000 (mapped from container port 80)
- **Container:** ardi_frontend
- **Technology:** React with Vite, served by Nginx
- **Features:**
  - Modern React 19 with TypeScript support
  - Tailwind CSS for styling
  - Radix UI components
  - Production-optimized build

## File Structure

```
Ardi_agent/
├── docker-compose.yml          # Main orchestration file
├── .dockerignore              # Files to exclude from Docker context
├── ardi_chat_api/
│   ├── Dockerfile             # Backend container configuration
│   ├── requirements.txt       # Python dependencies
│   └── src/                   # Backend source code
└── ardi_chat_frontend/
    ├── Dockerfile             # Frontend container configuration
    ├── nginx.conf             # Nginx configuration
    ├── package.json           # Node.js dependencies
    └── src/                   # Frontend source code
```

## Docker Commands

### Start services
```bash
docker compose up -d
```

### Stop services
```bash
docker compose down
```

### View logs
```bash
# All services
docker compose logs

# Specific service
docker compose logs backend
docker compose logs frontend
```

### Rebuild containers
```bash
docker compose build --no-cache
docker compose up -d
```

### Check service status
```bash
docker compose ps
```

## Configuration Details

### Backend Configuration
- Uses Python 3.11 slim image
- Installs dependencies from requirements.txt
- Runs Flask application on 0.0.0.0:5000
- Mounts sessions directory for persistence
- Automatic database initialization

### Frontend Configuration
- Multi-stage build: Node.js for building, Nginx for serving
- Uses pnpm for package management
- Optimized production build with Vite
- Nginx serves static files with proper caching headers
- Supports client-side routing

### Network Configuration
- Both services run on a custom bridge network (ardi_network)
- Backend and frontend can communicate internally
- External access via mapped ports

## Troubleshooting

### Container won't start
1. Check logs: `docker compose logs [service_name]`
2. Verify ports aren't already in use
3. Ensure Docker daemon is running

### Build failures
1. Clean Docker cache: `docker system prune -a`
2. Rebuild without cache: `docker compose build --no-cache`

### Permission issues
1. Ensure Docker daemon is running
2. Add user to docker group: `sudo usermod -aG docker $USER`
3. Restart terminal session

## Development

For development purposes, you can:

1. **Mount source code as volumes** (add to docker-compose.yml):
   ```yaml
   volumes:
     - ./ardi_chat_api/src:/app/src
     - ./ardi_chat_frontend/src:/app/src
   ```

2. **Enable hot reload** by modifying the Dockerfile commands

3. **Use development builds** instead of production builds

## Production Deployment

For production deployment:

1. Set proper environment variables
2. Use production-grade database (PostgreSQL/MySQL)
3. Configure proper logging
4. Set up reverse proxy (Nginx/Apache)
5. Enable HTTPS/SSL certificates
6. Configure monitoring and health checks

## Security Notes

- Change default Flask SECRET_KEY in production
- Use environment variables for sensitive configuration
- Enable proper authentication and authorization
- Regular security updates for base images
- Network isolation and firewall rules

