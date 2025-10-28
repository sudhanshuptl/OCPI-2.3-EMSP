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

### API Implementation
-   **Source of Truth:** For any ambiguity regarding API endpoints, data structures, or protocol behavior, **always refer to the official OCPI 2.3 specification in `Document/OCPI-2.3.0.pdf`**. Do not guess or use information from other OCPI versions.
-   **Structure:** When adding a new OCPI module (e.g., `commands`, `tokens`), create a new top-level directory for it. This directory should contain all the logic, models, and API definitions for that module.
-   **Routing:** Each module should define its own FastAPI routes in a dedicated file (e.g., `locations/v1/api.py`). A central file can then aggregate these routes to run the project as a single service.

### Database
-   When defining database schemas or writing queries, ensure they are compatible with PostgreSQL.

### Code and Project Structure
-   Follow best practices for organizing a FastAPI application.
-   Focus on writing clear, modular, and well-commented Python code.
-   New features should be developed within the appropriate module folder. If a suitable module doesn't exist, create one.
