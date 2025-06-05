# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy dependency definition files, Alembic configuration, and Alembic scripts
COPY pyproject.toml poetry.lock ./
COPY alembic.ini ./
COPY alembic ./alembic/

# Install project dependencies (production only, no root package)
# This should be run AFTER copying alembic files if env.py imports from app.models
# (which it likely does to get the metadata target for Alembic)
# For now, let's keep it here. If Alembic setup in env.py fails due to missing app code,
# we might need to adjust the order of COPY ./app and RUN poetry install.
RUN poetry install --no-interaction --no-ansi --without dev --no-root --sync

# Copy the rest of the application code from your local 'app' directory
# (which contains main.py, models/, services/, etc.)
# into a subfolder 'app' inside the WORKDIR /app (i.e., to /app/app)
COPY ./app /app/app

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["/root/.local/bin/poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]