# Advertencias y descargos de responsabilidad 
Este script no es para ser utilizado con fines maliciosos. El usuario es responsable de cualquier uso indebido del script. El script monitorea la disponibilidad de una web y notifica cuando esté fuera de línea. No es un ataque DDoS. Por favor, úsenlo responsablemente. 


# Verificación del estado de la página web y notificación por correo electrónico

Este script de Python verifica si una página web está en línea y, si no lo está, envía una notificación por correo electrónico utilizando la cuenta de Gmail del remitente. El script está escrito en Python 3.

## Requisitos previos

1. Python 3 instalado en tu sistema.
   - Windows: Descarga e instala Python 3 desde https://www.python.org/downloads/windows/
   - macOS: Descarga e instala Python 3 desde https://www.python.org/downloads/mac-osx/
   - Linux: La mayoría de las distribuciones de Linux tienen Python 3 preinstalado. Si no es así, consulta la documentación de tu distribución para obtener instrucciones sobre cómo instalar Python 3.

2. Instalar pip:
   - Windows: Python 3.4 y versiones posteriores ya incluyen pip. Si necesitas actualizarlo, sigue las instrucciones en https://pip.pypa.io/en/stable/installation/
   - macOS: Python 3.4 y versiones posteriores ya incluyen pip. Si necesitas actualizarlo, sigue las instrucciones en https://pip.pypa.io/en/stable/installation/
   - Linux: Consulta la documentación de tu distribución para obtener instrucciones sobre cómo instalar pip.

3. Instalar bibliotecas requeridas:

- Ejecuta el siguiente comando en la terminal (después de navegar a la carpeta donde se encuentra el archivo `requirements.txt`):
    ```
    pip install -r requirements.txt
    ```

4. Configura la verificación en dos pasos para tu cuenta de Google:
- Sigue las instrucciones en https://www.google.com/landing/2step/

5. Establece una contraseña de aplicación para tu cuenta de Google:
- Sigue las instrucciones en https://support.google.com/accounts/answer/185833?hl=es


## Configuración

1. Abre el script en un editor de texto y actualiza las siguientes variables con tus propios valores:

- FROM_EMAIL = "tucorreo@gmail.com"
- FROM_PASSWORD = "contraseña de aplicación otorgada por Google"
- INTERVAL = 10 (cada cuantos minutos se ejecuta el script, en este caso 10, cambiar a gusto)


2. Crear dos archivos en excel con los websites y los mails a informar respectivamente e indicar la ruta de los mismos, luego indicar la ruta.
```
dfwebsites = pd.read_excel("C:\\ejemplo\\websites.xlsx")
dfemails = pd.read_excel("C:\\ejemplo\\emails.xlsx")
```
estos archivos deben contener una sola columna de datos.

## Uso

1. Abre una terminal o símbolo del sistema.

2. Navega hasta el directorio donde se encuentra el script.

3. Ejecuta el script con el siguiente comando:


- `python websitechecker.py`


Reemplaza "websitechecker.py" con el nombre del archivo si lo has cambiado.

El script verificará continuamente el estado de las páginas web e imprimirá un mensaje en la terminal cada 10 minutos, indicando el estado de las webs incluidas en el excel, en caso de que alguna no devuelva codigo 200 se indicará un mensaje NOT AVAILABLE y enviará los emails.

## Nota importante

Este script utiliza una conexión SMTP segura para enviar correos electrónicos a través de Gmail. Sin embargo, no es recomendable almacenar contraseñas en texto plano en un archivo de código. Asegúrate de proteger tus credenciales adecuadamente y considera utilizar soluciones de almacenamiento seguro, como un administrador de contraseñas o variables de entorno.
