# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the dependency definition files to leverage Docker cache
COPY pyproject.toml poetry.lock ./

# Install project dependencies (production only, no root package)
RUN poetry install --no-interaction --no-ansi --without dev --no-root --sync

# Copy the rest of the application code
COPY ./app /app/app

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
