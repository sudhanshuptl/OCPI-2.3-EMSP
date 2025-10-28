#!/bin/bash

# Database setup script for OCPI eMSP Server

echo "=== OCPI eMSP Database Setup ==="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Database credentials
DB_USER="postgres"
DB_PASSWORD="password"
DB_NAME="ocpi_emsp"
DB_HOST="localhost"
DB_PORT="5432"

echo "This script will create the database for OCPI eMSP Server"
echo "Database: $DB_NAME"
echo "User: $DB_USER"
echo ""

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null; then
    echo -e "${RED}PostgreSQL is not installed or not in PATH${NC}"
    echo ""
    echo "Please install PostgreSQL first:"
    echo ""
    echo "macOS (using Homebrew):"
    echo "  brew install postgresql@15"
    echo "  brew services start postgresql@15"
    echo ""
    echo "Linux (Debian/Ubuntu):"
    echo "  sudo apt-get update"
    echo "  sudo apt-get install -y postgresql"
    echo ""
    exit 1
fi

echo -e "${GREEN}PostgreSQL is installed${NC}"

# Create database
echo ""
echo "Creating database '$DB_NAME'..."

# Try to create database
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -c "CREATE DATABASE $DB_NAME;" 2>/dev/null

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Database '$DB_NAME' created successfully!${NC}"
else
    # Check if database already exists
    PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -lqt | cut -d \| -f 1 | grep -qw $DB_NAME
    if [ $? -eq 0 ]; then
        echo -e "${YELLOW}Database '$DB_NAME' already exists${NC}"
    else
        echo -e "${RED}Failed to create database. Please check your PostgreSQL connection.${NC}"
        echo ""
        echo "Try running this command manually:"
        echo "  psql -U $DB_USER -c \"CREATE DATABASE $DB_NAME;\""
        exit 1
    fi
fi

echo ""
echo -e "${GREEN}=== Setup Complete ===${NC}"
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Run database migrations:"
echo "   alembic upgrade head"
echo ""
echo "3. Start the application:"
echo "   python main.py"
echo ""
