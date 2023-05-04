#!/bin/bash

# Set PostgreSQL credentials
export PGUSER="cristian_iorga2000"
export PGPASSWORD="123"
export PGHOST="localhost"
export PGDATABASE="mpi"

# Terminate all connections to the database
psql -c "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = '$PGDATABASE' AND pid <> pg_backend_pid();"

# Drop the existing database
sudo dropdb --if-exists --username="$PGUSER" --host="$PGHOST" "$PGDATABASE"

# Create a new database
sudo createdb --username="$PGUSER" --host="$PGHOST" "$PGDATABASE"

# Run migrations
pipenv run python manage.py migrate

echo "All tables in the $PGDATABASE database have been truncated and their sequences have been reset."
