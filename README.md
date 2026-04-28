<div align="center">

# 🚀 NeoTUN Routing

**Готовые конфигурации маршрутизации для [Happ](https://happ.su), [INCY](https://incy.cc) и [Mihomo](https://github.com/MetaCubeX/mihomo)**

> Быстрый и универсальный роутинг: без дыр и утечки вашего сервера, "хирургическая" фильтрация, всё нужное — разблокировано, а ненужное — заблокировано

**Таргет:** 🇷🇺 Россия + 🇧🇾 Беларусь

[![Happ](https://img.shields.io/badge/Happ-blue.svg)](https://happ.su)
[![INCY](https://img.shields.io/badge/INCY-darkgreen.svg)](https://incy.cc)
[![Mihomo](https://img.shields.io/badge/Mihomo-grey.svg)](https://github.com/MetaCubeX/mihomo)

</div>

---

## ⚡ Быстрая установка

Открой ссылку **на телефоне** — приложение установит роутинг автоматически:

| Приложение | Профиль | Ссылка |
|-----------|---------|--------|
| **Happ** | DEFAULT (рекомендуется) | [neotun.ru/routing](https://neotun.ru/routing) |
| **Happ** | Whitelist (только РФ direct) | [neotun.ru/routing/whitelist](https://neotun.ru/routing/whitelist) |
| **Happ** | JSONSUB (минимальный) | [neotun.ru/routing/jsonsub](https://neotun.ru/routing/jsonsub) |
| **INCY** | DEFAULT (рекомендуется) | [neotun.ru/routing/incy](https://neotun.ru/routing/incy) |
| **INCY** | Whitelist | [neotun.ru/routing/incy/whitelist](https://neotun.ru/routing/incy/whitelist) |
| **INCY** | JSONSUB | [neotun.ru/routing/incy/jsonsub](https://neotun.ru/routing/incy/jsonsub) |

> Те же ссылки доступны через `sub.neotunnel.ru/routing`, `sub.neotunnel.ru/routing/incy` и т.д.

---

## 📱 Установка для Happ (файлы)

| Способ | Ссылка | Описание |
|--------|--------|----------|
| **DEFAULT** — полный профиль: RU/BY direct, YouTube/Telegram/GitHub через прокси, реклама блокируется | | |
| 🔗 DEFAULT.DEEPLINK | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/HAPP/DEFAULT.DEEPLINK) | Диплинк-ссылка в текстовом формате |
| 📊 DEFAULT.JSON | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/HAPP/DEFAULT.JSON) | JSON-конфиг роутинга |
| **WHITELIST** — direct только для сервисов и IP из белых списков РФ; всё остальное через прокси | | |
| 🔗 WHITELIST.DEEPLINK | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/HAPP/WHITELIST.DEEPLINK) | Диплинк-ссылка в текстовом формате |
| 📊 WHITELIST.JSON | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/HAPP/WHITELIST.JSON) | JSON-конфиг роутинга |
| **JSONSUB** — минимальный профиль: только DNS + кастомные geoip/geosite, без встроенных правил | | |
| 🔗 JSONSUB.DEEPLINK | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/HAPP/JSONSUB.DEEPLINK) | Диплинк-ссылка в текстовом формате |
| 📊 JSONSUB.JSON | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/HAPP/JSONSUB.JSON) | JSON-конфиг роутинга |

## 📱 Установка для INCY (файлы)

| Способ | Ссылка | Описание |
|--------|--------|----------|
| **DEFAULT** — полный профиль | | |
| 🔗 DEFAULT.DEEPLINK | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/INCY/DEFAULT.DEEPLINK) | Диплинк-ссылка в текстовом формате |
| 📊 DEFAULT.JSON | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/INCY/DEFAULT.JSON) | JSON-конфиг роутинга |
| **WHITELIST** | | |
| 🔗 WHITELIST.DEEPLINK | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/INCY/WHITELIST.DEEPLINK) | Диплинк-ссылка в текстовом формате |
| 📊 WHITELIST.JSON | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/INCY/WHITELIST.JSON) | JSON-конфиг роутинга |
| **JSONSUB** | | |
| 🔗 JSONSUB.DEEPLINK | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/INCY/JSONSUB.DEEPLINK) | Диплинк-ссылка в текстовом формате |
| 📊 JSONSUB.JSON | [Просмотр](https://raw.githubusercontent.com/Kolya-YT/neotun-routing/refs/heads/main/INCY/JSONSUB.JSON) | JSON-конфиг роутинга |

## 💻 Установка для Mihomo (Clash Meta)

Готовые YAML-шаблоны в папке `MIHOMO/`. Подставьте URL вашей подписки и используйте с любым Mihomo-совместимым клиентом.

---

## 🗺 Что роутится в DEFAULT-версии

### 🔴 BLOCK
| Что | Зачем |
|-----|-------|
| 🚫 Домены слежки Windows | Отключаем телеметрию |
| 🚫 BitTorrent DHT | Экономия трафика сервера |
| 🚫 Реклама VK Company | Отключаем рекламу в ВК Видео и ВК Музыке |

### 🟢 DIRECT
| Что | Зачем |
|-----|-------|
| ✅ Русские/белорусские домены и CIDR | За исключением РКН-списков |
| ✅ VK, OK, Mail.Ru, Яндекс, CDNVideo | Казённые сервисы РФ |
| ✅ Apple, Microsoft | Обновления и пуши |
| ✅ Все банки РФ | Корректная работа банковских приложений |
| ✅ Steam, Epic, Riot, EFT | Экономия трафика + проблемы через прокси |
| ✅ Twitch, Pinterest, Faceit | Экономия трафика / фиксы |

### 🔵 PROXY
| Что | Зачем |
|-----|-------|
| 🌐 YouTube | Борьба с ТСПУ и банами РКН |
| 🌐 Telegram | Борьба с ТСПУ и банами РКН |
| 🌐 Google Play | Борьба с ТСПУ и банами РКН |
| 🌐 GitHub | Борьба с ТСПУ и банами РКН |
| 🌐 Весь остальной интернет | Всё зарубежное через прокси |

---

## 🔄 Автообновление

Два GitHub Actions workflow запускаются **каждые 6 часов**:

**`update-configs.yml`** — обновляет `Geoipurl` и `Geositeurl` в JSON-конфигах из апстрим-репозиториев. Не трогает `Name` и правила.

**`sync-upstream-rules.yml`** — синхронизирует `DirectSites`, `ProxySites`, `BlockSites` из оригинального репозитория. Не трогает `Name`, `DnsHosts`, `Geoipurl`, `Geositeurl`.

После каждого обновления deeplink'и регенерируются и nginx-конфиги на сервере обновляются автоматически через SSH.

---

## 🔗 Основано на

- [hydraponique/roscomvpn-routing](https://github.com/hydraponique/roscomvpn-routing) — оригинальный репозиторий
- [roscomvpn-geoip](https://github.com/hydraponique/roscomvpn-geoip) — IP-диапазоны
- [roscomvpn-geosite](https://github.com/hydraponique/roscomvpn-geosite) — доменные списки

<div align="center">

Сделано для пользователей **NeoTUN** 🚀

</div>
