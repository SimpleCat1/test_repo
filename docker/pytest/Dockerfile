FROM python:3.7

ENV PYTHONUNBUFFERED 1

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# устанавливаем зависимости
RUN pip install --upgrade pip
# копируем содержимое текущей папки в контейнер
COPY test_repo test_repo/
# устанавливаем библиотеки для приложения
RUN pip install -r test_repo/requirements.txt
# RUN --network=host
CMD ["pytest"]
# если вдруг тесты не будут работать для selenoid браузеров, то в conftest , там где удаленный браузер указан, добавить поле option и отдать поля, которые выше сделаны
# еще, можно добавить обработчик, что запуск идет через docker или же через что-то другое, если докер, то нужно option Добавить в браузер, если не docker , а через компьютер, то без этих option