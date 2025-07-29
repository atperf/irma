# IRMA

IRMA (Industrial Robust Management Automation) is a platform for managing operational performance and continuous improvement. This repository provides a basic skeleton of the system including:

- **FastAPI backend** with SQLAlchemy models
- **Next.js frontend**
- Simple AI agent placeholder

## Quick Start

### Backend

```bash
cd backend
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend dev server runs on `http://localhost:3000` and proxies API requests to the backend.
