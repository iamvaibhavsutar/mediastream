FROM python:3.9

# Install required system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    python3-dev \
    python3-pip \
    python3-venv \
    libcurl4-openssl-dev \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    pkg-config \
    cmake \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]

