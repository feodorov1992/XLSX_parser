FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apk add --update --no-cache --virtual .tmp-deps build-base musl-dev linux-headers
RUN python -m venv /py
RUN /py/bin/pip install --upgrade pip
RUN /py/bin/pip install wheel
COPY ./requirements.txt /requirements.txt
RUN /py/bin/pip install -r /requirements.txt
RUN apk del .tmp-deps

COPY ./app /app
WORKDIR /app

RUN adduser --disabled-password --no-create-home app
RUN mkdir -p /vol/web/static
RUN mkdir -p /vol/web/media
RUN chown -R app:app /vol
RUN chmod -R 755 /vol

COPY ./scripts /scripts
RUN chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"
USER app

CMD ["run.sh"]