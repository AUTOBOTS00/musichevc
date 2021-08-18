FROM python:3.9-slim-buster
WORKDIR /app
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 main.py
