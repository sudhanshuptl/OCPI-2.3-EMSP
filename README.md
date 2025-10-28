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



## Contributing

Passionate open-source developers are welcome to contribute to this project! Whether you want to fix a bug, add a new feature, or improve the documentation, your help is appreciated. Please feel free to open an issue or submit a pull request.

