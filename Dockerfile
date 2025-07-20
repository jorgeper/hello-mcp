# Use Python 3.13 slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Make Python scripts executable
RUN chmod +x *.py

# Expose port for HTTP transport
EXPOSE 8000

# Default command runs the HTTP transport (for testing with curl)
# Override this when running containers for different transports
CMD ["python", "run_http.py"]