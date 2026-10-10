# Иллюстрации «Крути и говори!»

Все 22 изображения созданы специально для проекта из оригинальных геометрических векторных рисунков. Внешние изображения, emoji, CDN и готовые стоки не использованы. Источник — `assets-source.py`; экспорт выполнен CairoSVG 2.9.1. Исходные описания — предоставленное ТЗ.

Карточки — PNG RGBA 1024×1024 с настоящей прозрачностью; фоны — непрозрачные PNG 1920×1080. Иллюстрации готовы и включены в игру. Узнаваемость действий взрослым/детьми пока не подтверждена; галерея для просмотра находится в настройках взрослого.

| Файл | Размер | Статус |
|---|---|---|
| `assets/actions/action-break.png` | 1024×1024 | Создан, включён |
| `assets/actions/action-catch.png` | 1024×1024 | Создан, включён |
| `assets/actions/action-push.png` | 1024×1024 | Создан, включён |
| `assets/actions/action-put-to-bed.png` | 1024×1024 | Создан, включён |
| `assets/actions/action-stroke.png` | 1024×1024 | Создан, включён |
| `assets/backgrounds/cover-background.png` | 1920×1080 | Создан, включён |
| `assets/backgrounds/game-background.png` | 1920×1080 | Создан, включён |
| `assets/heroes/hero-elephant.png` | 1024×1024 | Создан, включён |
| `assets/heroes/hero-horse.png` | 1024×1024 | Создан, включён |
| `assets/heroes/hero-mila.png` | 1024×1024 | Создан, включён |
| `assets/heroes/hero-pavel.png` | 1024×1024 | Создан, включён |
| `assets/heroes/hero-wolf.png` | 1024×1024 | Создан, включён |
| `assets/moods/mood-angry.png` | 1024×1024 | Создан, включён |
| `assets/moods/mood-happy.png` | 1024×1024 | Создан, включён |
| `assets/moods/mood-sad.png` | 1024×1024 | Создан, включён |
| `assets/moods/mood-sleepy.png` | 1024×1024 | Создан, включён |
| `assets/moods/mood-surprised.png` | 1024×1024 | Создан, включён |
| `assets/objects/object-boat.png` | 1024×1024 | Создан, включён |
| `assets/objects/object-chocolate.png` | 1024×1024 | Создан, включён |
| `assets/objects/object-doll.png` | 1024×1024 | Создан, включён |
| `assets/objects/object-kolobok.png` | 1024×1024 | Создан, включён |
| `assets/objects/object-squirrel.png` | 1024×1024 | Создан, включён |

## Повторный экспорт (не нужен для запуска игры)

```sh
python3 -m venv /tmp/kg-art-venv
/tmp/kg-art-venv/bin/pip install CairoSVG==2.9.1
/tmp/kg-art-venv/bin/python assets-source.py
```

Экспорт заменяет только созданные изображения в `assets/`; не запускайте его поверх собственных заменённых иллюстраций. Рисунки используют единый контур и пастельную палитру; действия — плоские знаки с тёмно-синим контуром, оранжевым акцентом и светлой заливкой.
