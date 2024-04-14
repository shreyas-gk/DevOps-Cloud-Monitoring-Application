FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip install flask-socketio

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0
ENV AWS_DEFAULT_REGION=us-east-1
ENV AWS_ACCESS_KEY_ID="ACCESSKEYHERE"
ENV AWS_SECRET_ACCESS_KEY=""HERE"
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
