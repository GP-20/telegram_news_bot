from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
import datetime
import time

options = Options()
options.headless = True

def scrape_diario(url="http://diario.mx"):
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    diario=driver.page_source
    soup=BeautifulSoup(diario,"lxml")
    driver.quit()

    noticias=soup.find("div",class_="rcm12 mas_leidas separacion_grande")
    encabe_diario=[]
    enlaces_diario=[]

    for i in noticias.find_all("h2"):
        enca=i.text
        encabe_diario.append(enca)

    for i in noticias.find_all("a"):
        links=i["href"]
        enlaces_diario.append(links)
        
    zip_diario=zip(encabe_diario,enlaces_diario)
    return zip_diario
    
def scrape_universal(url="http://eluniversal.com.mx/"):
    universal=requests.get(url,headers={"User-Agent":"Mozilla/5.0"}).text
    soup=BeautifulSoup(universal,"lxml")

    noticias=soup.find("div",class_="gl-Grid_9")
    articulos=noticias.find_all("h2",class_="titulo")

    encabe_universal=[]
    enlaces_universal=[]

    for i in articulos:
        encabe_universal.append(i.text)

    for i in articulos:
        enlaces_universal.append(i.find("a")["href"])
    
    zip_universal=zip(encabe_universal,enlaces_universal)
    return zip_universal


def scrape_economista(url="https://www.eleconomista.com.mx/"):
    economista=requests.get(url,headers={"User-Agent":"Mozilla/5.0"}).text
    soup=BeautifulSoup(economista,"lxml")
    main_frame=soup.find("div",class_="container clearfix con-banners-a-costados")
    noticias_1=main_frame.find_all("article",class_="entry-box entry-50")
    noticias_2=main_frame.find_all("article",class_="entry-box entry-25")
    noticias_3=main_frame.find_all("article",class_="entry-box entry-70")
    noticias_4=main_frame.find_all("article",class_="entry-box entry-30")
    noticias_5=main_frame.find_all("article",class_="entry-box entry-100")
    
    encabe_econ=[]
    enlaces_econ=[]
    
    try:
        for i in noticias_5:
            enca=i.find("h2").text.strip("\n").strip("\t")
            encabe_econ.append(enca)
        for i in noticias_5:
            link_lookup=i.find("a")
            sublink=link_lookup["onclick"].split(",")[1]
            link=sublink.strip(" ").split(" ")[0]
            enlaces_econ.append(link.strip("\'"))
    except:
        try:
            for i in noticias_5:   
                link_lookup=i.find("a",class_="cover-link")
                sublink=link_lookup["href"]
                link=f"https://www.eleconomista.com.mx{sublink}"
                enlaces_econ.append(link)
        except:
            pass    
    
    try:
        for i in noticias_1:
            enca=i.find("h2").text.strip("\n").strip("\t")
            encabe_econ.append(enca)
        for i in noticias_1:
            link_lookup=i.find("a",class_="cover-link")
            sublink=link_lookup["href"]
            link=f"https://www.eleconomista.com.mx{sublink}"
            enlaces_econ.append(link)
    except:
        pass
    
    try:
        for i in noticias_2:
            enca=i.find("h3").text.strip("\n").strip("\t")
            encabe_econ.append(enca)
        for i in noticias_2:
            link_lookup=i.find("a")
            link_raw=link_lookup["onclick"].split("=")[1]
            link=link_raw.split(",")
            enlaces_econ.append(link[0])
    except:
        try:
            for i in noticias_2:   
                link_lookup=i.find("a",class_="cover-link")
                sublink=link_lookup["href"]
                link=f"https://www.eleconomista.com.mx{sublink}"
                enlaces_econ.append(link)
        except:
            pass
    
    try:
        for i in noticias_3:
            enca=i.find("h2").text.strip("\n").strip("\t")
            encabe_econ.append(enca)
        for i in noticias_3:
            link_lookup=i.find("a",class_="cover-link")
            sublink=link_lookup["href"]
            link=f"https://www.eleconomista.com.mx{sublink}"
            enlaces_econ.append(link)
    except:
        pass
    
    try:
        for i in noticias_4:
            enca=i.find("h3").text.strip("\n").strip("\t")
            encabe_econ.append(enca)
        for i in noticias_4:
            link_lookup=i.find("a",class_="cover-link")
            sublink=link_lookup["href"]
            link=f"https://www.eleconomista.com.mx{sublink}"
            enlaces_econ.append(link)
    except:
        pass    


    zip_economista=zip(encabe_econ,enlaces_econ)
    return zip_economista
    

def mensaje_diario(noticias):
    news_list=[f"Las noticias de *El Diario* en este momento *{time}*"]
    x=1
    for i,j in noticias:
        linea=f"{x}. {i} \n{j}"
        news_list.append(linea)
        x+=1
    noti_diario=("\n").join(news_list)
    return noti_diario


def mensaje_universal(noticias):
    news_list=[f"Las noticias de *El Universal* en este momento *{time}*"]
    x=1
    for i,j in noticias:
        linea=f"{x}. {i} \n{j}"
        news_list.append(linea)
        x+=1
    noti_universal=("\n").join(news_list)
    return noti_universal


def mensaje_economista(noticias):
    news_list=[f"Las noticias de *El Economista* en este momento *{time}*"]
    x=1
    for i,j in noticias:
        linea=f"{x}. {i} \n{j}"
        news_list.append(linea)
        x+=1
    noti_economista=("\n").join(news_list)
    return noti_economista


time=datetime.datetime.now()
time=time.strftime("%d/%m/%Y %H:%M")
diario=scrape_diario()
universal=scrape_universal()
economista=scrape_economista()

noticias_diario=mensaje_diario(diario)
noticias_universal=mensaje_universal(universal)
noticias_economista=mensaje_economista(economista)

