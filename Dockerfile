# Use Python 3.9 image
FROM python:3.8.10

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    libopenblas-dev \
    liblapack-dev \
    gfortran

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the application port
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "fastAPI:app", "--host", "0.0.0.0", "--port", "8000"]
