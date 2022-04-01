# astronomo-vs-alien

![image](https://user-images.githubusercontent.com/42480199/161172553-33fa1efc-f5ed-4a63-8ae9-fcf64ff5a43d.png)


Una vez se completa el juego, tienes la posibilidad de crear tu propio jefe y agregarlo para los demas que lo jueguen.

Primero debes de realizar una actualización
```bash
git fetch
git pull
```

Una vez que tengas tu jefe listo el juego te indicara el comando que debes correr en la terminal
```bash
git add *
git commit -a -m 'aqui va tu mensaje y nombre'
git push
```
## Instalacion
Sirve sobre Python3.6 comprobado hasta el 3.10
Notese que si tienes Python2 debes de utilizar `pip3` en cada comando, ya que todo corre con pyton3
Para empezar crea un entorno virtual para no modificar ninguna de tus librerias ya instaladas ( puedes omitir este paso en caso de que no te importe mucho, unicamente estareas instalando `pygame` )
```
pip install virtualenv
virtualenv NOMBREENTORNOVIRTUAL
```
Luego activamos esto, puedes visitar la seccion de abajo sobre como activar un entorno virtual, en este caso llamado `astrovs`

Comenzamos por instalar los requisitos, esto mediante: 
```bash
pip install -r requirements.txt
```


## Activar un Entorno virtual
Para comenzar debes de instalar los paquetes, te recomiendo activar el environment de python para que no debas instalar nada a tu python. 
Para ello dentro de la carpeta de este github dirigete a `astrovs` el cual contiene el `environment` de python.
```bash
cd astrovs\Scripts
.\activate
```
En el caso de utilizar Mac
```bash
cd astrovs\Scripts
chmod 755 activate
source .\activate
```

La ultima linea activara el `environment` por tanto no tendras que instalar nada, entonces para iniciar el juego, dirigete a la carpeta base
```bash
python .\main.py
``` 

