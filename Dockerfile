# Use the official Ubuntu image as the base image
FROM ubuntu:22.04

# Set environment variables to reduce unnecessary prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PATH="/root/.local/bin:$PATH"

# Set the working directory in the container
WORKDIR /flask-crud

# Install Python and necessary tools
RUN apt-get update && apt-get install -y \
    python3.12 \
    python3-pip \
    python3.12-dev \
    g++ \
    unixodbc-dev \
    gnupg \
    unixodbc \
    curl \
    libgssapi-krb5-2 \
    apt-transport-https \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Update python3 and pip3 to point to the newly installed Python 3.12
RUN ln -sf /usr/bin/python3.12 /usr/bin/python3 \
    && ln -sf /usr/bin/python3.12 /usr/bin/python \
    && ln -sf /usr/bin/pip3 /usr/bin/pip

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Import the Microsoft repository GPG keys
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Register the Microsoft SQL Server Ubuntu repository
RUN curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Update package lists
RUN apt-get update

# Install SQL Server drivers and tools
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18 mssql-tools18

# Configure path for mssql-tools
ENV PATH="/opt/mssql-tools18/bin:${PATH}"

# Copy Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock ./

# Install dependencies using pipenv, specifying Python version
RUN pipenv install --ignore-pipfile --deploy --python /usr/bin/python

# Copy the rest of the application code into the container
COPY . .

# Expose the port your app runs on
EXPOSE 6010

# Start the application using pipenv to ensure the correct Python environment
CMD ["pipenv", "run", "flask", "--debug", "--app", "api/app.py", "run", "--host=0.0.0.0", "--port=6010"]
