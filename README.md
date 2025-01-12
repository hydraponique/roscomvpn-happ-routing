# Кастомный роутинг `RoscomVPN` для приложения [Happ](https://happ.su)

# [Обновляющаяся ссылка на диплинк для Happ](https://github.com/hydraponique/roscomvpn-happ-routing/blob/main/ROUTING_HAPP_DEEPLINK)

## Преимущества:
1) [Кастомный geoip](https://github.com/hydraponique/roscomvpn-geoip) - добавлены все "пророссийские" диапазоны IP (даже забугорные) от VK Company (mail.ru, ok, vk, my.games) и Яндекса (яндекс, я.клауд, я.диск итд). Добавлены IP-адреса Discord (спасибо, @fatyzzz)
2) [Кастомный geosite](https://github.com/hydraponique/roscomvpn-geosite) - куча обновлений по сервисам, урезан максимально под этот роутинг, ни на что более не способен, т.е. чего нет в конфиге роутинга - значит выпилено (весят очень мало по сравнению с дефолтными, тем самым разгружают ядро от фильтрации мусора)

## DNS:
- [AdGuard DNS](https://adguard-dns.io/ru/public-dns.html) 94.140.14.14 с блоком рекламы (разгружаем ядро от тысячи тысяч фильтров рекламы в блок). Утечек ДНС нет, проверено.

## Роутинги:
- все сервера обновлений ОС от Apple, Windows, Android - идут в директ
- все основные банковские приложения РФ (тбанк, ВТБ, сбер, Альфа) - идут в директ и прекрасно работают с включенным ВПН (обновлены списки доменов по информации из парсера по вышеуказанным компаниям)
- все основные сайты заблоченные РКН - идут в прокси
- все ru, by, kz (домены + IP) - идут в директ
- Windows домены для слежки - идут в блок
- Steam, Twitch - идут в директ (убирает растрату сотен гигабайтов трафика VPN)
- Youtube, Discord, TikTok - идут в прокси (обновлены списки доменов этих сервисов + список IP для дискорд)

### В целом: просто быстрый и универсальный конфиг с закрытыми дырками тем, кому не нужно знать об использовании ВПН + адекватный по трафику.
