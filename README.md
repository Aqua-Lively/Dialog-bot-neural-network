﻿# Dialog-bot-neural-network

## Описание

Вступительное испытание на смену ML в Сириусе. Телеграмм-бот с прикрученной нейронной сетью. Его основная задача, поддерживать переписку с собеседником. Бот от модели тинькофф <b>tinkoff-ai/ruDialoGPT-medium<b>. Мне сразу понравился этот кейс и я решил взяться за него. Для себя ставил цели погрузиться в проект и с интересом реализовать его.

## Как запустить проект:
Использовал виртуальное окружение <b>pipenv<b>

1. Заходим в проект, открыаем консоль. Создаём папку <b>.venv<b> (  mkdir .venv  )
2. Прописываем в консоль (  pipenv shell  ), чтобы войти в окружение и (  pipenv install  ), чтобы загрузить все билблиотеки, которые использовались в проекте.
3. Скачиваем нейронную модель (  python .\app\model\download-model.py  )
4. Запускаем файл (  python .\app\bot\main.py  )
5. Теперь можно перейти в телеграмм и проверить бота. @Best_Friend_N1_Bot
