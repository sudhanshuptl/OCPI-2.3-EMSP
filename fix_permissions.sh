#!/bin/bash

# Script to fix database permissions for OCPI database with OCPI_2_3 schema

echo "Fixing database permissions..."

DB_NAME="OCPI"
SCHEMA_NAME="OCPI_2_3"
DB_USER="postgres"

# Run SQL commands to grant permissions
psql -U postgres -d $DB_NAME <<EOF
-- Create schema if it doesn't exist
CREATE SCHEMA IF NOT EXISTS "$SCHEMA_NAME";

-- Grant all privileges on the database
GRANT ALL PRIVILEGES ON DATABASE "$DB_NAME" TO $DB_USER;

-- Grant usage on the schema
GRANT ALL ON SCHEMA "$SCHEMA_NAME" TO $DB_USER;

-- Grant create on the schema
GRANT CREATE ON SCHEMA "$SCHEMA_NAME" TO $DB_USER;

-- Grant all privileges on all tables in schema
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA "$SCHEMA_NAME" TO $DB_USER;

-- Grant all privileges on all sequences in schema
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA "$SCHEMA_NAME" TO $DB_USER;

-- Set default privileges for future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA "$SCHEMA_NAME" GRANT ALL ON TABLES TO $DB_USER;
ALTER DEFAULT PRIVILEGES IN SCHEMA "$SCHEMA_NAME" GRANT ALL ON SEQUENCES TO $DB_USER;

-- Show current privileges
\l $DB_NAME
\dn+ "$SCHEMA_NAME"

EOF

echo "Permissions updated successfully!"
