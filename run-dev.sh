#!/usr/bin/env zsh
set -euo pipefail

########################################
# CONFIGURE THESE FOR YOUR PROJECT
########################################

# Directories are relative to this script
BACKEND_DIR="rag-backend"
FRONTEND_DIR="rag-frontend"

# Commands to start each server (use EXACTLY what you normally type)
# These are arrays so arguments are handled safely.
BACKEND_CMD=(uvicorn app.main:app --reload --host 0.0.0.0 --port 8000)
FRONTEND_CMD=(npm run dev)

########################################
# DO NOT EDIT BELOW UNLESS NEEDED
########################################

# Array of child PIDs so we can clean them up
pids=()

cleanup() {
  echo
  echo "Stopping servers..."

  if [[ ${#pids[@]} -gt 0 ]]; then
    # Try graceful stop first
    kill "${pids[@]}" 2>/dev/null || true
    sleep 2
    # Force kill anything still running
    kill -9 "${pids[@]}" 2>/dev/null || true
  fi

  echo "All servers stopped."
}

trap 'cleanup; exit 0' INT TERM

start_backend() {
  (
    cd "$BACKEND_DIR"
    # If a local virtualenv exists, activate it; otherwise just run with current env
    if [[ -f venv311/bin/activate ]]; then
      source venv311/bin/activate
    fi
    "${BACKEND_CMD[@]}"
  ) &
  pids+=($!)
}

start_frontend() {
  (
    cd "$FRONTEND_DIR"
    "${FRONTEND_CMD[@]}"
  ) &
  pids+=($!)
}

echo "Starting backend in ${BACKEND_DIR}..."
start_backend

echo "Starting frontend in ${FRONTEND_DIR}..."
start_frontend

echo
echo "Both servers are running."
echo "Press Ctrl+C to stop them both."

# Wait for all child processes
wait
