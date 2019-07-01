FROM python:3.5.6-slim-stretch

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

WORKDIR /app/client

ENV FLASK_APP=main.py

CMD ["flask", "run", "--host=0.0.0.0"]
