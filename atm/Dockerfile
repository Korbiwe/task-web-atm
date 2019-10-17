FROM python:3.7-alpine

COPY requirements.txt /



RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install -r requirements.txt && \
 apk --purge del .build-deps

COPY ./ /src/atm
WORKDIR /src

CMD ["gunicorn", "-c", "atm/gunicorn.conf.py", "atm.wsgi:app"]
