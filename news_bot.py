import json
import requests
from flask import Flask
from flask import request
from flask import Response
from flask_sslify import SSLify
from dotenv import load_dotenv
import os
from scrape import noticias_diario, noticias_universal, noticias_economista

def parse_message(message):
    chat_id= message["message"]["chat"]["id"]
    txt= message["message"]["text"].lower()
    valid=["diario","universal","economista","todos","/hola","/start"]
    if txt in valid:
        sitio=txt
    else:
        sitio=""
    return chat_id, sitio

def send_message(chat_id,text):
    load_dotenv()
    bot_token =  os.environ["TELEGRAM_TOKEN"]
    send_text= f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={text}"
    response = requests.post(send_text)

    return response.json()


app=Flask(__name__)
sslify=SSLify(app)

bienvenida="""Hola, soy el bot de las noticias, en este momento tengo las siguientes sitios disponibles:
-Manda la palabra *'diario'* para recibir las notas del periódico El Diario
-Manda la palabra *'economista'* para recibir las notas del periódico El Economista
-Manda la palabra *'universal'* para recibir las notas del periódico El Universal
-Manda la palabras *'todos'* para recibir las notas de todos los sitios"""

@app.route("/",methods=["POST","GET"])
def index():
    if request.method=="POST":
        msg=request.get_json()
        chat_id,sitio=parse_message(msg)
        if sitio=="/hola":
            send_message(chat_id,bienvenida)
        elif sitio=="/start":
            send_message(chat_id,bienvenida)
        elif sitio=="diario":
            send_message(chat_id,noticias_diario)
        elif sitio=="universal":
            send_message(chat_id,noticias_universal)
        elif sitio=="economista":
            send_message(chat_id,noticias_economista)
        elif sitio=="todos":
            send_message(chat_id,noticias_diario)
            send_message(chat_id,noticias_economista)
            send_message(chat_id,noticias_universal)
        else:
            send_message(chat_id,"Opción incorrecta, manda /hola para ver las opciones disponibles")
        

        return Response("ok",status=200)
    else:
        return "<h1>Noticias All_news_20bot<h1>"




if __name__ == "__main__":
    app.run(debug=True)
