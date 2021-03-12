# Taller_FoxDot_TTU_2021

~~~
Material de trabajo para el taller de Livecoding con python y supercollider [FoxDot] Toda la teoria del universo 2021
~~~


## Sesión 1 


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


### sintetisadores


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
 
 ~~~
 nj >> bass (amp=.6, dur=8, )
 ~~~
 
 Acá tenemos casí lo mismo que antes solo que cambiamos el bh por cambiamos de sinte y dentro de los paretnesis pusimos dos atributos, **amp** que le indica el volumen, y **dur** que le indica una duracion en el ciclo.
 
 
 
 Para visualizar los atributos que podemos usar ejecutamos la sigiente linea 
 
 ~~~
 print(Player.get_attributes())
 ~~~
 
 ~~~
 ('degree', 'oct', 'freq', 'dur', 'delay', 'buf', 'blur', 'amplify', 'scale', 'bpm', 'sample', 'env', 'sus', 'fmod', 'pan', 'rate', 'amp', 'midinote', 'channel', 'vib', 'vibdepth', 'slide', 'sus', 'slidedelay', 'slidefrom', 'glide', 'glidedelay', 'bend', 'benddelay', 'coarse', 'striate', 'buf', 'rate', 'pshift', 'hpf', 'hpr', 'lpf', 'lpr', 'swell', 'bpf', 'bpr', 'bpnoise', 'chop', 'tremolo', 'beat_dur', 'echo', 'echotime', 'spin', 'cut', 'room', 'mix', 'formant', 'shape', 'drive')
 ~~~
 
 Para ver más información sobre los atributos y efectos [Documentación](https://foxdot.org/docs/player-attributes/)

 
 ## Sesión 3 
 
 ### samples
 
 Foxdot utiliza una libreria de samples que se interpretan con algunas botones del teclado. para ver donde está ubicada esta carpeta y descubrir que digitos podemos usar vamos al  menu superior Help & setting → open sample folder
 
 La sintaxis basica para reproducir un sample es la siguiente.
 
 ~~~
 fr >> play (" T T U" )
 ~~~
 
 En esta linea tenemos que fr es el obejto como en los sints >> dice que sonido va y en este caso está play, dentro de los parentesis y dentro de comillas estan los samples que vamos a ejecutar, en este caso T T U 
 
 ### loops
 
 
 ## Sesión 4
 
 ### patrones 
 
 ### 
 
 
 
 
 
 
















