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

## 📱 Установка для Happ

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

## 📱 Установка для INCY

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

Два GitHub Actions workflow:

**`update-configs.yml`** — запускается каждые 6 часов:
- Проверяет новые теги в [roscomvpn-geoip](https://github.com/hydraponique/roscomvpn-geoip) и [roscomvpn-geosite](https://github.com/hydraponique/roscomvpn-geosite)
- Обновляет `Geoipurl` и `Geositeurl` в JSON-конфигах
- Регенерирует диплинки
- **Не трогает** `Name`, `DnsHosts` и правила роутинга

**`sync-upstream-rules.yml`** — запускается каждый понедельник (или вручную):
- Синхронизирует `DirectSites`, `ProxySites`, `BlockSites` и IP-списки из оригинального репозитория
- **Не трогает** `Name`, `DnsHosts`, `Geoipurl`, `Geositeurl` — они остаются твоими

> Если хочешь изменить правила роутинга под себя — редактируй JSON-файлы напрямую. При следующей синхронизации правила обновятся из апстрима. Чтобы заблокировать синхронизацию конкретного файла — удали его из списка `git add` в workflow.

---

## 🔗 Основано на

- [hydraponique/roscomvpn-routing](https://github.com/hydraponique/roscomvpn-routing) — оригинальный репозиторий
- [roscomvpn-geoip](https://github.com/hydraponique/roscomvpn-geoip) — IP-диапазоны
- [roscomvpn-geosite](https://github.com/hydraponique/roscomvpn-geosite) — доменные списки

<div align="center">

Сделано для пользователей **NeoTUN** 🚀

</div>
