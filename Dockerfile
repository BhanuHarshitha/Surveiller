# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port that the app will run on
EXPOSE 8000

# Start the app
CMD python manage.py runserver 0:8000