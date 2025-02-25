# Use Python base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies including uvicorn
RUN pip install --no-cache-dir fastapi uvicorn pytest

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
