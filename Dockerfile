# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install pipenv
RUN pip install pipenv

# Install any needed packages specified in Pipfile
RUN pipenv install
# --deploy --ignore-pipfile

EXPOSE 5000 
# the port here doesnt mean anything.

# Run flask when the container launches
CMD ["pipenv", "run", "flask", "--app", "api/app.py", "--debug", "run", "--host=0.0.0.0", "--port=5000"]
# the port down here is important, and this is your container port and not host one. The port for host gets set in the docker compose file.


# build steps
# docker build --platform="linux/amd64" -t flask-crud .
# docker tag flask-crud buildwithdan/flask-crud:latest
# docker push buildwithdan/flask-crud:latest
# docker compose up