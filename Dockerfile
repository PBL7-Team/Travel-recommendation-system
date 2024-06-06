FROM python:3.11-slim

USER root

COPY requirements /requirements

RUN set -ex \
    && RUN_DEPS=" \
    libpcre3 \
    mime-support \
    default-libmysqlclient-dev \
    pkg-config \
    libgl1 \
    libssl-dev\
    gcc\
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y $RUN_DEPS \
    && pip install --no-cache-dir -r /requirements/production.txt \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code/
WORKDIR /code/
ADD backend /code/

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
