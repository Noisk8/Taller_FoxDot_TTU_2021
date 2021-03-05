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


### Primeros pasos Conociendo SytnhDefs


Si ejecutamos la linea 
~~~
print(SynthDefs)
~~~

Podemos ver en la terminal de FoxDot los sintetizadores que tenemos disponibles para poner a poner a sonar 

~~~
['loop', 'stretch', 'play1', 'play2', 'audioin', 'noise', 'dab', 'varsaw', 'lazer', 'growl', 'bass', 'dirt', 'crunch', 'rave', 'scatter', 'charm', 'bell', 'gong', 'soprano', 'dub', 'viola', 'scratch', 'klank', 'feel', 'glass', 'soft', 'quin', 'pluck', 'spark', 'blip', 'ripple', 'creep', 'orient', 'zap', 'marimba', 'fuzz', 'bug', 'pulse', 'saw', 'snick', 'twang', 'karp', 'arpy', 'nylon', 'donk', 'squish', 'swell', 'razz', 'sitar', 'star', 'jbass', 'sawbass', 'prophet', 'pads', 'pasha', 'ambi', 'space', 'keys', 'dbass', 'sinepad']
~~~

 En FoxDot, todos los nombres de variables de dos caracteres están reservados para los objetos player, como 'p1'd4 ji...
 
 ~~~
 bh >> keys ()
 ~~~
 
 En esta linea tenemos algo como:  **bh**  es el objeto, **>>** designa que sinte va sonar y por ultimo tenemos **keys** que es el sinte que va sonar, luego esta el parentesis que es para ingresar argumentos al sinte.
 
 
 
















