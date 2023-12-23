# Use an official Python runtime as a base image
FROM python:3.8

# Set environment variables for Python to run in unbuffered mode (recommended for Docker)
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files for dependency installation
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app/

# Expose the port your app will run on (assuming your Django app runs on port 8000 by default)
EXPOSE 8000

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
