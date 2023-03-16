# start by pulling the python image
FROM python:3.11-alpine

# copy every content from the local file to the image
COPY src/* ./
COPY requirements.txt ./

# install the dependencies and packages in the requirements file
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# run flask app
CMD ["python", "./app.py"]

# Expose ports
EXPOSE 8000