export PGUSER="cristian_iorga2000"
export PGPASSWORD="123"
export PGHOST="localhost"
export PGDATABASE="mpi"

# Retrieve the number of entries from all tables and print the results
psql -c "SELECT schemaname, relname, n_live_tup FROM pg_stat_user_tables ORDER BY n_live_tup DESC;"