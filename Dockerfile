FROM python:3.7-alpine as dev
LABEL version="0.0.1"

RUN apk add --update musl-dev gcc libffi-dev make --no-cache

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY src/ .
COPY VERSION /

FROM dev as prod

EXPOSE 3939
ENTRYPOINT [ "python3",  "server_conf.py" ]
CMD []
