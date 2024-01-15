# Use the official Python image as a base image
FROM public.ecr.aws/docker/library/python:3.10
#FROM python:3.10
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install project dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose port 8000 for the Django application
EXPOSE 8000

COPY commands.sh /app/
RUN chmod +x /app/commands.sh

COPY . .

# Run the Django application
CMD ["/app/commands.sh"]
