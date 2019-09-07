FROM python:3.7-alpine

WORKDIR /src

VOLUME /src/log
VOLUME /src/media
VOLUME /src/assets

EXPOSE 8000

COPY . .

RUN cp ./script/docker-entrypoint.sh /usr/local/bin/entrypoint && \
    chmod +x /usr/local/bin/entrypoint && \
    \
    apk add --update --no-cache --virtual build-deps \
        build-base linux-headers libc-dev \
        pcre-dev && \
    apk add --no-cache \
        libuuid pcre mailcap \
        musl-dev libxslt-dev libffi-dev \
        jpeg-dev zlib-dev postgresql-dev && \
    \
    pip3 install --no-cache-dir pipenv uwsgi && \
    pipenv install --system --deploy --ignore-pipfile && \
    \
    apk del build-deps

ENTRYPOINT [ "entrypoint" ]

CMD [ "uwsgi", "--ini", "./deploy/uwsgi.ini" ]
