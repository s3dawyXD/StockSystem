#!/bin/bash
cd stock_system

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Run tests
echo "Running tests..."
python manage.py test

# Start Django app
echo "Starting Django application..."
python manage.py runserver 0.0.0.0:8000 &

# Keep the container running
wait
