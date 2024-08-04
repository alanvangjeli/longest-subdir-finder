# Longest Subdirectory Finder

This project is a Python application that finds the subdirectory with the longest name within a given directory. It can be run locally or using Docker.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Running Locally](#running-locally)
  - [Running with Docker](#running-with-docker)
- [Next steps](#next-steps)

## Prerequisites

- **Python 3.10 or higher** (for running locally)
- **Docker** (for containerization)

## Getting Started

### Running Locally

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/longest-subdir-finder.git
   cd longest-subdir-finder

2. **Run the script**:
   
    ```sh
    python longest_subdir.py /path/to/directory
    ```

### Running with Docker

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/longest-subdir-finder.git
   cd longest-subdir-finder

2. **Build the Docker image**:
   
    ```sh
    docker build -t longest-subdir-finder .
    ```
    
4. **Run the Docker container**:

    ```sh
    docker run --rm -v /path/to/directory:/mnt/data longest-subdir-finder /mnt/data
    ```
    
    Replace `/path/to/directory` with the path to the directory you want to search. The directory is mounted into the container at `/mnt/data`.


## Next steps:

- Cache Docker layers with cache action
- Include test with the mock directories
