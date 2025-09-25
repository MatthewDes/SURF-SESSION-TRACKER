# Phase 2: Core Backend To-Do List

This phase focuses on transitioning from in-memory persistence to a real database, implementing user authentication, and establishing full CRUD (Create, Read, Update, Delete) operations for Spots and Sessions with proper validation and error handling.

## Database Setup & ORM
- [x] **Choose a Database:** Decide between SQLite (for development) and PostgreSQL (for production).
- [x] **Install Database Driver:** Install the appropriate Python package (e.g., `psycopg2-binary` for PostgreSQL, `sqlite3` is built-in).
- [x] **Configure SQLAlchemy:**
    - [x] Set up database connection string.
    - [x] Initialize SQLAlchemy engine and session.
- [x] **Define SQLAlchemy Models:**
    - [x] Convert existing Pydantic `Spot` and `Session` schemas into SQLAlchemy ORM models.
    - [x] Add necessary fields (e.g., primary keys, foreign keys for user association).
    - [x] Define relationships between models (e.g., User-Spot, User-Session, Spot-Session). (have not created users yet.)

## Database Migrations with Alembic
- [ ] **Install Alembic:** Add `alembic` to `requirements.txt` and install.
- [ ] **Initialize Alembic:** Run `alembic init` to set up migration environment.
- [ ] **Configure Alembic:** Update `alembic.ini` and `env.py` to connect to your database and use your SQLAlchemy models.
- [ ] **Create Initial Migration:** Generate the first migration script to create tables for `Spot`, `Session`, and `User` models.
- [ ] **Apply Migrations:** Run `alembic upgrade head` to apply the migrations to your database.

## User Authentication (JWT)
- [ ] **Install Authentication Libraries:** Add `python-jose[cryptography]` and `passlib[bcrypt]` (or `passlib[argon2]`) to `requirements.txt` and install.
- [ ] **Define User Model:** Create a SQLAlchemy model for `User` with fields like `id`, `email`, `hashed_password`.
- [ ] **Implement Password Hashing:** Use `bcrypt` or `argon2` to securely hash user passwords.
- [ ] **Create Authentication Endpoints:**
    - [ ] **User Registration (`/register`):**
        - [ ] Accept `email` and `password`.
        - [ ] Hash password and store user in DB.
        - [ ] Return success message or user data (without password).
    - [ ] **User Login (`/login`):**
        - [ ] Accept `email` and `password`.
        - [ ] Verify password against hashed password in DB.
        - [ ] Generate JWT access token upon successful login.
        - [ ] Return access token.
- [ ] **Implement JWT Dependency:**
    - [ ] Create a FastAPI dependency to decode JWT tokens and authenticate users for protected routes.
    - [ ] Extract user ID from token.

## CRUD Endpoints for Spots & Sessions
- [ ] **Refactor Routers:** Update `routers/spots.py` and `routers/sessions.py` to use SQLAlchemy for database interactions instead of in-memory storage.
- [ ] **Implement Protected Routes:** Apply the JWT authentication dependency to all CRUD endpoints for Spots and Sessions.
- [ ] **Ensure User Ownership:** Modify CRUD operations to ensure users can only access/modify their own Spots and Sessions.
- [ ] **Create Endpoints for Spots:**
    - [ ] `POST /spots`: Create a new surf spot (requires authentication).
    - [ ] `GET /spots`: Retrieve all user's surf spots (requires authentication).
    - [ ] `GET /spots/{spot_id}`: Retrieve a specific surf spot by ID (requires authentication and ownership).
    - [ ] `PUT /spots/{spot_id}`: Update a surf spot by ID (requires authentication and ownership).
    - [ ] `DELETE /spots/{spot_id}`: Delete a surf spot by ID (requires authentication and ownership).
- [ ] **Create Endpoints for Sessions:**
    - [ ] `POST /sessions`: Create a new surf session (requires authentication).
    - [ ] `GET /sessions`: Retrieve all user's surf sessions (requires authentication).
    - [ ] `GET /sessions/{session_id}`: Retrieve a specific surf session by ID (requires authentication and ownership).
    - [ ] `PUT /sessions/{session_id}`: Update a surf session by ID (requires authentication and ownership).
    - [ ] `DELETE /sessions/{session_id}`: Delete a surf session by ID (requires authentication and ownership).

## Validation & Error Handling
- [ ] **Pydantic Validation:** Ensure all incoming request data is validated using Pydantic models.
- [ ] **Database Error Handling:** Implement `try-except` blocks for database operations to catch and handle potential errors (e.g., unique constraint violations, not found errors).
- [ ] **Custom Exceptions:** Define custom exceptions for common application errors (e.g., `UserNotFound`, `SpotNotFound`, `UnauthorizedAccess`).
- [ ] **FastAPI Exception Handlers:** Register custom exception handlers to return appropriate HTTP status codes and error messages.

## Testing
- [ ] **Update Existing Tests:** Modify `tests/test_spots.py` and `tests/test_sessions.py` to interact with the real database and include authentication.
- [ ] **Add Authentication Tests:** Write new tests for user registration, login, and JWT token validation.
- [ ] **Add Ownership Tests:** Ensure tests cover scenarios where users try to access/modify resources they don't own.
- [ ] **Test Error Handling:** Write tests to verify that error conditions are handled correctly and return expected responses.

---
**Acceptance Criteria for Phase 2:**
- All endpoints for Spots and Sessions are protected by JWT authentication.
- User registration and login functionality is working correctly.
- All data (Users, Spots, Sessions) is persistently stored in the chosen database.
- Users can only perform CRUD operations on their own Spots and Sessions.
- Robust validation and error handling are in place for all API interactions.
- All tests pass, covering database interactions, authentication, and ownership.
