### Запуск проекта:

Вы можете запустить проект 2 способами:

А): через докер. Тогда **docker compose up**



Б): через py manage.py runserver (перед этим понадобится создать базу данных, как указано в параметрах settings/runserver_settings):

1 терминал:

**docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management**

2 терминал:

**celery -A forum worker --loglevel=info (или celery -A forum worker -l info -P eventlet)**

3 терминал:

**docker run -it --name redis -p 6379:6379 redis**

4 терминал:

**py manage.py runserver --settings=forum.settings.runserver_settings**

Так же в директории forum содержится файл mysite_data.json с данными из моей БД

### Краткий обзор:

**Аккаунт**:
- Есть возможность авторизации через Google
- При создании нового аккаунта/смене почты на почту будет отправлен код подтверждения. (За отправку кода отвечает работник celery);
- Есть возможность генерировать ключ для входа без пароля и логина, для этого в детальной информации о аккаунте нужно кликнуть по соответствующей ссылки и ввести пароль от аккаунта;
- На странице детальной информации доступно удаление статей и комментариев;
- Каждая статья имеет количество просмотров, просмотры уникальные: если пользователь авторизован, создаётся ключ в редисе с user.id как часть ключа и article.id как значение ключа. Если пользователь неавторизован, то информация о том, что пользователь просмотрел данную статью закидывается пользователю в сессию.

**Статьи**:
- Возможен поиск по тегу, теги у каждого поста кликабельны;
- Есть триграммный поиск для поиска статей;
- Фреймворк сообщений уведомит при создании/попытке создания статьи и успехе/неудаче;
- Для создания статьи минимум 1 тег;
- Теги нельзя создавать, лишь пользоваться существующими
- Есть markdown.

**Api**:
- CRUD функционал.

**Тестирование**:
- при запуске юнит тестов py manage.py test нужно поменять настройки кеширования на DummyCache, в настроечном файле есть заготовка.

Есть карты сайта
Форум доступен в 2 языках: английский и русский
