# Кастомный роутинг `RoscomVPN` для приложения [Happ](https://happ.su)

# [Обновляющаяся ссылка на диплинк для Happ](https://raw.githubusercontent.com/hydraponique/roscomvpn-happ-routing/refs/heads/main/ROUTING_HAPP_DEEPLINK)

## Преимущества:
1) [Кастомный geoip](https://github.com/hydraponique/roscomvpn-geoip) - добавлены все "пророссийские" диапазоны IP (даже забугорные) от VK Company (MAIL.RU, OK, VK, My.Games) и Яндекса (ya.ru, cloud, disk итд). Добавлены диапазоны и IP-адреса Discord для проксирования (спасибо, [@fatyzzz](https://github.com/fatyzzz/))
2) [Кастомный geosite](https://github.com/hydraponique/roscomvpn-geosite) - куча обновлений по сервисам, урезан максимально под этот роутинг, ни на что более не способен, т.е. чего нет в конфиге роутинга - значит выпилено (весят очень мало по сравнению с дефолтными, тем самым разгружают ядро от фильтрации мусора)

## DNS:
- [AdGuard DNS](https://adguard-dns.io/ru/public-dns.html) 94.140.14.14 с блоком рекламы (разгружаем ядро от тысячи тысяч фильтров рекламы в блок). Утечек ДНС нет, проверено.

## Роутинги:
- все сервера обновлений ОС от Apple, Windows, Android - идут в `DIRECT`
- все основные банковские приложения РФ (Т-Банк, ВТБ, Сбер, Альфа) - идут в `DIRECT` и прекрасно работают с включенным ВПН (обновлены списки доменов по владельцу методом парсинга)
- все основные сайты заблокированные Роскомпозором - идут в `PROXY`
- все существующие русские, белорусские и казахстанские (домены + IP) - идут в `DIRECT` (от греха подальше)
- все домены ОС Windows для слежки за пользователями - идут в `BLOCK`
- Steam, Twitch - идут в `DIRECT` (убирает растрату сотен гигабайтов трафика VPN)
- Youtube, Discord, TikTok - идут в `PROXY` (обновлены списки доменов этих сервисов + список IP для Discord)

### В целом: просто быстрый и универсальный конфиг с закрытыми дырками тем, кому не нужно знать об использовании ВПН + адекватный по трафику.
