import PySimpleGUI as sg
import random
import os.path
import json
from Configuracion import ajustes

sg.theme('DarkPurple1')

diseño = [[sg.Text('ScrabbleAr', font = ('Times New Romas',25))],
          [sg.Button('Comenzar partida', size = (20, 1), key = 'Inicio')],
          [sg.Button('Puntajes', size = (20, 1), key = 'Puntos')],
          [sg.Button('Configuración', size = (20, 1), key = 'Config')],
          [sg.Button('Salir del juego', size = (20, 1), key = 'Salir')]]
          
if(os.path.isfile("Guardado.json")):
    diseño += [[sg.Button('Continuar partida', size=(20, 1), key="Continua")]]
    
window = sg.Window('Menu', diseño)

configuracion = {'Dificultad':'medio', 'PuntajeJugador':0, 'PuntajeCPU':0, 'Tiempo':10, 'Pal':[], 'Bolsa':[]}

while True:
    window.un_hide()
    event, f = window.read()
    if event in ("inicio", "continue"):
        if(event == 'inicio' and os.path.isfile('Guardado.json')):
            event2, _ = sg.Window('ADVERTENCIA', [[sg.T('Si inicias una nueva partida se borrara la guardada, seguro que quieres continuar?')], [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)
            if event2 == 'OK':
                remove('Guardado.json')
            else:
                continue    
        window.close()
        config['pal'] = setDif(config['dif'])
        Tablero.Jugar(config,event)
    elif event == "Puntos":
        window.hide()
        puntuaciones()
    elif event == 'Config':
        window.hide()
        configuracion = ajustes(configuracion)
    elif event in (None, 'Salir'):
        break
