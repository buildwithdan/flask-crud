# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /flask-crud

# Install system dependencies for pyodbc and utilities
RUN apt-get update && apt-get install -y \
    g++ \
    unixodbc-dev \
    gnupg \
    unixodbc \
    curl \
    libgssapi-krb5-2 \
    # Import Microsoft GPG key
    && curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc \
    # Configure the Microsoft repository for Debian 11
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    # Update the package lists from repositories
    && apt-get update \
    # Install the latest msodbcsql and mssql-tools
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && ACCEPT_EULA=Y apt-get install -y mssql-tools18

# Configure path for mssql-tools
ENV PATH="/opt/mssql-tools18/bin:${PATH}"

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock ./

# Install dependencies using pipenv
RUN pipenv install --ignore-pipfile

# Copy the rest of the application code into the container
COPY . .

# Expose the port your app runs on
EXPOSE 6010

# Start the application using pipenv to ensure the correct Python environment
CMD ["pipenv", "run", "flask", "--debug", "--app", "api/app.py", "run", "--host=0.0.0.0", "--port=6010"]
