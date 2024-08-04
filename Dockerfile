FROM python:3.10-slim

WORKDIR /app

# Copy the longest_subdir.py script into the container at /app
COPY . /app

# Normally, we would install the dependencies here, but since the script only uses the standard libraries we don't need to install anything

# Run longest_subdir.py when the container launches
ENTRYPOINT ["python", "longest_subdir.py"]
