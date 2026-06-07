# Shadowrocket community adapter

Shadowrocket не умеет напрямую читать RoscomVPN `geoip.dat`, `geosite.dat` и Mihomo `mrs` rule-providers. Этот community-адаптер конвертирует RoscomVPN Routing в совместимые с Shadowrocket `RULE-SET` профили.

## Быстрая установка

Импортируйте профиль в Shadowrocket:

```text
https://raw.githubusercontent.com/lemonchikHere/roscomvpn-shadowrocket/main/roscomvpn-shadowrocket.conf
```

## Что внутри

- `roscomvpn-shadowrocket.conf` — легкий профиль с удаленными `RULE-SET` списками.
- `roscomvpn-shadowrocket-expanded.conf` — expanded-версия без process rules.
- `roscomvpn-shadowrocket-with-process.conf` — expanded-версия с process rules для клиентов, где они поддерживаются.
- `rules/*.list` — Shadowrocket-compatible списки, собранные из RoscomVPN geoip/geosite и дополнительных источников.

## Исходники

Конвертер и generated-конфиги лежат в community repo:

```text
https://github.com/lemonchikHere/roscomvpn-shadowrocket
```

Адаптер сохраняет логику RoscomVPN Routing: российские и белорусские ресурсы идут напрямую, нужные зарубежные сервисы через прокси, рекламные и лишние правила блокируются.
