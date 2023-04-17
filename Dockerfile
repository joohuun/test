# default 구글 크롬 직접띄우기

# FROM python:3.8.12-slim

# WORKDIR /usr/src

# RUN apt-get -y update && \
#     apt-get install -y wget && \
#     apt-get install unzip && \
#     apt-get install -y curl && \
#     apt-get install -y fonts-nanum* && \
#     apt-get install -y locales locales-all && \ 
#     wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
#     apt-get -y install ./google-chrome-stable_current_amd64.deb && \
#     wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip && \
#     mkdir chrome && \
#     unzip /tmp/chromedriver.zip chromedriver -d /usr/src/chrome

# ENV DISPLAY=:0
# ENV LC_ALL=ko_KR.UTF-8

# COPY requirements.txt ./

# RUN pip install --no-cache-dir -r requirements.txt

# COPY app ./app

# CMD ["google-chrome-stable", "--disable-dev-shm-usage", "--remote-debugging-port=9222", "--user-data-dir=./chrometemp", "--disable-gpu", "--disable-setuid-sandbox", "--no-sandbox"]

FROM python:3.9-slim-buster

# Chrome installation
RUN apt-get update && apt-get install -y wget gnupg unzip curl
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Set display environment variable
ENV DISPLAY=:99

# Install chromedriver
RUN LATEST=`curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget https://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY . .

# Start Xvfb and run Chrome in background
CMD Xvfb $DISPLAY -screen 0 1024x768x16 & \
    pytest app/test/tower/test_account.py
