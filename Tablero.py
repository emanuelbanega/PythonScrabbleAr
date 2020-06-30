import PySimpleGUI as sg
from random import choice
import auxiliar
from validacion import validez
'''
CANTIDAD DE FICHAS POR LETRA:
A ×11, E ×11,
O ×8,
S ×7, 
I ×6, U ×6,
N ×5,
L ×4, R ×4, T ×4 ,C ×4, D ×4, 
M ×3, B ×3, 
P ×2,F ×2,G ×2, H ×2, V ×2,J ×2
K ×1, LL ×1, Ñ ×1, Q ×1, RR ×1, W ×1, X ×1 , Y ×1,Z ×1
'''

#CAN = CANTIDAD
#PUN = PUNTAJE
FICHASTOTALES= {"A":{"CAN":11,"PUN":1,"imagen":'./letras/letras60/a.png',"imagen1":'./letras/letras30/a.png'},#tengo que tener 2 imagenes uno para mostrar fichas del jugador y otro para ponerlo en el tablero
                "E":{"CAN":11,"PUN":1,"imagen":'./letras/letras60/e.png',"imagen1":'./letras/letras30/e.png'},
                "O":{"CAN":8,"PUN":1,"imagen":'./letras/letras60/o.png',"imagen1":'./letras/letras30/o.png'},
                "S":{"CAN":7,"PUN":1,"imagen":'./letras/letras60/s.png',"imagen1":'./letras/letras30/s.png'},
                "I":{"CAN":6,"PUN":1,"imagen":'./letras/letras60/i.png',"imagen1":'./letras/letras30/i.png'},
                "U":{"CAN":6,"PUN":1,"imagen":'./letras/letras60/u.png',"imagen1":'./letras/letras30/u.png'},
                "N":{"CAN":5,"PUN":1,"imagen":'./letras/letras60/n.png',"imagen1":'./letras/letras30/n.png'},
                "L":{"CAN":4,"PUN":1,"imagen":'./letras/letras60/l.png',"imagen1":'./letras/letras30/l.png'},
                "R":{"CAN":4,"PUN":1,"imagen":'./letras/letras60/r.png',"imagen1":'./letras/letras30/r.png'},
                "T":{"CAN":4,"PUN":1,"imagen":'./letras/letras60/t.png',"imagen1":'./letras/letras30/t.png'},
                "C":{"CAN":4,"PUN":3,"imagen":'./letras/letras60/c.png',"imagen1":'./letras/letras30/c.png'},
                "D":{"CAN":4,"PUN":2,"imagen":'./letras/letras60/d.png',"imagen1":'./letras/letras30/d.png'},
                "M":{"CAN":3,"PUN":3,"imagen":'./letras/letras60/m.png',"imagen1":'./letras/letras30/m.png'},
                "B":{"CAN":3,"PUN":3,"imagen":'./letras/letras60/b.png',"imagen1":'./letras/letras30/b.png'},
                "P":{"CAN":2,"PUN":3,"imagen":'./letras/letras60/p.png',"imagen1":'./letras/letras30/p.png'},
                "F":{"CAN":2,"PUN":4,"imagen":'./letras/letras60/f.png',"imagen1":'./letras/letras30/f.png'},
                "G":{"CAN":2,"PUN":2,"imagen":'./letras/letras60/g.png',"imagen1":'./letras/letras30/g.png'},
                "H":{"CAN":2,"PUN":4,"imagen":'./letras/letras60/h.png',"imagen1":'./letras/letras30/h.png'},
                "V":{"CAN":2,"PUN":4,"imagen":'./letras/letras60/v.png',"imagen1":'./letras/letras30/v.png'},
                "J":{"CAN":2,"PUN":8,"imagen":'./letras/letras60/j.png',"imagen1":'./letras/letras30/j.png'},
                "K":{"CAN":1,"PUN":8,"imagen":'./letras/letras60/k.png',"imagen1":'./letras/letras30/k.png'},
                "Ñ":{"CAN":1,"PUN":8,"imagen":'./letras/letras60/ñ.png',"imagen1":'./letras/letras30/ñ.png'},
                "Q":{"CAN":1,"PUN":10,"imagen":'./letras/letras60/q.png',"imagen1":'./letras/letras30/q.png'},
                "W":{"CAN":1,"PUN":4,"imagen":'./letras/letras60/w.png',"imagen1":'./letras/letras30/w.png'},
                "X":{"CAN":1,"PUN":8,"imagen":'./letras/letras60/x.png',"imagen1":'./letras/letras30/x.png'},
                "Y":{"CAN":1,"PUN":4,"imagen":'./letras/letras60/y.png',"imagen1":'./letras/letras30/y.png'},
                "Z":{"CAN":1,"PUN":10,"imagen":'./letras/letras60/z.png',"imagen1":'./letras/letras30/z.png'}} 
tipos=['NN','NNS','NNP', 'JJ', 'VB']
aux=auxiliar# auxiliar tiene las posiciones de las imagenes en el tablero
def vis(*t):#visibilidad de las posiciones del tablero
    if(t==(7,7)):
        return False
    else:
        return True
    
LETRAS="A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z".split()
VOCALES="A E I O U".split()

def elegirLetras(CantRandom):#este modulo elige las letras dependiendo la cantidad
    letraselegidas=[]
    for n in range(CantRandom):# aca hago que por lo menos se elija una vocal y sino hay mas fichas de vocales se usan las letras que hay
        letraelegida=choice(LETRAS)
        while (FICHASTOTALES[letraelegida]["CAN"] == 0):#aca si la ficha elegida no esta disponible se elige otra
            letraelegida=choice(LETRAS)
        if(n == (CantRandom -1) ):#aca cuando se elige la ultima ficha verifica que por lo menos si esta disponible se llegue a agregar una vocal
            if((not("A" in letraselegidas) or not("E" in letraselegidas) or not("I" in letraselegidas) or not("O" in letraselegidas) or not("U" in letraselegidas)) and not(letraelegida in ["A","E","I","0","U"])):
                if(FICHASTOTALES["A"]["CAN"] > 0 or FICHASTOTALES["E"]["CAN"] > 0 or FICHASTOTALES["I"]["CAN"] > 0 or FICHASTOTALES["O"]["CAN"] > 0 or FICHASTOTALES["U"]["CAN"] > 0):
                    listaaux=[]
                    for l in VOCALES:
                        if FICHASTOTALES[l]["CAN"] > 0:
                            listaaux.append(l)
                    letraelegida=choice(listaaux)
        FICHASTOTALES[letraelegida]["CAN"] =FICHASTOTALES[letraelegida]["CAN"]-1 #aca se decrementa la cantidad de fichas de cada letra elegida
        letraselegidas.append(letraelegida)
    return letraselegidas
def Jugar(configuracion, evento):
 CantR=7 # cantidad de fichas a elegir se puede cambiar durante el programa dependiendo las restantes
 elegidasOponente=elegirLetras(CantR)
 elegidasJugador=elegirLetras(CantR)
 print("elegidas por oponente "+str(elegidasOponente))
 print("elegidas por jugador "+str(elegidasJugador))

 MAX_ROWS = MAX_COL = 15
 imagen='./imagenes/img1.png'
 imagen1='./imagenes/img2.png'
 imagen2='./imagenes/a.png' 

 FENEMIGAS = [[sg.Button(image_filename='./imagenes/duda.png', image_size=(40,40), key=("FE"+str(m+n)),disabled=False, pad=(0,0)) for n in range(7)] for m in range(1)] #FE = FICHAS ENEMIGAS
 FJUGADOR = [[sg.Button(image_filename=FICHASTOTALES[elegidasJugador[n]]["imagen"], image_size=(60,60), key=("FJ"+str(m+n)), pad=(0,0)) for n in range(7)] for m in range(1)] #FJ = FICHAS JUGADOR
 tablero =  [[sg.Button(image_filename=aux.elegirimagen(i,j), image_size=(30,30), key=(i,j),disabled=True, pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
 #tablero=[[sg.Button(image_filename=asignarImagen(i,j), key=(i,j), image_size=(30,30), pad=(0,0)) for j in range(cantX)] for i in range(cantY)]
 
 
 colA = [[sg.Button('Guardar', size = (20, 1), key = 'Guardar')],
            [sg.Button('Terminar', size = (20, 1), key = 'Salir')],
            [sg.Frame(layout=[[sg.Text("Ponga una ficha en ST para comenzar la partida", size=(13, 10), key="-comment-", background_color="#190901")]], title="Comentarios", title_color="Yellow", background_color="Black", key="-block-")],
            [sg.Frame(layout=[[sg.Text('00:00:00', size=(13, 1), font=('Helvetica', 10), justification='center', key='-timer-', background_color="#190901")]], title="Tiempo", title_color="Orange", background_color="Black")],
            [sg.Text(text='Dificultad: ', size = (20, 1), key = 'Dificultad')],
            [sg.Text(text='Tu puntaje: 0', size = (20, 1), key = 'PuntajeJugador')],
            [sg.Text(text='Puntaje CPU: 0', size = (20, 1), key = 'PuntajeCPU')]]
 
 colC = [[sg.Button("CONFIRMAR JUGADA",key="OK")],
         [sg.Button("CANCELAR JUGADA",key="NO")]]
         
 colB = [[sg.Text("Fichas Enemigas")],[sg.Column(FENEMIGAS)],
        [sg.Column(tablero),sg.Column(colA)],
        [sg.Text("Fichas Jugador")],[sg.Column(FJUGADOR),sg.Column(colC)]]
 
 layout=[[sg.Column(colB)]]
 window = sg.Window('SCRABBLE', layout)
 ok1=False
 contadorp=-1#contador de palabras en el tablero arranca desde -1 para q al sumarlo la primera posicicion sea 0
 lugaresocupados=[]
 lugaresconfirmados=[]
 auxdatos={"coordenadas":[],"letras":[]}
 ldicocupados=[]#lista de diccionarios de letras ocupadas para restablecer
 letrasparaborrarJugador=[]
 letrasjugadasJugador=[]
 while True:
    event,values = window.read()
    #print("lugares ocupados",lugaresocupados)
    if (event==sg.WIN_CLOSED or event =="Exit"):
        break
    elif(event =="OK" and len(lugaresocupados)>=2):
        if(validez(tipos,auxdatos["coordenadas"],auxdatos["letras"]) == 2):
            for i in letrasparaborrarJugador:
                letrasjugadasJugador.append(elegidasJugador[int(i[2])])
            letrasareponer=elegirLetras(len(lugaresocupados))
            #("letras a reponer",letrasareponer,"posiciones",letrasparaborrarJugador)
            for n in range(len(letrasareponer)):
                window[letrasparaborrarJugador[n]].update(image_filename=FICHASTOTALES[letrasareponer[n]]["imagen"],disabled=False)#aca completo las fichas restantes del jugador
                elegidasJugador[int(letrasparaborrarJugador[n][2])]=letrasareponer[n]
            for n in lugaresocupados:
                lugaresconfirmados.append(n)
            #print("lugares confirmados",lugaresconfirmados)
            lugaresocupados=[]
            auxdatos={"coordenadas":[],"letras":[]}
        else:
            #print("lugares ocupados",lugaresocupados)
            temp=letrasparaborrarJugador.copy()
            for x in temp:
                window[x].update(disabled=False)
                letrasparaborrarJugador.remove(x)####
            dicaux=list(reversed(ldicocupados))
            contador=0
            for n in dicaux:
                window[n["evento"]].update(image_filename=n["imagen"])
                contador=contador+1
                if(contador == len(lugaresocupados)):
                    break
            for n in range(len(lugaresocupados)):
                posicion=(len(ldicocupados)-1)
                #print(posicion)
                ldicocupados.pop(posicion)
            
                
            if((7,7) in lugaresocupados):#aca lo que hago es si la coordenada central esta en la lista de lugares ocupados como la voy a borrar
                window[(7,7)].update(disabled=True)#la actualizo al estado inicial
                for j in range(MAX_COL):
                    for i in range(MAX_ROWS):
                        window[(j,i)].update(disabled=True)
                ok1=False
            
            lugaresocupados=[]
            auxdatos={"coordenadas":[],"letras":[]}
    
    elif("FE" not in event and (not(type(event)is tuple)) and (event!="OK")and (event!="NO")):
            window[event].update(disabled=True)
            tempevent=event
            if(ok1 == False):
                window[(7,7)].update(disabled=False)
            ok=True
            while(ok==True):
                event,values = window.read()
                if(event==sg.WIN_CLOSED or event =="Exit"):
                    break
                if("FE" not in event):
                    if("FJ" not in event and event!="OK" and event!="NO" and event not in lugaresconfirmados and event not in lugaresocupados):
                        if(ok1 == False):#si es false habilito todo el tablero
                            for j in range(MAX_COL):
                                for i in range(MAX_ROWS):
                                    window[(j,i)].update(disabled=False)
                            ok1=True
                        lugaresocupados.append(event)
                        print(lugaresocupados)
                        #print(lugaresocupados)
                        window[event].update(image_filename=FICHASTOTALES[elegidasJugador[int(tempevent[2])]]["imagen1"])#esto cambia la imagen del tablero por la letra elegida
                        ldicocupados.append({"evento":event,"imagen":window[event].ImageFilename})#guardo la posicion y la imagen actual
                        auxdatos["coordenadas"].append(event)
                        auxdatos["letras"].append(elegidasJugador[int(tempevent[2])])
                        letrasparaborrarJugador.append(tempevent)
                        
                        ok=False
                    else:
                        #######################arreglar error sigue poniendo en lugares ya ubicados###################33
                        if(event!="OK" and event!="NO" and event not in lugaresocupados and event not in lugaresconfirmados):
                            window[tempevent].update(disabled=False)
                            window[event].update(disabled=True)
                            tempevent=event
    #lo que hago cuando se cancela la jugada                        
    elif(event =="NO" and len(lugaresocupados)>=1):
        #print("lugares ocupados",lugaresocupados)
        temp=letrasparaborrarJugador.copy()
        for x in temp:
            window[x].update(disabled=False)
            letrasparaborrarJugador.remove(x)####
        dicaux=list(reversed(ldicocupados))
        contador=0
        for n in dicaux:
            window[n["evento"]].update(image_filename=n["imagen"])
            contador=contador+1
            if(contador == len(lugaresocupados)):
                break
        for n in range(len(lugaresocupados)):
            posicion=(len(ldicocupados)-1)
            #print(posicion)
            ldicocupados.pop(posicion)
        
            
        if((7,7) in lugaresocupados):#aca lo que hago es si la coordenada central esta en la lista de lugares ocupados como la voy a borrar
            window[(7,7)].update(disabled=True)#la actualizo al estado inicial
            for j in range(MAX_COL):
                for i in range(MAX_ROWS):
                    window[(j,i)].update(disabled=True)
            ok1=False
        
        lugaresocupados=[]
        auxdatos={"coordenadas":[],"letras":[]}
            
 window.close()

        
            

    # window[(row, col)].update('New text')   # To change a button's text, use this pattern
    # For this example, change the text of the button to the board's value and turn color black
        #print(event)
    #window[event].update(image_filename=choice([imagen1,imagen2]))
    #else:
        #if event in (sg.WIN_CLOSED, 'Exit'):
           # break
