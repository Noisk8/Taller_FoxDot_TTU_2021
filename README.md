# Taller_FoxDot_TTU_2021

~~~
Material de trabajo para el taller de Livecoding con python y supercollider [FoxDot] Toda la teoria del universo 2021
~~~


## Sesión 1 

Presentación de lx facilitadorx y de lxs participantes...

Escuchamos una ronda con las espectativas de las participantes...


### Palabras clave

[Livecoding](https://toplap.org/about/) 

+ sobre [Livecoding](https://github.com/toplap/awesome-livecoding/)

[Foxdot](https://foxdot.org/)

[Python](https://www.python.org/)

[Supercollider](https://supercollider.github.io/)

[Git](https://git-scm.com/)

[Terminal_shell](https://es.wikipedia.org/wiki/Shell_de_Unix)

[Cmd](https://www.ionos.es/digitalguide/servidores/know-how/comandos-cmd/)


### Instalación 

[Guia oficial](https://foxdot.org/installation/)

[Linux](https://github.com/Noisk8/InstalandoFoxDot-En-linux/blob/master/Debian-Ubuntu/foxdot.sh)

[Windows]()

[Mac]()




## Sesión 2 

### Como abrir Foxdot 

#### Linux 

Abrimos una terminal y luego ↓↓↓


1  lo primero que debemos hacer es abrir el servidor del cliente de audio, en este caso usamos jack para abrirlo podemos hacerlo de dos maneras 

con el comando 
~~~
jackd -d alsa
~~~

o abriendo por la interfaz qjackctl

~~~
qjackctl
~~~


Abrimos otra terminal y luego ↓↓↓

2 Abrir SuperCollider 

~~~
scide
~~~

2.1 Después de abrir supercollider debemos arrancar el proceso de Foxdot con el siguiente comando 

~~~
FoxDot.start
~~~


Abrimos otra terminal y luego ↓↓↓


3 Abrir Foxdot con el siguiente comando 

~~~
python3 -m FoxDot
~~~






#### Windows 

#### Mac


###Primeros pasos Conociendo SytnhDefs


Si ejecutamos la linea 
~~~
print(SynthDefs)
~~~

Podemos ver en la terminal de FoxDot los sintetizadores que tenemos disponibles para poner a poner a sonar 

















