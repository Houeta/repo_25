FROM python:alpine

WORKDIR /script

RUN pip install mysql-connector-python

COPY . .

CMD [ "python3", "main.py" ]