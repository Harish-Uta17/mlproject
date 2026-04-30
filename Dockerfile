# Use latest stable Python image
FROM python:3.10-slim

WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "application:app"]