# Travel app
## Requirements


This project build a framework that lets organizations can build, organize, manage and sharing their knowledge. It can be used as internal knowledge management either product/support document system.

## 1. Setup
Make sure these software have been installed on your computers:
- [Python](https://www.python.org/downloads/) 3.12 or newer version
- [Node](https://nodejs.org/en/download) 20.9 or newer version
- (Optional) If you are using ubuntu linux, you might have to install mysql client too.
```
    sudo apt-get -y install python-virtualenv mysql-server mysql-client python3 python3-dev python3-pip python-mysqldb libmysqlclient-dev
```
- (Optional) For Mac OSX, make sure you export (run it in your current terminal) these flags before pip install
    ```
        export CFLAGS="-isysroot $(xcrun --show-sdk-path) -I/usr/include -I/usr/local/include/ ${CFLAGS}"
        export LDFLAGS="-isysroot $(xcrun --show-sdk-path) -L/usr/local/lib -L/usr/lib"
        export CPPFLAGS="-isysroot $(xcrun --show-sdk-path) -I/usr/include -L/usr/lib"
    ```
### 1.1. Create python virtual evironment
Follow one of these guide to create python virtual environment corresponding to your operating system.
#### 1.1.1. Linux
```
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate
```

#### 1.1.2. MacOS
```
python3 -m venv .venv
source .venv/bin/activate
```

#### 1.1.3.Windows
```
py -3 -m venv .venv
.venv\scripts\activate
```
### 1.2. Install libraries for backend
After activating the python virtual environment, rung this command to install libraries:
```
pip install -r ./requirements.txt
```

### 1.3. Config
copy [backend/config.env.sample](backend/config.env.sample) to `backend/config.env`. Open this file and change the variables values according to your environment.

### 1.4. Migrate data
```
python ./backend/manage.py migrate
```

### 1.5. Build fronend
From the frontend folder
* Install libraries for frontend
    ```
    npm install
    ```
* Build front end for production:
    ```
    npm run build
    ```
* Or Build front end for development:
    ```
    npm run dev
    ```
### 1.6. Collect static files
Run this command from [backend](backend) directory before you run the backend.
```
python manage.py collectstatic
```
### 1.7. Run backend
Open source code with Visual Studio -> Chose `Run and Debug` on the left panel -> Click `Start Debuging`

## 2. Use docker
If you would like to use docker on your pc. Please following these steps to build and rund docker container locally
- Copy [ci/Dockerfile.template](./ci/Dockerfile.template) to the root folder and remane it to `Dockerfile`
- Copy [ci/docker-compose.yml.local](./ci/docker-compose.yml.local) to the root folder and remane it to `docker-compose.yml`
- Copy [ci/docker-compose.yml.local](./ci/docker.env.template) to the root folder and remane it to `docker.env`. Open this file and change the environment variables as you want
- Build and rund docker conatiner:
    ```
    docker-compose up -d --build
    ```
- Stop docker container:
    ```
    docker-compose down