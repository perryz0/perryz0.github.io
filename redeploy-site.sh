#!/bin/bash
# Script should be ran from the `/root` dir in the Droplet
# Current setup is using Docker Compose for the Astro static site

set -e  # Exit on any error

echo "Starting deployment..."

# First retrieve latest changes
echo "Fetching latest changes..."
cd ~/MLH-Portfolio
git fetch && git reset origin/main --hard

# Stop and remove any existing containers to avoid conflicts
echo "Stopping existing containers..."
docker compose -f docker-compose.prod.yml down --remove-orphans 2>/dev/null || true

# Force remove any lingering containers that might cause conflicts
echo "Cleaning up any lingering containers..."
docker rm -f myportfolio nginx 2>/dev/null || true

# Remove any orphaned containers
echo "Removing orphaned containers..."
docker container prune -f

# Build and start fresh containers
echo "Building and starting containers..."
docker compose -f docker-compose.prod.yml up -d --build

# Wait a moment for containers to start
echo "Waiting for containers to start..."
sleep 5

# Check if containers are running
echo "Checking container status..."
if docker ps | grep -q "myportfolio\|nginx"; then
    echo "Deployment successful! Containers are running."
    echo "Your site should be available at: https://perryz0.duckdns.org"
else
    echo "Deployment failed! Containers are not running."
    echo "Container logs:"
    docker compose -f docker-compose.prod.yml logs
    exit 1
fi
