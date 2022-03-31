# astronomo-vs-alien

![image](https://user-images.githubusercontent.com/42480199/161132547-781816b7-dd77-45a5-b1fb-898efbbed0ae.png)

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

## Instalación
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

