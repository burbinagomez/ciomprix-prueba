FROM python

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./requirements.txt .
RUN apt-get update \
    && apt-get -y install libpq-dev python-dev

RUN pip install -r requirements.txt

COPY . .


