FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y git && apt-get clean

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
