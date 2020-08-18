from Configuracion import ajustes
from random import randint
import PySimpleGUI as sg
import json
import os.path
import Tablero

def setDificultad(dificultad):
    if(dificultad == 'Facil'):
        return ['Sustantivos', 'Adjetivos', 'Verbos']
    elif(dificultad == 'Medio'):
        return ['Sustantivos', 'Verbos']
    elif(dificultad == 'Dificil'):
        i = randint(0,2)
        dif = ['Sustantivos', 'Adjetivos', 'Verbos']
        return dif[i]
        
sg.theme('DarkPurple1')

diseño = [[sg.Text('ScrabbleAr', font = ('Times New Romas',25))],
          [sg.Button('Comenzar partida', size = (20, 1), key = 'Inicio')],
          [sg.Button('Puntajes', size = (20, 1), key = 'Puntos')],
          [sg.Button('Configuración', size = (20, 1), key = 'Configuracion')],
          [sg.Button('Salir del juego', size = (20, 1), key = 'Salir')]]
          
if(os.path.isfile("Guardado.json")):
    diseño += [[sg.Button('Continuar partida', size=(20, 1), key = "Continua")]]
    
window = sg.Window('Menu', diseño)

configuracion = {'Dificultad':'Medio', 'PuntajeJugador':0, 'PuntajeCPU':0, 'Tiempo':10, 'Palabras':[], 'Bolsa':[]}

while True:
    evento, f = window.read()
    if evento in ('Inicio', 'Continua'):
        if(evento == 'inicio') and (os.path.isfile('Guardado.json')):
            segundoEvento, f = sg.Window('Partida anterior guardada', [[sg.Text('Desea continuar la partida anterior?')], [sg.Button('Aceptar'), sg.B('Cancelar') ]]).read()
            if segundoEvento == 'Aceptar':
                remove('Guardado.json')
            else:
                continue    
        window.close()
        configuracion['Palabras'] = setDificultad(configuracion['Dificultad'])
        Tablero.Jugar(configuracion, evento)
    elif evento == "Puntos":
        window.hide()
        puntuaciones()
    elif evento == 'Configuracion':
        window.hide()
        configuracion = ajustes(configuracion)
        window.UnHide()
    elif evento in (None, 'Salir'):
        break
