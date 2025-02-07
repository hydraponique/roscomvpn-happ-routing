# Добавление роутинга `RoscomVPN` в Marzban
- Положите файл subscription.py в `/var/lib/marzban/`
- Прилинкуйте файл строкой `- /var/lib/marzban/subscription.py:/code/app/routers/subscription.py` в конец файла `/opt/marzban/docker-compose.yml`
- Перезагрузите Marzban - `marzban restart`
- Готово! Теперь в Happ вместе с подписками поставляется всегда свежий роутинг `RoscomVPN`
