#!/bin/bash

# Set PostgreSQL credentials
export PGUSER="your_database_user"
export PGPASSWORD="your_database_password"
export PGHOST="localhost"
export PGDATABASE="your_database_name"

# Drop the existing database
dropdb --if-exists --username="$PGUSER" --password="$PGPASSWORD" --host="$PGHOST" "$PGDATABASE"

# Create a new database
createdb --username="$PGUSER" --password="$PGPASSWORD" --host="$PGHOST" "$PGDATABASE"

# Run migrations
pipenv run python manage.py migrate

echo "All tables in the $PGDATABASE database have been truncated and their sequences have been reset."
