FROM python:3.11

ADD src/* .

RUN pip install pipenv
RUN pipenv install

CMD ["python", "./app.py"]

EXPOSE 5000 8000
