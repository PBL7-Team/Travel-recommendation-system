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

#Expose port 8000 để Django server chạy trên nó
EXPOSE 8000

#Chạy Django server khi container được khởi động
# CMD ["python", "manage.py", "runserver_plus", "--cert-file", "cert.pem", "--key-file", "key.pem"]

# Run the application
CMD ["gunicorn", "--chdir", "myproject", "--bind", ":8000", "myproject.wsgi:application"]