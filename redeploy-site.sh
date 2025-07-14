#!/bin/bash
# Script should be ran from the `/root` dir in the Droplet
# Current setup is using systemd to run the Flask app

# first retrieve latest changes
cd ~/MLH-Portfolio
git fetch && git reset origin/main --hard

# enter venv and update dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# restart systemd service
sudo systemctl restart myportfolio