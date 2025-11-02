# OCPI 2.3 eMSP Server Implementation

This project provides a server-side implementation of the Open Charge Point Interface (OCPI) version 2.3 from the perspective of an e-Mobility Service Provider (eMSP).

The primary goal is to offer a compliant, ready-to-use eMSP server that can be used for development, testing, and integration purposes.

## Who is this project for?

This project is designed for two main groups:

1.  **Charge Point Operators (CPOs):** CPOs who are developing or have implemented OCPI 2.3 can use this eMSP server to test and validate their implementation. It provides a reliable counterparty for ensuring that their systems can correctly communicate with an eMSP.

2.  **e-Mobility Service Providers (eMSPs):** New or existing eMSPs can use this project as a foundation to:
    *   Quickly set up a compliant OCPI 2.3 server.
    *   Accelerate migration from older OCPI versions.
    *   Bootstrap their business operations around the OCPI protocol without building an entire system from scratch.

## Setup

### Database

Before running the application, you will need to have a PostgreSQL database set up.

#### macOS (using Homebrew)

```bash
# Install PostgreSQL version 15
brew install postgresql@15

# Start the PostgreSQL service
brew services start postgresql@15
```

- Connect via pgAdmin with usernamer = macusername and blank password
- create new user => `postgres` and password =  `password`

#### Linux (Debian/Ubuntu using APT)

```bash
# Update package list and install PostgreSQL
sudo apt-get update
sudo apt-get install -y postgresql

# The service should start automatically. You can check its status with:
sudo systemctl status postgresql
```
- Connect via pgAdmin with usernamer = macusername and blank password
- create new user => `postgres` and password =  `password`

### Create Database

Create a new database named `ocpi_emsp`:

```bash
# Using psql command line
psql -U postgres -c "CREATE DATABASE ocpi_emsp;"
```

Or use pgAdmin to create the database with the GUI.

### Python Environment Setup

1. **Create a virtual environment:**

```bash
python -m venv venv
```

2. **Activate the virtual environment:**

macOS/Linux:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

The default configuration is already set for local development with:
- Username: `postgres`
- Password: `password`
- Database: `ocpi_emsp`

5. **Run database migrations:**

```bash
alembic upgrade head
```

### Running the Application

Start the development server:

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive API docs (Swagger)**: http://localhost:8000/docs
- **Alternative API docs (ReDoc)**: http://localhost:8000/redoc
- **OCPI Versions**: http://localhost:8000/ocpi/emsp/versions

## OCPI Implementation Status

### ✅ Implemented Modules

- **Versions** (`/ocpi/emsp/versions`) - Lists available OCPI versions and endpoints

### 🚧 Planned Modules

- **Credentials** - Authentication and registration
- **Locations** - Charge point location data
- **Sessions** - Charging session information  
- **CDRs** - Charge Detail Records
- **Tariffs** - Pricing information
- **Tokens** - Authorization tokens
- **Commands** - Remote commands (START_SESSION, STOP_SESSION, etc.)
- **Charging Profiles** - Smart charging profiles

## Project Structure

```
OCPI-2.3-EMSP/
├── core/                   # Core application logic
│   ├── __init__.py
│   ├── config.py          # Application settings
│   └── database.py        # Database connection and session management
├── versions/              # OCPI version implementations
│   └── __init__.py
├── alembic/               # Database migrations
│   ├── versions/          # Migration scripts
│   └── env.py            # Alembic environment configuration
├── tests/                 # Test files
├── main.py               # Application entry point
├── requirements.txt      # Python dependencies
├── alembic.ini          # Alembic configuration
└── .env                 # Environment variables (not in git)
```

## Contributing

```
- Connect via pgAdmin with usernamer = macusername and blank password
- create new user => `postgres` and password =  `password`



## Contributing

Passionate open-source developers are welcome to contribute to this project! Whether you want to fix a bug, add a new feature, or improve the documentation, your help is appreciated. Please feel free to open an issue or submit a pull request.

