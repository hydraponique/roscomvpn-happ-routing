# Добавление роутинга `RoscomVPN` в Marzban для пользователей JSON-подписок
- Положите файл subscription.py в `/var/lib/marzban/`
- Прилинкуйте файл строкой `- /var/lib/marzban/subscription.py:/code/app/routers/subscription.py` в конец файла `/opt/marzban/docker-compose.yml`
- Перезагрузите Marzban - `marzban restart`
- Готово! Теперь в Happ вместе с подписками поставляется всегда свежие файлы geoip.dat и geosite.dat от `RoscomVPN`
- Теперь в ваш JSON вставляйте любые правила из основного роутинга `RoscomVPN`, посмотреть их можно например в файле RAW.JSON/RAWUNFILTERED.JSON в корне данного репо