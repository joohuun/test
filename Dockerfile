
FROM python:3.8.12-slim

WORKDIR /usr/src

RUN apt-get -y update && \
    apt-get install -y wget && \
    apt-get install unzip && \
    apt-get install -y curl && \
    apt-get install -y fonts-nanum* && \
    apt-get install -y locales locales-all && \ 
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get -y install ./google-chrome-stable_current_amd64.deb && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip && \
    mkdir chrome && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/src/chrome

ENV DISPLAY=:0
ENV LC_ALL=ko_KR.UTF-8

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get -y install vim

COPY app ./app

CMD ["google-chrome-stable", "--disable-dev-shm-usage", "--remote-debugging-port=9222", "--user-data-dir=./chrometemp", "--disable-gpu", "--disable-setuid-sandbox", "--no-sandbox"]