#!/bin/bash
# Script should be ran from the `/root` dir in the Droplet
# Current setup is using systemd to run the Flask app

# first retrieve latest changes
cd ~/MLH-Portfolio
git fetch && git reset origin/main --hard

# spin containers down to build fresh and deploy
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build
