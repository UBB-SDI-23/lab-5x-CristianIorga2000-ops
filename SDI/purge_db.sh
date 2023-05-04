#!/bin/bash

# Set PostgreSQL credentials
export PGUSER="cristian_iorga2000"
export PGPASSWORD="123"
export PGHOST="localhost"
export PGDATABASE="mpi"

# Drop the existing database
sudo dropdb --if-exists --username="$PGUSER" --host="$PGHOST" "$PGDATABASE"

# Create a new database
sudo createdb --username="$PGUSER" --host="$PGHOST" "$PGDATABASE"

# Run migrations
pipenv run python manage.py migrate

echo "All tables in the $PGDATABASE database have been truncated and their sequences have been reset."
