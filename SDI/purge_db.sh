#!/bin/bash

# Set PostgreSQL credentials
export PGUSER="your_database_user"
export PGPASSWORD="your_database_password"
export PGHOST="localhost"
export PGDATABASE="your_database_name"

# Drop the existing database
sudo dropdb --if-exists --username="$PGUSER" --host="$PGHOST" "$PGDATABASE"

# Create a new database
sudo createdb --username="$PGUSER" --host="$PGHOST" "$PGDATABASE"

# Run migrations
pipenv run python manage.py migrate

echo "All tables in the $PGDATABASE database have been truncated and their sequences have been reset."
