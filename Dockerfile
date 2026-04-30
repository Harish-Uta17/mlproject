# 1. Use Bookworm to avoid the "404 Not Found" repository errors
FROM python:3.8-slim-bookworm

# 2. Set the working directory
WORKDIR /app

# 3. Copy your project files into the container
COPY . /app

# 4. Install awscli using apt-get (better for scripts)
# We combine update and install, then clean up to keep the image small
RUN apt-get update && apt-get install -y \
    awscli \
    && rm -rf /var/lib/apt/lists/*

# 5. Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Expose the port your app runs on
EXPOSE 8000

# 7. Start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "application:app"]