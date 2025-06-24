#!/bin/bash

set -e

MIGRATIONS_DIR="./migrations/versions"

if [ ! -d "$MIGRATIONS_DIR" ] || [ -z "$(ls -A $MIGRATIONS_DIR)" ]; then
  poetry run alembic revision --autogenerate -m "Initial migration"
  echo "Initial migrations created"
  poetry run alembic upgrade head
  echo "Migrations updated"
else
  poetry run alembic upgrade head
  echo "Migrations updated"
fi

poetry run uvicorn main:app --host 0.0.0.0 --port 8080 --reload