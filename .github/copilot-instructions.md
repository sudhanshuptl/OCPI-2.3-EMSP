# Copilot Instructions

This document provides guidance for AI coding agents to effectively contribute to the OCPI-2.3-EMSP project.

## 1. Project Overview & Architecture

This project is an implementation of an OCPI 2.3 eMSP (e-Mobility Service Provider) server. The primary goal is to create a server for integration testing and validation with CPO (Charge Point Operator) systems.

-   **High-Level Goal:** Implement a compliant OCPI 2.3 eMSP server.
-   **Architectural Style:** The system is designed for flexibility, allowing it to run either as a single monolithic service or as a set of independent microservices (one for each OCPI module).
-   **Containerization:** When run as microservices, each module will operate in its own Docker container. Modules should be self-contained and communicate only through defined APIs.

## 2. Key Technologies

-   **Primary Language & Framework:** Python with FastAPI.
-   **Database:** PostgreSQL. All database interactions should use standard SQL or a compatible library.
-   **Core Specification:** OCPI 2.3. This is the most critical piece of external knowledge.

## 3. Development Workflow & Conventions

### OCPI-Specific Patterns

#### Response Structure
All OCPI endpoints MUST return responses in this format:
```json
{
  "data": <actual_data>,
  "status_code": 1000,
  "status_message": "Success",
  "timestamp": "2025-11-02T12:00:00Z"
}
```

**Key Points:**
- `data` field contains the actual response (object, array, or null)
- `status_code` is an OCPI status code (see below)
- `timestamp` must be in RFC3339 format (ISO 8601)
- Always use `datetime.now(timezone.utc).isoformat()` for timestamps

#### OCPI Status Codes
Use these standard OCPI status codes:

**Success Codes (1xxx):**
- `1000` - Success (generic)
- `1001` - Success with warning/additional info

**Client Errors (2xxx):**
- `2000` - Generic client error
- `2001` - Invalid or missing parameters
- `2002` - Not enough information (e.g., missing fields)
- `2003` - Unknown location

**Server Errors (3xxx):**
- `3000` - Generic server error
- `3001` - Unable to use client's API
- `3002` - Unsupported version
- `3003` - No matching endpoints

#### Module Structure
When creating a new OCPI module (e.g., `locations`, `sessions`):

1. Create directory: `versions/v2_3/<module_name>/`
2. Required files:
   - `__init__.py` - Module marker
   - `schemas.py` - Pydantic models for request/response
   - `models.py` - SQLAlchemy database models (if needed)
   - `api.py` - FastAPI router with endpoints
   - `crud.py` - Database operations (if needed)

3. Database models should use schema: `__table_args__ = {'schema': 'OCPI_2_3'}`

4. API router should follow pattern:
   ```python
   router = APIRouter(
       prefix="/ocpi/emsp/2.3/<module>",
       tags=["<Module Name>"],
   )
   ```

5. Register in `main.py`:
   ```python
   from versions.v2_3.<module>.api import router as <module>_router
   app.include_router(<module>_router)
   ```

#### OCPI Roles
- **eMSP as SENDER**: tokens, commands, chargingprofiles
- **eMSP as RECEIVER**: credentials, locations, sessions, cdrs, tariffs

#### Common Fields
- All objects with IDs should use type-specific ID fields (not generic "id")
- Timestamps: Always RFC3339 format, UTC timezone
- URLs: Use `HttpUrl` from Pydantic
- Country codes: ISO-3166 alpha-2 (e.g., "NL", "DE")
- Currency: ISO-4217 (e.g., "EUR", "USD")

#### Enums
Define all OCPI enums as Python Enums matching the spec exactly:
```python
class Status(str, Enum):
    AVAILABLE = "AVAILABLE"
    BLOCKED = "BLOCKED"
```

### API Implementation
-   **Source of Truth:** For any ambiguity regarding API endpoints, data structures, or protocol behavior, **always refer to the official OCPI 2.3 specification in `Document/OCPI-2.3.0.pdf`**. Do not guess or use information from other OCPI versions.
-   **Structure:** When adding a new OCPI module (e.g., `commands`, `tokens`), create a new top-level directory for it. This directory should contain all the logic, models, and API definitions for that module.
-   **Routing:** Each module should define its own FastAPI routes in a dedicated file (e.g., `locations/v1/api.py`). A central file can then aggregate these routes to run the project as a single service.

### Database
-   When defining database schemas or writing queries, ensure they are compatible with PostgreSQL.
-   All tables must be in the `OCPI_2_3` schema: `__table_args__ = {'schema': 'OCPI_2_3'}`
-   Use Alembic for all schema changes - never modify database directly.
-   Migration naming: `YYYYMMDD_HHMM_<revision>_<description>`

### Code and Project Structure
-   Follow best practices for organizing a FastAPI application.
-   Focus on writing clear, modular, and well-commented Python code.
-   New features should be developed within the appropriate module folder. If a suitable module doesn't exist, create one.
-   Use Python 3.9+ compatible syntax (no `|` union operator, use `Union` from typing).

### API Documentation (Swagger)
-   All Pydantic models should have pre-populated default values for easy testing in Swagger UI.
-   Use `Field(..., description="...")` for all model fields.
-   Include `json_schema_extra` examples in model Config.
-   Default values should be realistic and follow OCPI spec format.

### Error Handling
-   Use FastAPI's `HTTPException` for HTTP errors.
-   Map HTTP errors to OCPI status codes in response.
-   Always return OCPI response format, even for errors.
-   Log errors appropriately for debugging.

### Testing
-   Test endpoints using Swagger UI during development.
-   Verify response format matches OCPI specification exactly.
-   Check that timestamps are RFC3339 formatted.
-   Validate all enums and required fields.
