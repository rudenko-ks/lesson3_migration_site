# Bitly url shortener

The script returns a short link in the bitly service. If the transmitted link is already short, then the number of clicks on it is displayed.

### How to install

Python3 should be already installed. 
Then use `pip` or `pip3` (if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Bitly will not give you the data until you receive a personal key - `TOKEN`. It is needed to interact with the Bitly API.

On [**bitly.com**](https://bitly.com/), you get a string like this: `17c09e20ad155405123ac1977542fecf00231da7` .

### Usage
```
python main.py [-h] url
```
positional arguments:
  `url`         link

options:
  `-h, --help`  show this help message and exit
  
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).



# Обрезка ссылок с помощью Bitly

Скрипт возвращает короткую ссылку в сервисе bitly. Если передаваемая ссылка уже короткая, то отображается количество переходов по ней.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` или `pip3` (есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Bitly не даст вам данные, пока вы не получите персональный ключ – `TOKEN`. Он нужен для взаимодействия с API Bitly. 

На сайте [**bitly.com**](https://bitly.com/) вы получили строку наподобие такой: `17c09e20ad155405123ac1977542fecf00231da7` .

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).