# python app
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install requirements.txt

# Run the Python when container launches
CMD ["python", "app.py"]
