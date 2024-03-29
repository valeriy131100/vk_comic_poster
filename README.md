# vk_comic_poster
Скрипт, который постит случайный комикс [xkcd](https://xkcd.com/) в заданную группу [Вконтакте](https://vk.com).

# Установка
Вам понадобится установленный Python 3.6-3.9 и git.

Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/vk_comic_poster
```

Создайте в этой папке виртуальное окружение:
```bash
$ python3 -m venv [полный путь до папки vk_comic_poster]
```

Активируйте виртуальное окружение и установите зависимости:
```bash
$ cd vk_comic_poster
$ source bin/activate
$ pip install -r requirements.txt
```
# Использование
Вам необходимо создать группу вконтакте и получить токен Вконтакте.

Чтобы получить токен Вконтакте, вам необходимо создать приложение Вконтакте. Для этого перейдите по [ссылке](https://vk.com/apps?act=manage) и нажмите на кнопку создать. Укажите необходимые данные, в качестве типа приложения выберите standalone.

После того как вы создали приложение необходимо получить его client_id. Вернитесь в список ваших приложений и нажмите на кнопку редактировать возле созданного приложения. Затем перейдите в раздел Настройки слева и скопируйте ID приложения.

После получения client_id осталось лишь получить токен. Для этого вставьте в ссылку ниже ваше значение client_id (фигурные скобки оставлять не нужно):
```text
https://oauth.vk.com/authorize?client_id={CLIENT_ID}&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos,groups,wall,offline&response_type=token&v=5.131&state=vk_comic_poster
```

Перейдите по созданной ссылке и нажмите разрешить. Вас переадресует на другую страницу. Скопируйте из адреса параметр access_token:
```text
https://oauth.vk.com/blank.html#access_token={здесь будет токен}&expires_in...
```

ID группы Вконтакте можно получить с помощью [этого сервиса](https://regvk.com/id/).

Заполните файл .env.example и переименуйте его в .env или иным образом задайте переменные среды:
* VK_ACCESS_TOKEN - токен полученный выше.
* VK_GROUP_ID - ID группы вконтакте, в которую будет производиться постинг комиксов.


Находясь в директории vk_comic_poster исполните:
```bash
$ bin/python main.py
```
В указанную группу будет опубликован случайный комикс xkcd.