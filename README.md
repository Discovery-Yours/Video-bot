
Совместный хакатон Инженерной школы ГУАП и компании «RuFilms» по созданию видео-чатбота
 Задача Хакатона выполняется индивидуально или в составе команд из 2х человек
    1. Задачи для решения в рамках Хакатона: 
        a. Необходимо реализовать клиент-серверную архитектуру.
        b. Создать web-страницу (или мобильное приложение) с чат-ботом и встроенным видео-плеером.
        c. Реализовать ответы бота в виде коротких видео в плеере в соответствии с ключевыми словами в сообщениях пользователя (примеры видео для тестирования работы серверной части в локальном режиме будут выданы участникам перед началом выполнения задания, тематику видеочат-бота команды участников должны будут определить самостоятельно, ключевые слова система должна анализировать из текста сообщений пользователей в соответствии с тематикой чат-бота).
        d. Видеочат-бот должен уметь:
        ◦ Поприветствовать пользователя несколькими вариантами;
        ◦ Попрощаться с пользователем несколькими вариантами;
        ◦ Запустить видео из интернета или из локального хранилища по ключевым словам;
        ◦ Задать пользователю не менее 2-х иерархических вопросов для уточнения содержимого сообщения и более точного отображения видео-ответа;
        ◦ Учитывать вариативность сообщений пользователей (например, утро, с утра, утром, с утреца, morning, a.m. и т.п.);
        e. Применять при работе на Хакатоне систему контроля версий, предоставленную организаторами мероприятия.
    2. Документация для реализации задач: 
    • https://medium.com/@awesammcoder/javascript-tutorial-simple-chatai-using-rivescript-js-4f0291e298f1 — Javascript Tutorial — Simple ChatAI using RiveScript.js
    • https://codeanddogs.medium.com/javascript-chatbot-in-10-minutes-d40630324430 — JavaScript Chatbot in 10 Minutes
    • https://www.htmlgoodies.com/javascript/basic-chatbot-in-javascript/ — Basic Chatbot in Javascript
    • https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio — Build a WhatsApp Chatbot With Python
    • https://pythonist.ru/sozdanie-chat-bota-v-python/ — Создание чат-бота на Python
    • https://www.machinelearningmastery.ru/build-your-first-chatbot-using-python-nltk-5d07b027e727/ — Создайте свой первый чат-бот, используя Python NLTK
    • https://dev.to/sahilrajput/build-a-chatbot-using-flask-in-5-minutes-574i — Build a Chatbot using Flask in 5 minutes 
    • https://medium.datadriveninvestor.com/building-a-machine-learning-chat-bot-with-flask-framework-and-python-2c24b2def49b — Building A Machine learning chat-bot with flask framework and python
    • https://dev-gang.ru/article/sozdaite-prostoi-czat-bot-s-python-i-google-search-wptggrso22/ — Создайте простой чат-бот с Python и Google Search 
    • https://www.i2tutorials.com/build-chatbot-using-python/ — Build ChatBot Using Python

3. Пример сценария чат-бота.
Видеобот: Здравствуйте! На связи видеочат-бот компании NNN. Чем могу помочь? 
Клиент: Сколько по времени займет предоставление услуги? (Ключевые слова: сколько, времени, услуга, ?) 
Видеобот: Предоставление услуги обычно занимает 5 рабочих дней. Подробнее о факторах, которые могу повлиять на сроки, можно прочитать здесь: https://google.com. 
Пользователь: на какое время я могу записаться? (Ключевые слова: запись, время, какое, ?)
Видеобот: имеется запись на сегодня на 10 часов
Клиент: Я хотел бы записаться на услугу в другое время (Ключевые слова: запись, другое, время)
Видеобот: Я могу записать Вас на завтра на утро, день или вечер. Выберите подходящее Вам время суток
Клиент: Хочу прийти утром (Ключевые слова: утро, с утра и т.п.)
Видеобот: имеется свободное время на завтра на 10, 11, 12 часов (в соответствии с предыдущим ответом пользователя) 
Видеобот: Чтобы подтвердить заказ, нажмите сюда: https://google.com. 
(Клиент нажимает)
Видеобот: Если я могу еще чем-то Вам помочь, напишите что-то еще 
Клиент: Я хочу записать друга (Ключевые слова: запись, …)
Видеобот: (продолжение диалога)



