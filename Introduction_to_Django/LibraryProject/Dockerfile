FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install system dependencies for MySQL and build tools
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Command to run the Django development server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]