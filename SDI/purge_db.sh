#!/bin/bash

# Set PostgreSQL credentials
export PGUSER="your_database_user"
export PGPASSWORD="your_database_password"
export PGHOST="localhost"
export PGDATABASE="your_database_name"

# Execute SQL command to truncate all tables and reset sequences
psql <<EOF
DO \$\$
DECLARE
   r RECORD;
BEGIN
   FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
       EXECUTE 'TRUNCATE TABLE ' || quote_ident(r.tablename) || ' CASCADE';
   END LOOP;
   
   FOR r IN (SELECT column_name, column_default FROM information_schema.columns WHERE column_default LIKE 'nextval%' AND table_schema = current_schema()) LOOP
       EXECUTE 'ALTER SEQUENCE ' || substring(r.column_default from '^nextval\(''(.*?)''\:.+') || ' RESTART WITH 1';
   END LOOP;
END \$\$;
EOF

echo "All tables in the $PGDATABASE database have been truncated and their sequences have been reset."
