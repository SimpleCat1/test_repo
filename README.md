Используя docker, docker-compose(для win идет в паре с docker) на своем компьютере развернуть приложение opencart.


Конфигурационный файл для запуска: Docker-compose opencart + phpmyadmin (github.com). https://gist.github.com/konflic/ecd93a4bf7666d97d62bcecbe2713e55

В качестве ответа приложить скриншот с url приложения, и вывод графического приложения с запущенным контейнером, либо скриншот терминала с работающими образами.

Полезные команды(использовались по ubuntu, но думаю на других ос семейств linux, или win должны работать):
docker-compose up -d - запустить сборку приложения
docker-ps - посмотреть запущенные контейнеры
docker-compose down - потушить.
docker images - показать все образы
docker system prune -a - удалить все образы
docker volume prune - очистить кеш(используется после prune для полной чистки содержимого)
jenkins
запускаем docker
docker logs наш_docker_container_jenkins
и копируем так ключ
переходим по http://192.168.0.102:8080
вводим ключ
нажимаем установку по умолчанию
нажимаем Skip and continue as admin 
нажимаем Save and Finish
нажимаем Start using Jenkins
нажимаем Настроть Jenkins->Управление плагинами->Available plugins
устанавливаем allure и 

Послесборочные операции выбрали allure, то там выскоичит ошибка , где нужно нажать Global Tool Configuration.
и там снизу у Allure Commandline в Имя пишем Allure
 Галочку "Установить автоматически" оставляем то что указано в maven и сохраняем

http://192.168.0.102:8080/manage/cli/ нажимаем на jenkins-cli.jar

java -jar C:\Users\Y\Downloads\jenkins-cli.jar -s http://admin:8785767d90e84de89cfd6880aea7a1ba@192.168.0.102:8080 get-job pytest > pytest.xml
java -jar C:\Users\Y\Downloads\jenkins-cli.jar -s http://admin:8785767d90e84de89cfd6880aea7a1ba@192.168.0.102:8080 create-job pytest < pytest.xml



