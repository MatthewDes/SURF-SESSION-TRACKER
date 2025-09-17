# Surf Session Tracker (Phase 1)

A FastAPI project to track surf spots and sessions.  
Currently, all data is stored in memory (lost when the server restarts).  
Phase 1 implements CRUD basics for spots and sessions.

## Features
- **Spots**
  - Create a spot (`POST /spots`)
  - List all spots (`GET /spots`)
  - Get a spot by ID (`GET /spots/{spot_id}`)
  - Get all sessions at a spot (`GET /spots/{spot_id}/sessions`)

- **Sessions**
  - Create a session linked to a spot (`POST /sessions`)
  - List all sessions (`GET /sessions`)
  - Get a session by ID (`GET /sessions/{session_id}`)

## Requirements
- Python 3.10+
- See `requirements.txt` for dependencies.

## Setup
```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
