
#TODA LA TEORIA DEL UNIVERSO 2021

#HOLA BIENVENIDAS AL TALLER DE LIVECODING CON PYTHON Y SUPERCOLLIDER

#RECUERDA ↓↓↓

#PARA EJECUTAR UNA LINEA DE CÓDIGO PRESIONA CTRL ENTER O COMAND ENTER EN MAC


s1 >> play ("T T U" ) 

# s1 es el indicador de la linea código 

# >> indica a la linea de código que viene lance  un sonido

# play indica a la linea de codigo que va reproducir samples 

# dentro de los parentesis estan los atributos que se van a cumplir

# en este caso como es  un sample la linea va reproducir lo que este ubicado dentro de las comillas "T T U"

# algunas teclas son utilizados como samples por foxdot ver en  HELP & SETTINGS → OPEN SAMPLE FOLDER

# Estos samples pueden ser reemplazados por tus propios sonidos :) 



Clock.bpm = 90


#Foxdot esta basado en los players así que podemos nombrar nustro propio player
ttu = player()



ttu >> dirt ()



ttu >> dirt ([0,1,2,3])


ttu >> dirt ((0,2,4)) #suenen las notas a la vez




#Patron con reversa cada 4 ciclos 
ttu >> dirt ([0,1,2,3]).every(4, "reverse")


#Patron Random 


gh >> dirt (PxRand([0,1,2,3,4,5,6]))

nh >> dirt (dur=PDur(3,8), amp=.8, )



#Ejecutando loops 


nj >> loop("Foxdot")
