# Dockerfile - a blueprint for building images
# Image - a template for running containers
# Containers - the running instance of the image

FROM python:3.8

ADD scrape_agoda.py .

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

RUN apt-get -y update

RUN apt-get install -y google-chrome-stable 

RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

RUN apt-get install -yqq unzip

RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN pip install selenium

CMD ["python", "./scrape_agoda.py"]








