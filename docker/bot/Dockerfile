FROM python:3.8.5

WORKDIR /code

ADD . .

RUN pip install pipenv && pipenv install

CMD ["/usr/local/bin/pipenv", "run", "start"]
