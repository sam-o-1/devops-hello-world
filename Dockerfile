# Use Python 3.9 as the base OS
FROM python:3.9-slim

# Set the working folder inside the container
WORKDIR /app

# Copy requirements first (for speed)
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code into the container
COPY . .

# Tell Docker we want to use port 5000
EXPOSE 5000

# The command that starts the app
CMD ["python", "app.py"]
