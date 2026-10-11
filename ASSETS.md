# Пользовательские изображения

Источник: архив `Kruti_i_govori_assets_and_TZ.zip`, предоставленный пользователем. 20 PNG перенесены без изменения байтов; корпус заменён исправленной генерацией. В архиве использована более ранняя редакция ТЗ; реализация ориентируется на отдельно приложенное новое ТЗ.

| Файл | Статус |
|---|---|
| `assets/actions/action-break.png` | Подключён без изменения |
| `assets/actions/action-catch.png` | Подключён без изменения |
| `assets/actions/action-push.png` | Подключён без изменения |
| `assets/actions/action-put-to-bed.png` | Подключён без изменения |
| `assets/actions/action-stroke.png` | Подключён без изменения |
| `assets/backgrounds/game-background.png` | Подключён без изменения |
| `assets/heroes/hero-elephant.png` | Подключён без изменения |
| `assets/heroes/hero-mila.png` | Подключён без изменения |
| `assets/heroes/hero-pavel.png` | Подключён без изменения |
| `assets/heroes/hero-wolf.png` | Подключён без изменения |
| `assets/interface/machine-frame.png` | Сгенерирован из пользовательского корпуса: ручка удалена, центр очищен |
| `assets/moods/mood-angry.png` | Подключён без изменения |
| `assets/moods/mood-happy.png` | Подключён без изменения |
| `assets/moods/mood-sad.png` | Подключён без изменения |
| `assets/moods/mood-sleepy.png` | Подключён без изменения |
| `assets/moods/mood-surprised.png` | Подключён без изменения |
| `assets/objects/object-boat.png` | Подключён без изменения |
| `assets/objects/object-chocolate.png` | Подключён без изменения |
| `assets/objects/object-doll.png` | Подключён без изменения |
| `assets/objects/object-kolobok.png` | Подключён без изменения |
| `assets/objects/object-squirrel.png` | Подключён без изменения |
| `assets/heroes/hero-horse.png` | Предоставлен пользователем отдельно, подключён без изменения |
| `assets/interface/machine-lever.png` | Сгенерирован и подключён |

План полного набора: 20 карточек, фон, неподвижный корпус и отдельный рычаг — 23 файла. Предоставленные карточки имеют размер 1254×1254, фон — 1672×941. Размеры новых генераций сохраняются без растягивания в интерфейсе. Автоматический повторный экспорт старой графики удалён, чтобы не перезаписать пользовательские изображения.

Корпус и рычаг созданы инструментом image_gen по запросу пользователя. Оригиналы сохранены в `/workspace/generated_images/`. Все изображения имеют настоящий прозрачный внешний фон.

Полный набор содержит 23 PNG. Лошадь получена из отдельного пользовательского ZIP; предыдущий блокер устранён.

## Обновление качеств и аппарата

Аппарат теперь создан HTML/CSS, поэтому `machine-frame.png` и игровой фон не используются. Старые `mood-sad`, `mood-surprised`, `mood-angry`, `mood-sleepy` сохранены как исходные материалы и исключены из словаря игры.

Новые изображения созданы image_gen: `mood-brave.png` (щит), `mood-agile.png` (мячики), `mood-affectionate.png` (сердце в ладонях), `mood-nice.png` (солнышко). `mood-happy.png` сохранён пользовательский. Все подписи создаёт HTML и согласует с родом героя.
