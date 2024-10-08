# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the necessary files into the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for Flask or web framework (default 5000 for Flask)
EXPOSE 5000

# Set environment variables (optional for Flask)
ENV FLASK_APP=mederpapp.py
ENV FLASK_ENV=production

# Run the application
CMD ["python", "mederpapp.py"]
