Python web scraping test.

Para el desarollo de esta prueba se utilizo la version de python 3.9.11.
Tambien se hizo el uso de diferentes librerias y paquetes que se encuentran en el archivo 'requeriments.txt'. Todo el proyecto se llevo a cabo dentro de un entorno virtual.
Para la instalacion de los diferentes paquetes haga uso del comando 'pip *nombre del paquete*'.

Twitter, Facebook scrapers.
La funcion principal de estos scraper se llevo a cabo mediante Selenium. Con este se pudo extraer todos los datos necesarios para realizar su tarea, para despues ser almacenados en un archivo .csv.

## Versiones

    python 3.9.11
    pip 22.0.4

## Crear variables de entorno (variables.sh):
```
    export CSV_DELIMITER=";"
    #Facebok
    export FACEBOOK_COMENTARIO_CLASE="_2b06"
    #Instagram
    export INSTA_ID_CLASE="_a9zc"
    export INSTA_COMENTARIO_CLASE="_a9zs"
    #Twitter
    export TWEETS_LIMIT=500

```
## Crear entorno virtual:

    $ python -m venv env

## Activar entorno virtual:

    $ source env/bin/activate

##  Cargar las variables de entorno dentro del entorno virtual activado:

    $ source variables.sh

## Desde la carpeta del proyecto instalar los requerimientos (asegurar que su entorno virtual esta activado):

    (env)$ pip install -r requirements.txt

## Correr cada archivo y esperar que termine su tarea

    (env)$ python facebook.py
    (env)$ python twitter.py
    (env)$ python insta.py