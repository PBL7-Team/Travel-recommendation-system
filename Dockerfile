FROM node:20-alpine AS builder

USER root

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY frontend ./

# clear the old dependencies
RUN rm -rf node_modules package-lock.json 

# build vue frontend
RUN npm install \
    && npm run build \
    && mv /app/dist/static/* /app/dist/ \
    && cp -r /app/public/* /app/dist/ \
    && rm -rf /app/dist/static


FROM python:3.11-slim

# Copy in your requirements file
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

# Copy requirements.txt vào image và cài đặt dependencies
# ADD requirements/base.txt /requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy toàn bộ mã nguồn của Django vào image
# COPY backend /app/
# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir /code/
WORKDIR /code/
ADD backend /code/


# Chạy các lệnh migrate và collectstatic
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

#Expose port 8000 để Django server chạy trên nó
EXPOSE 8080

#Chạy Django server khi container được khởi động
CMD ["python", "manage.py", "runserver"]