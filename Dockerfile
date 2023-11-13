FROM python:3

WORKDIR /hw25

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .
