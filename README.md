# hng14-stage2-devops

## 🟢 STEP 4 — Fix Bugs + Document

### File: api/main.py (Line 10)
Problem: Hardcoded Redis URL
Fix: Replaced with REDIS_URL environment variable for better configuration and deployment flexibility

---

### File: worker/worker.py (Line 12)
Problem: Hardcoded Redis connection URL/host in code
Fix: Replaced with environment variables (REDIS_HOST, REDIS_PORT) to improve scalability and environment management

---

### File: worker/worker.py (Line 25)
Problem: Missing error handling for Redis connection failure
Fix: Added try/except block to handle Redis connection errors and prevent worker crashes

## Setup

git clone <repo>
cd repo
docker-compose up --build

## Access
Frontend: http://localhost:3000
API: http://localhost:8000
