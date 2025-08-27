#!/bin/bash
# Script should be ran from the `/root` dir in the Droplet
# Current setup is using Docker Compose for the Astro static site

set -euo pipefail

echo "[deploy] pulling latest..."
cd ~/MLH-Portfolio
git fetch origin main
git reset --hard origin/main

echo "[deploy] bringing stack up (build -> copy -> serve)..."
docker compose -f docker-compose.prod.yml up -d --build --force-recreate

echo "[deploy] verifying HTML is fresh..."
docker exec -it nginx sh -lc \
  'grep -n "/src/styles/globals.css" /usr/share/nginx/html/thoughts/hello-world/index.html || echo "OK: no stale css path"'

echo "[deploy] done -> https://perryz0.duckdns.org"
