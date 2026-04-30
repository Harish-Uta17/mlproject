# Using Bookworm fixes the 404 repository issues
FROM python:3.8-slim-bookworm

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install system dependencies (including awscli)
# Combining commands and cleaning the cache keeps the image size down
RUN apt-get update && apt-get install -y \
    awscli \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Inform Docker that the container listens on the specified network port at runtime
EXPOSE 8000

# Run the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "application:app"]