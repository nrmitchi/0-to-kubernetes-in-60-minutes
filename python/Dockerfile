# Use Python 2.7.13-slim image as our base
from python:2.7.13-slim

# Add our requirements file.
# We add this separately so that everytime we change our code and rebuild,
# we do not have to rebuild all of our dependecies as well.
COPY requirements.txt .

# Install the dependencies from our requirements file into our image
RUN pip install -r requirements.txt

# Copy the rest of our application in
COPY . .

# Set the environment variable used by the `flask` command
ENV FLASK_APP=hello.py

# Export port 5000 (used by the `flask` command)
EXPOSE 5000

# Set the default command run when the container is started
#  We have to listen on all interfaces, or else the app will not be accessible
#  outside of the container.
CMD flask run --host=0.0.0.0

