
# Здесь обычный проект по автоматизации тестирования UI(кнопочек :) ) на Python


## :rocket: Технологии и инструменты (наведите на картинку курсором, чтобы прочитать название)

<p  align="center"><code><img width="5%" title="Python" src="images/python-logo.svg"></code>
<code><img width="5%" title="Docker" src="images/docker-logo.svg"></code>
<code><img width="5%" title="Allure" src="images/allure-logo.svg"></code>
<code><img width="5%" title="Git" src="images/picture_git-logo.svg"></code>
<code><img width="5%" title="PyCharm" src="images/PyCharm-logo.svg"></code>
<code><img width="5%" title="Selenium" src="images/selenium-logo.svg"></code>
<code><img width="5%" title="Selenoid" src="images/picture_selenoid-logo.svg"></code>
<code><img width="5%" title="Pytest" src="images/Pytest_logo.svg"></code></p>
Кратко опишу ,что в проекте реализовано: 

Код написан на `Python` в нем использовался,
`Faker`, чтобы генерировать рандомные данные для тестов, а не одни и те же
.`config.py` , находятся ссылки на данные, которые скрываем
.`Allure`, для генерации отчетов
.`Docker`- инструмент, чтобы запускать всю сборку локально без сохранения установленных окружений на личном компьютере.
.В проекте используется фреймворк `Pytest`, `Selenium`, для UI тестов. Тесты запускаются через `Pytest`. Тесты могут запускаться удаленно, через `Selenoid`,в котором используется контейнеры `Docker` для запуска браузеров, так и локально (на вашем компьютере) можно запустить (если у вас установлены драйвера для браузеров).
## :spiral_notepad: Реализованы проверки

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UI

> - [x] *Проверка страницы авторизации*
>- [x] *Проверка хлебных крошек у товара*
>- [x] *Имя вкладки браузера главной страницы*
>- [x] *Авторизация нового пользователя*
>- [x] *Изменение валюты товаров*
>- [x] *Удаление, добавление товара в корзину*
>- [x] *Просмотр карточки товара*


## :computer: Запуск тестов из терминала

Скачиваем этот репозиторий и переходим через 'CMD' в test_repo, эта папка в скаченном репозитории.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:green_circle:&nbsp;&nbsp;*Запуск тестов локально, с вашего компьютера, при условии, что у вас установлены окружения(драйверы для браузера). Если не установлены, то используйте Selenoid*

И тесты запустятся, через ваш браузер

Простой запуск(запуск будет локальный на вашем браузере chrome)
```bash
pytest tests
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:green_circle:&nbsp;&nbsp;*Запуск тестов в несколько потоков:*

В два потока
```bash
pytest --url=http://192.168.0.102:8081 --browser=chrome --remote=False -n 2 tests
```


В один поток
```bash
pytest --url=http://192.168.0.102:8081 --browser=chrome --remote=False tests
```


Больше двух потоков делать нет смысла, тут у меня несколько параллельных тестов, остальные не параллельные

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:green_circle:&nbsp;&nbsp;*Запуск в разных браузерах:*

Если нужно запустить в другом браузере, то указываем так
```bash
pytest --url=http://192.168.0.102:8081 --browser=firefox --remote=False tests
```
или
```bash
pytest --url=http://192.168.0.102:8081 --browser=opera --remote=False tests
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:green_circle:&nbsp;&nbsp;*Запуск на Selenoid:*

```bash
pytest --url=http://192.168.0.102:8081 --browser=chrome --remote=True --command_executor=http://192.168.0.102:4444/wd/hub --browser_version=80  tests
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:green_circle:&nbsp;&nbsp;*Запуск тестов c подготовкой отчета Allure:*

```bash
pytest --url=http://192.168.0.102:8081 --browser=firefox --remote=False --alluredir=allure-results  tests
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:green_circle:&nbsp;&nbsp;*Сформировать allure отчет после проейденных тестов:*

```bash
allure serve  allure-results
```

где:
>- [x] *browser - браузер, в котором будут выполняться тесты (по умолчанию chrome), и по умолчанию последняя версия браузера на вашем же компьютере. По коду поддерживается только: chrome, firefox, opera*
>- [x] *browser_version - указывает версию браузера*
>- [x] *command_executor - url, где будут запускаться браузеры через selenoid*
>- [x] *remote - указывает коду тестов, когда нужно запускать на удаленном барузера (при True) или не запускать (при False)*
>- [x] *url - указываем url, где находится opencart(сайт, который тетируем)*
>- [x] *alluredir - папка, куда будут загружаться файлы для отчета Allure*

## Opencart
1. Узнаем наш Ip в поле IPv4-адрес в таблице с информацией о сети, к которой подключен ваш компьютер. Запоминаем его
```bash
ipconfig
``` 
2. Сейчас мы внутри папки test_repo `%USERPROFILE%\Documents\hd\4\test_repo`
3. Запускаем программу `Docker` (если запущена, то пропускаем)
4. заходим в папку 
```bash 
cd docker/opencart
```
5. Создаем образ Jenkins
```bash 
docker compose up
```
6. заходим в браузере по http://ваш_Url_из_шага_0:8081 и вот наш selenoid

Если вдруг не зашло, то нужно будет пересобрать образ(удалив старый).Заходим в файл docker/opencart/docker-compose.yml на строке 30 , там где OPENCART_HOST проставьте Url из шага 0, порт не изменяйте. Повторите шаги выше


## <img width="4%" title="Jenkins" src="images/picture_jenkins-logo.svg"> Запуск тестов в Jenkins


### Запускаем jenkins
0. Узнаем наш Ip в поле IPv4-адрес в таблице с информацией о сети, к которой подключен ваш компьютер. Запоминаем его
```bash
ipconfig
``` 
1. Сейчас мы внутри папки test_repo `%USERPROFILE%\Documents\hd\4\test_repo`
2. Запускаем программу `Docker` (если запущена, то пропускаем)
3. заходим в папку 
```bash 
cd docker/jenknins
```
4. Создаем образ Jenkins
```bash 
docker build -t myjenkins .
```
5. Запускаем Jenkins на нашем url на порту 8080
```bash
docker run --name jenkins --restart=on-failure --detach ^
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 ^
    --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 ^
      --volume jenkins-data:/var/jenkins_home ^
        --volume jenkins-docker-certs:/certs/client:ro ^
          --publish 8080:8080 --publish 50000:50000 myjenkins
```
6. заходим в браузере по http://ваш_Url_из_шага_0:8080 и вот наш jenkins
7. 8785767d90e84de89cfd6880aea7a1ba берется так, в cmd вводим команду `docker images --all` потом ищем в таблие myjenkins и копируем его id и вводим его в эту команду `docker logs id_myjenkins_который_увидели` и тут в консоли увидим строчку одну, которая будет выглядеть как этот код 8785767d90e84de89cfd6880aea7a1ba ( у вас может быть другим, это нормально)
8. вводим пароль из шага 7
9. устанавливаем плагины по умолчанию, ничего не меняем(логин и пароль) и просто нажимаем далее 
(нажимаем установку по умолчанию
нажимаем Skip and continue as admin 
нажимаем Save and Finish
нажимаем Start using Jenkins)
10. нажимаем "Настроить Jenkins"->"Jenkins CLI"-> нажимаем на jenkins-cli.jar
11. И сейчас подготовим job-у в jenkins
8785767d90e84de89cfd6880aea7a1ba берется так, в cmd вводим команду `docker images --all` потом ищем в таблие myjenkins и копируем его id и вводим его в эту команду `docker logs id_myjenkins_который_увидели` и тут в консоли увидим строчку одну, которая будет выглядеть как этот код 8785767d90e84de89cfd6880aea7a1ba ( у вас может быть другим, это нормально)
admin - логин jenkins по умолчанию
192.168.0.102 - ip, из шага 0
8080 - порт, из шага 5
```bash 
java -jar C:\Users\Y\Downloads\jenkins-cli.jar -s http://admin:8785767d90e84de89cfd6880aea7a1ba@192.168.0.102:8080 create-job pytest < pytest.xml
```
12. нажимаем Настроть Jenkins->Управление плагинами->Available plugins-> в input вводим allure ->в списке появится наш allure, ставим галочку на нем и устанавливаем с перезагрузкой
13. нажимаем "Настроить Jenkins"->нажать "Global Tool Configuration."->снизу у "Allure Commandline" в Имя пишем Allure-> Галочку "Установить автоматически" оставляем, то что указано в maven оставляем
14. Готово. Теперь на главной странице нажимаем на нашу job-у, и запускаем с параметрами

### :pushpin: Параметры сборки

    browser - браузер, в котором будут выполняться тесты (по умолчанию chrome), и по умолчанию последняя версия браузера на вашем же компьютере. По коду поддерживается только: chrome, firefox, opera
    browser_version - указывает версию браузера
    command_executor - url, где будут запускаться браузеры через selenoid
    remote_start - указывает коду тестов, когда нужно запускать на удаленном барузера (при True) или не запускать (при False)
    url_test_project - указываем url, где находится opencart(сайт, который тетируем)
    parallel - параллельный запуск тестов, =1 то один поток, =2 многопточный запуск тестов

*Для запуска сборки необходимо указать значения параметров(там где выпадающий список есть, там и меняем) и нажать кнопку <code><strong>*Собрать*</strong></code>*, если выбрали, что нужно.

<p align="center">
  <img src="images/jenkins_job.jpg" alt="job" width="800">
</p>

*После выполнения сборки, в блоке <code><strong>*История сборок*</strong></code>, напротив номера сборки, появится
значок <img width="2%" title="Allure Report" src="images/picture_allure-Report-logo.svg"><code><strong>*Allure
Report*</strong></code>, кликнув по которому, откроется страница с сформированным html-отчетом.*
<p align="center">
  <img src="images/allure_result.jpg" alt="job" width="800">
</p>

## <img width="4%" title="Allure Report" src="images/allure-logo.svg"> Отчет о результатах тестирования в Allure Report

### :pushpin: Общая информация

*Главная страница Allure отчета, содержит следующие информационные блоки:*

>- [x] <code><strong>*ALLURE REPORT*</strong></code> - отображает дату и время прохождения теста, общее количество пройденных кейсов, а также диаграмму с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
>- [x] <code><strong>*TREND*</strong></code> - отображает тренд прохождения тестов от сборки к сборке
>- [x] <code><strong>*SUITES*</strong></code> - отображает распределение результатов тестов по тестовым наборам
>- [x] <code><strong>*ENVIRONMENT*</strong></code> - отображает тестовое окружение, на котором запускались тесты (в данном случае информация не задана)
>- [x] <code><strong>*CATEGORIES*</strong></code> - отображает распределение неуспешно прошедших тестов по видам дефектов
>- [x] <code><strong>*FEATURES BY STORIES*</strong></code> - отображает распределение тестов по функционалу, который они проверяют
>- [x] <code><strong>*EXECUTORS*</strong></code> - отображает исполнителя текущей сборки (ссылка на сборку в Jenkins)

<p align="center">
  <img src="images/allure_report_title.jpg" alt="Allure Report" width="900">
</p>

### :pushpin: Список тестов c описанием шагов и визуализацией результатов

*На данной странице представляется стандартное распределение выполнявшихся тестов по тестовым наборам или классам, в
которых находятся тестовые методы.*

<p align="center">
  <img src="images/allure_result.jpg" alt="Allure Report" width="900">
</p>


## <img width="4%" title="Selenoid" src="images/picture_selenoid-logo.svg"> Пример запуска теста в Selenoid
1. Узнаем наш Ip в поле IPv4-адрес в таблице с информацией о сети, к которой подключен ваш компьютер. Запоминаем его
```bash
ipconfig
``` 
2. Сейчас мы внутри папки test_repo `%USERPROFILE%\Documents\hd\4\test_repo`
3. Запускаем программу `Docker` (если запущена, то пропускаем)
4. заходим в папку 
```bash 
cd docker/selenoid
```
5. Создаем образ Jenkins
```bash 
docker compose up
```
6. Подгружаем браузеры chrome( можно и firefox, opera, там только имя поменять в названии, вместо chrome поставить firefox)
```bash 
docker pull selenoid/chrome:80.0
```
```bash 
docker pull selenoid/chrome:81.0
```
```bash 
docker pull selenoid/vnc:chrome_80.0
```
```bash 
docker pull selenoid/vnc:chrome_81.0
```
7. заходим в браузере по http://ваш_Url_из_шага_0:8082 и вот наш selenoid
<p align="center">
  <img src="images/selenoid_chrome.jpg" alt="video" width="1000">
</p>

## Запуск тестов внтури dockerfile
1. Сейчас мы внутри папки test_repo `%USERPROFILE%\Documents\hd\4\test_repo`
3. Запускаем программу `Docker` (если запущена, то пропускаем)
4. копируем файл, в cmd вводим команду. Так мы Dockerfile переместим выше test_repo и файл будет на одном уровне с папкой test_repo
```bash 
copy test_repo\docker\pytest\Dockerfile ..\
```
5. Создаем образ pytest с нашими тестами
```bash 
cd ..
```
```bash 
docker build -t tests .
```
6. запускаем тесты так
`docker images --all` и находим id нашего образа tests и ниже же, этот в id используем. Также в команде можно использовать параметры, что описаны выше , такие как --url и т.д.
```bash
docker run 3e016f8539e0 pytest test_repo/tests
```

Тесты запустятся внутри контейнера, там не будет allure, и там будет работать только chrome, потому что нужно подгружать другие браузеры с драйверами, но оставил один браузер
