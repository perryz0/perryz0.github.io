#!/bin/bash
# Script should be ran from the `MLH-Portfolio` project root


# kill the current `portfolio` tmux
tmux kill-session -t portfolio

# first retrieve latest changes
git fetch && git reset origin/main --hard

# enter venv and update dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# new tmux and then start server
tmux new-session -d -s portfolio 'cd ~/MLH-Portfolio && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'

