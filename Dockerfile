# Python image
FROM python:3.10-slim
# This is just precedent with docker containers? should be the same as it is in docker-run.sh
WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt .
# Install python dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt
# Copy all the rest of the contents into the container
COPY ./python .
# Run main.py
CMD ["python3", "main.py"]