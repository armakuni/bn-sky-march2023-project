FROM python:3.11

ADD src/* ./
ADD Pipfile* ./

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "./app.py"]

EXPOSE 5000 8000
