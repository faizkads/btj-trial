FROM python:3.9-alpine

RUN apk update && apk add build-base libffi-dev
RUN pip3 install ansible

WORKDIR /app
COPY . .

CMD ["python3","./graduation.py"]
