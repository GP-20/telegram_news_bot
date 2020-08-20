# telegram_news_bot
Bot de telegram que manda las noticias principales de tres sitios (El Diario, El Universal y El Economista)

A continuación se describen los archivos de ese repositorio:

## scrape
En este archivo se realiza el scraping de estos sitios web utilizando la libreria **requests** y **BeautifulSoup** 

## news_bot
En este archivo se crea un servidor local utilizando **Flask** el cual respondera a los POST requests de Telegram. Es necesario redireccionar nuestro servidor local a un servidor en linea para despues activar un [webhook](https://core.telegram.org/bots/api#setwebhook) el cual se encargará de la comunicación entre Telegram y el servidor 

## env.example
En este archivo es necesario escribir el token del bot, el cual se obtiene al mandar un mensaje al [BotFather](https://core.telegram.org/bots#6-botfather)

