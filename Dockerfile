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
    \
    apk add --no-cache \
        libuuid pcre mailcap \
        musl-dev libxslt-dev libffi-dev \
        jpeg-dev zlib-dev postgresql-dev \
        logrotate && \
    \
    cp ./deploy/django.logrotate.conf /etc/logrotate.d/django && \
    echo -e "#\!bin/sh\nlogrotate -f /etc/logrotate.d/django" > /etc/periodic/daily/django-logrotate && \
    chmod +x /etc/periodic/daily/django-logrotate && \
    [[ -d ./log/archived ]] || mkdir -p ./log/archived && \
    crond && \
    \
    pip3 install --no-cache-dir pipenv uwsgi && \
    pipenv install --system --deploy --ignore-pipfile -v && \
    \
    apk del build-deps && \
    rm -rf ~/.cache

ENTRYPOINT [ "entrypoint" ]

CMD [ "uwsgi", "--ini", "./deploy/uwsgi.ini" ]
