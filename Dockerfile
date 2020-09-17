FROM python:3.7-slim-buster

WORKDIR /workdir

COPY . .

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
RUN apt-get update
RUN apt-get install -y procps

CMD ["python","./source/server.py"]
