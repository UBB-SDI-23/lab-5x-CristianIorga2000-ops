#!/bin/bash

# Kill all Python and Node background processes
pkill -9 python
pkill -9 node

# Restart Nginx
sudo systemctl restart nginx

# Run backend and frontend servers in the background
cd /path/to/backend
nohup pipenv run python manage.py runserver > backend.log 2>&1 &
cd /path/to/frontend
nohup npm run dev > frontend.log 2>&1 &
cd ..