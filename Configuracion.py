import PySimpleGUI as sg

def dificultadYTiempo(dificultad, tiempo):
    tiempo = int(tiempo)
    if dificultad in ('Facil','Medio','Dificil'):
        return dificultad,tiempo
    return None,tiempo

def ajustes(configuracion):
    n = []
    for i in range(1,21):
        n.append(str(i))
        
    diseño = [[sg.Text("Configuracion ScrabbleAr", size = (20, 1), font = ("Times New Roman", 16))],
             [sg.Text('Dificultad:'), sg.DropDown(('Facil','Medio','Dificil'), default_value = ('medio'), size = (20,1))],
             [sg.Text('Tiempo:', size = (20, 1)), sg.InputCombo((n), size = (5,1), default_value = '10')],
             [sg.Button('Guardar', size = (13, 1), key = 'Guardo'), sg.Exit('Regresar', size = (13, 1), key = 'Regreso')]]

    window = sg.Window('Configuracion', diseño)
    
    while True:
        evento, validacion = window.Read()
        if evento in ('Guardo'):
            try:
                dificultad, tiempo = dificultadYTiempo(validacion[0],validacion[1])
                if(dificultad == None):
                    sg.popup('ingrese valores validos')
                    continue
            except ValueError:
                sg.popup('ingrese valores validos')
            else:
                configuracion['Dificultad'] = dificultad
                configuracion['Tiempo'] = tiempo
        elif evento in (None, 'Regreso'):
            break
    window.close()
    return configuracion
