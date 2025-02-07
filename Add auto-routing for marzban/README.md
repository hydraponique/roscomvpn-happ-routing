# Добавление роутинга `RoscomVPN` в Marzban
1. Положите файл `subscription.py` в `/var/lib/marzban/`
2. Прилинкуйте файл строкой `- /var/lib/marzban/subscription.py:/code/app/routers/subscription.py` в конец файла `/opt/marzban/docker-compose.yml`
3. Перезагрузите Marzban командой `marzban restart`
4. Готово! Теперь в приложении Happ, вместе с подписками поставляется - всегда свежий роутинг `RoscomVPN`!
