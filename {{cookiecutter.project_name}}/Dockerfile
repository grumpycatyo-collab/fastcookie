FROM python:{{cookiecutter.python_version}}-slim

WORKDIR /app

# Set environment variables
ENV PYTHONPATH=/app \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install Ruff for linting
RUN pip install --no-cache-dir ruff

# Create logs directory
RUN mkdir -p /app/logs

# Copy project
COPY . /app/

# Run Ruff check before starting the application
RUN ruff check .

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]