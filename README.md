# Портал для проведения опросов.

## Запуск.
Докер файлы и инструкции по запуску [тут](https://github.com/H4RP3R/hr_tech_docker)  

## Использование.
Пользователи добавляются через админку django.  
Чтобы дать пользователю возможность составлять опросники, создавать вопросы и просматривать общую  
статистику необходимо в админке во вкладке " Profiles" выбрать профиль нужного пользователя,  
отметь галочкой "Is hr staff" и сохранить изменения.  
Стандартные пользователи могут только проходить опросы и просматривать свою статистику  

Опросники составляются в основном веб-интерфейсе во вкладке "ADMIN".  
Во вкладке "MAIN" отображаются доступные для прохождения опросники. Опросники публикуются к  
указанной дате. Пустые опросники так-же не доступны.  

## Возможности
* Редактор для составления вопросов с форматированием текста.
* Drag and drop наполнение опросников.
* Статистика по опросникам и отдельным вопросам с графиками.
* Просмотр ответов конкретного пользователя.

## Технологии.

### Back
1 Django
2 Django REST framework
3 PostgreSQL

### Front ([тут](https://github.com/H4RP3R/hr_tech_front))
1 Vue.js
2 Chart.js
