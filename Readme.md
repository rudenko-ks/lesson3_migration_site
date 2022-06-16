# Bitly url shortener

The script returns a short link in the bitly service. If the transmitted link is already short, then the number of clicks on it is displayed.

Bitly will not give you the data until you receive a personal key - `BITLY_API_TOKEN`. It is needed to interact with the Bitly API. The necessary token for working with the service can be obtained in your personal account by registering on [**bitly.com**](https://bitly.com/). You get a string like this: `17c09e20ad155405123ac1977542fecf00231da7` and should be located in the `.env` file in the root folder of the project.

### How to install

`Python3` should be already installed. 


### Virtual environments
To isolate a project, it is recommended to use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) or `venv` (built into the Python distribution)

```
pip install virtualenvwrapper
```

Use `pip` or `pip3` (if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Environment variables

Managing environment variables during development is the use of the `.env` file, which is loaded into the application when the program is executed.

Create a `.env` file at the root of the project and paste key/value pairs in the following format `BITLY_API_TOKEN=17c09e20ad155405123ac1977542fecf00231da7`.

The project is assembled and ready to run.


### Usage
```
python main.py url [-h]

```
***Arguments passed:***

`url` - link to shorten or count clicks

***Additionally:***

`-h, --help` - show program help
  
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).



# Обрезка ссылок с помощью Bitly

Скрипт возвращает короткую ссылку в сервисе bitly. Если передаваемая ссылка уже короткая, то отображается количество переходов по ней.

Bitly не даст вам данные, пока вы не получите персональный ключ – `BITLY_API_TOKEN`. Он нужен для взаимодействия с API Bitly.
Необходимый токен для работы с сервисом можно получить в личном кабинете зарегистрировавшись на сайте [**bitly.com**](https://bitly.com/). Выглядит он следующим образом: `17c09e20ad155405123ac1977542fecf00231da7` и должен располагаться в файле `.env` в корневой папке проекта.


### Как установить

`Python3` должен быть уже установлен. 

### Виртуальные окружения
Для изоляции проекта рекомендуется использовать [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) или `venv` (встроена в дистрибутив Python)

```
pip install virtualenvwrapper
```

Используйте `pip` или `pip3` (если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Переменные окружения

Управление переменными окружения в процессе разработки заключается в использовании файла `.env`, который загружается в приложение при выполнении программы.

Создайте файл `.env` корне проекта и вставьте пары ключ/значение в следующем формате `BITLY_API_TOKEN=17c09e20ad155405123ac1977542fecf00231da7`. 

Проект собран и готов к работе.

###  Выполните в консоле:

```
python main.py url [-h]

```
***Передаваемые аргументы:***

`url` - cсылка для укорачивания или подсчёта кликов

***Дополнительно:***

`-h, --help` - отобразить помощь по программе

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).