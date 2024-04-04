#!/bin/bash

set -e

ROOT_DIR=$(git rev-parse --show-toplevel)
BACKEND_DIR=${ROOT_DIR}/backend
FRONTEND_DIR=${ROOT_DIR}/frontend
cd ${ROOT_DIR}

# Copy or download scret files
# scp -i ${SSH_KEY} ${SERVER_SSH}:${CLIENT_SECRET_FILE} ${BACKEND_DIR}/api/credentials.json

# For docker
echo preprocess docker environment variables
cp -f ${ROOT_DIR}/ci/docker.env.template ${ROOT_DIR}/docker.env
find ${ROOT_DIR}/docker.env -type f -name "*" | xargs sed -i '' s/DJANGO_SETTINGS_MODULE=/DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}/g
find ${ROOT_DIR}/docker.env -type f -name "*" | xargs sed -i '' s/DB_HOST=/DB_HOST=${DB_HOST}/g
find ${ROOT_DIR}/docker.env -type f -name "*" | xargs sed -i '' s/DB_PORT=/DB_PORT=${DB_PORT}/g
find ${ROOT_DIR}/docker.env -type f -name "*" | xargs sed -i '' s/DB_USER=/DB_USER=${DB_USER}/g
find ${ROOT_DIR}/docker.env -type f -name "*" | xargs sed -i '' s/DB_PASSWORD=/DB_PASSWORD=${DB_PASSWORD}/g
find ${ROOT_DIR}/docker.env -type f -name "*" | xargs sed -i '' s/DB_NAME=/DB_NAME=${DB_NAME}/g

echo preprocess docker compose files
cp -f ${ROOT_DIR}/ci/docker-compose.yml.template ${ROOT_DIR}/docker-compose.yml
echo ${ROOT_DIR}/docker-compose.yml
find ${ROOT_DIR}/docker-compose.yml -type f -name "*" | xargs sed -i '' s/__WEB_PORT__/${WEB_PORT}/g

echo preprocess docker file
cp -f ${ROOT_DIR}/ci/Dockerfile.template ${ROOT_DIR}/Dockerfile

# Backend config
cp -f ${BACKEND_DIR}/config.env.template ${BACKEND_DIR}/config.env
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/APP_NAME=/APP_NAME=${APP_NAME}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/SECRET_KEY=/SECRET_KEY=${SECRET_KEY}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/DEBUG=/DEBUG=${DEBUG}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/API_HOST=/API_HOST=${API_HOST}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/CORS_ALLOW_ALL_ORIGINS=/CORS_ALLOW_ALL_ORIGINS=${CORS_ALLOW_ALL_ORIGINS}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s%CORS_ALLOWED_ORIGINS=%CORS_ALLOWED_ORIGINS=${CORS_ALLOWED_ORIGINS}%g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/DJANGO_ALLOWED_HOSTS=/DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/USE_X_FORWARDED_HOST=/USE_X_FORWARDED_HOST=${USE_X_FORWARDED_HOST}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/PRIVATE_KEY_FILE=/PRIVATE_KEY_FILE=${PRIVATE_KEY_FILE}/g
# Database
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/DB_HOST=/DB_HOST=${DB_HOST}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/DB_PORT=/DB_PORT=${DB_PORT}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/DB_USER=/DB_USER=${DB_USER}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/DB_PASSWORD=/DB_PASSWORD=${DB_PASSWORD}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/DB_NAME=/DB_NAME=${DB_NAME}/g
# Default accounts
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/DEFAULT_CLIENT_ID=/DEFAULT_CLIENT_ID=${DEFAULT_CLIENT_ID}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/DEFAULT_CLIENT_SECRET=/DEFAULT_CLIENT_SECRET=${DEFAULT_CLIENT_SECRET}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/SUPER_ADMIN_EMAIL=/SUPER_ADMIN_EMAIL=${SUPER_ADMIN_EMAIL}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/SUPER_ADMIN_PASSWORD=/SUPER_ADMIN_PASSWORD=${SUPER_ADMIN_PASSWORD}/g
# Email
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/EMAIL_HOST=/EMAIL_HOST=${EMAIL_HOST}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/EMAIL_HOST_USER=\'\'/EMAIL_HOST_USER=\'${EMAIL_HOST_USER}\'/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/EMAIL_HOST_PASSWORD=\'\'/EMAIL_HOST_PASSWORD=\'${EMAIL_HOST_PASSWORD}\'/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s%BLOCKED_EMAIL_DOMAINS=%BLOCKED_EMAIL_DOMAINS=${BLOCKED_EMAIL_DOMAINS}%g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/DEFAULT_FROM_EMAIL=/DEFAULT_FROM_EMAIL=${DEFAULT_FROM_EMAIL}/g
# API documents
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/ALLOWED_SWAGGER=/ALLOWED_SWAGGER=${ALLOWED_SWAGGER}/g
# AWS
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/AWS_ACCESS_KEY_ID=/AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/AWS_SECRET_ACCESS_KEY=/AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/STORE_USER_FILES_ON_S3=/STORE_USER_FILES_ON_S3=${STORE_USER_FILES_ON_S3}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/AWS_STORAGE_BUCKET_NAME=/AWS_STORAGE_BUCKET_NAME=${AWS_STORAGE_BUCKET_NAME}/g
find ${BACKEND_DIR}/config.env -type f -name "*" | xargs sed -i '' s/AWS_S3_REGION_NAME=/AWS_S3_REGION_NAME=${AWS_S3_REGION_NAME}/g

# Front end
cp -f ${FRONTEND_DIR}/env.template ${FRONTEND_DIR}/.env
find ${FRONTEND_DIR}/.env -type f -name "*" | xargs sed -i '' s%VUE_APP_BASE_URL=%VUE_APP_BASE_URL=${BASE_URL}%g
find ${FRONTEND_DIR}/.env -type f -name "*" | xargs sed -i '' s%VUE_APP_API_URL=%VUE_APP_API_URL=${API_URL}%g
find ${FRONTEND_DIR}/.env -type f -name "*" | xargs sed -i '' s%VUE_APP_BLOCKED_EMAIL_DOMAINS=%VUE_APP_BLOCKED_EMAIL_DOMAINS=${BLOCKED_EMAIL_DOMAINS}%g
find ${FRONTEND_DIR}/.env -type f -name "*" | xargs sed -i '' s/VUE_APP_CACHE_PERIOD=/VUE_APP_CACHE_PERIOD=${CACHE_PERIOD}/g
find ${FRONTEND_DIR}/.env -type f -name "*" | xargs sed -i '' s/VUE_APP_SIMILAR_THRESHOLD=/VUE_APP_SIMILAR_THRESHOLD=${SIMILAR_THRESHOLD}/g
find ${FRONTEND_DIR}/.env -type f -name "*" | xargs sed -i '' s/VUE_APP_SIMILAR_THRESHOLD_HIGH=/VUE_APP_SIMILAR_THRESHOLD_HIGH=${SIMILAR_THRESHOLD_HIGH}/g

# Create file pub/pri KEY
cd $BACKEND_DIR
file="${BACKEND_DIR}/${PRIVATE_KEY_FILE}"
echo $file
if [ -f "$file" ]
then
	echo "File ${file}.key is already exists"
else
	openssl genrsa -out "${file}" 4096
	openssl rsa -in "${file}" -pubout > "${file}.pub"
	chmod 777 "${file}"
fi

echo "Done."
