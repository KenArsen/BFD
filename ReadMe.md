# BFD

Заправляйся сейчас, плати потом Без ежемесячной платы!

Мы предлагаем широкий выбор топливных карт для различных видов техники и оборудования.
Подать заявку на карту

## Установка

1. Загрузите скрипт установки Docker:

   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   ```

2. Запустите скрипт установки Docker:

   ```bash
   sudo sh get-docker.sh
   ```

3. Инициализируйте репозиторий Git и настройте удаленный доступ:

   ```bash
   git init
   git config credential.helper '!aws codecommit credential-helper $@'
   git config credential.UseHttpPath true
   экспорт ключей
   git remote add origin <url>
   git pull origin main
   ```

4. Сборка и запуск Docker-контейнеров:

    ```bash
   docker-compose up -d --build
   ```

5. Запустите Docker-контейнеры (на переднем плане):

    ```bash
   docker-compose up
   ```