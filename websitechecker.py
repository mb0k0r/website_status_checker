import requests
from requests.exceptions import ReadTimeout
import schedule
import time
import datetime
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
# Configuración del correo electrónico
FROM_EMAIL = 'tucorreo@gmail.com'
FROM_PASSWORD = 'contraseña de aplicación otorgada por Google'
INTERVAL = 15 # Cada cuantos minutos ejecuta el checkeo de las webs

# Carga el archivo Excel
dfwebsites = pd.read_excel("C:\\ejemplo\\websites.xlsx")
dfemails = pd.read_excel("C:\\ejemplo\\emails.xlsx")

# Define la función para revisar la disponibilidad del sitio web
def check_website(url):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return True
        else:
            return False
    except (requests.exceptions.Timeout, ReadTimeout):
        print("TIMEOUT DE " + url)
        return False
 
# Defino la función para enviar correos electrónicos
def send_email(url):
    for idx, emails in dfemails.iterrows():
        message = MIMEMultipart()
        message['From'] = FROM_EMAIL
        message['To'] = emails[0]
        message['Subject'] = 'WEBSITE ' + url + ' NO DISPONIBLE'
        body = 'Website ' + url + ' no se encuentra disponible en este momento.'
        message.attach(MIMEText(body, 'plain'))
    
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(FROM_EMAIL, FROM_PASSWORD)
            text = message.as_string()
            server.sendmail(FROM_EMAIL, emails[0], text)
            server.quit()
            print("Correo electrónico enviado exitosamente a:", emails[0])
        except Exception as e:
            print("Ocurrió un error al enviar el correo electrónico:", str(e))

# Defino la función que se ejecutará periódicamente
def check_websites():
    print("--- STARTING SCRIPT AT {} ---".format(datetime.datetime.now()))
    for idx, sites in dfwebsites.iterrows():
        url = str(sites[0])
        if not check_website(url):
            print(url, ' -- NOT AVAILABLE')
            send_email(url)
        else:
            print(url, ' -- OK')
    print("--- SCRIPT END ---\n")
 
# Programa principal
schedule.every(INTERVAL).minutes.do(check_websites)
 
while True:
    schedule.run_pending()
    time.sleep(1)
