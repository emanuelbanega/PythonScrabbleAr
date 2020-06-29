import PySimpleGUI as sg
def crearTablero():
    col = fil = 15
    """
    col,fil y fichas son constantes que se usan a la hora de definir las proporciones del tablero y las fiachas por estante de jugador
    BackT es el tablero pero en back end, usado a la hora de ver el contenido de las casillas
    y es actualizado cuando se verifica una palabra
    """

    fichas = 7
    backT = [["" for i in range(col)] for i in range(fil)]
    # ColM es la columna donde se encuentra la informacion de la partida junto a otros comentarios y los botones para terminar y guardar la partida
    colM = [
        [sg.B("Guardar", size=(13, 1), key="-save-", disabled=True)],
        [sg.B("Terminar", size=(13, 1), key="Exit")],
        [sg.Frame(layout=[[sg.Text("Ponga una ficha en ST para comenzar la partida", size=(13, 10), key="-comment-", background_color="#190901")]],
                  title="Comentarios", title_color="Yellow", background_color="Black", key="-block-")],
        [sg.Frame(layout=[[sg.Text('00:00:00', size=(13, 1), font=('Helvetica', 10), justification='center', key='-timer-', background_color="#190901")]],
                  title="Tiempo", title_color="Orange", background_color="Black")],
        [sg.Text(text="Dificultad: ", size=(13, 1), key="-dif-")],
        [sg.Text(text="Tu puntaje: 0", size=(13, 1), key="-pJug-")],
        [sg.Text(text="Puntaje CPU: 0", size=(13, 1), key="-pCPU-")]
    ]

    # col board es la columna donde esta el atril del cpu y el tablero, generados de esta forma para que quede una columna al lado de la otra
    colBoard = [[sg.Text("CPU:"), sg.Text(font=("Times New Roman", 17),
                                          text="                            S C R A B B L E A R ", justification="right")]]

    colBoard += [[sg.B("?", key=('-'+str(i)), size=(2, 1), pad=(0, 0), disabled=True)
                  for i in range(fichas)]]

    colBoard += [[sg.Text("")]]

    colBoard += [[sg.B("", size=(3, 1), key=(m, n), pad=(0, 0))
                  for m in range(col)] for n in range(fil)]

    # ColPlayer es la columna donde estan las fichas del jugador
    colPlayer = [[sg.B("", size=(3, 1), key=str(k), pad=(0, 0))
                  for k in range(fichas)]for l in range(1)]

    # layout del tablero, junta todas las columnas y añade el resto de los botones
    frontT = [
        [sg.Column(colM),
         sg.Column(colBoard)],
        [sg.Text("")],
        [sg.Text("Tus fichas:"), sg.Column(colPlayer),
         sg.B("Comprobar", key="-check-", size=(10, 1)
              ), sg.B("Cambiar", key="-cambiar-", size=(10, 1)),
         sg.B("Deshacer", key="-back-", size=(10, 1))]
    ]

    tablero = sg.Window("ScrabbleAR - Juego", frontT, finalize=True)

    return tablero,backT

def cargarTablero(tablero, board, datos):
    # si es None, no hay partida guardada entonces carga la lista de tuplas por cada casilla especial
    tabla = datos['tablero']
    tablero['-pJug-'].Update(('Tu puntaje: ' + str(datos['puntosJ'])).format())
    tablero['-pCPU-'].Update(('Puntaje CPU: ' +
                              str(datos['puntosIA'])).format())                          
    tablero['-dif-'].Update(('Dificultad: ' + datos['dif']).format())
    if(datos['cambios'] == 0):
        tablero['-cambiar-'].update("Pasar")
    ActualizarAtril(tablero, datos['atrilJ'].get_atril_array())
    if(tabla == None):

        triple_letter = [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9),
                         (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)]
        double_letter = [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (
            7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11)]
        double_word = [(1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10),
                       (13, 1), (12, 2), (11, 3), (10, 4), (10, 10), (11, 11), (12, 12), (13, 13)]
        triple_word = [(0, 0), (0, 7), (0, 14), (7, 0),
                       (7, 14), (14, 0), (14, 7), (14, 14)]
        start_button = (7, 7)

        for x in triple_letter:
            tablero[x].Update(
                "Lx3", button_color=("#D4D4D4", "#8A1111"))
            board[x[0]][x[1]] = "Lx3"
        for x in double_letter:
            tablero[x].Update(
                "Lx2", button_color=("#D4D4D4", "#79118A"))
            board[x[0]][x[1]] = "Lx2"
        for x in double_word:
            tablero[x].Update(
                "Px2", button_color=("#D4D4D4", "#8A1155"))
            board[x[0]][x[1]] = "Px2"
        for x in triple_word:
            tablero[x].Update(
                "Px3", button_color=("#D4D4D4", "#0F6F6C"))
            board[x[0]][x[1]] = "Px3"
        tablero[start_button].Update(
            "St", button_color=("#D4D4D4", "#928900"))
        board[start_button[0]][start_button[1]] = "St"

    # caso contrario, recorre el tablero guardado y actualiza en base a eso
    else:

        board = tabla
        for i in range(len(tabla)):
            for j in range(len(tabla[i])):
                if(tabla[i][j] == ""):
                    continue
                elif(tabla[i][j] == "Lx3"):
                    tablero[(i, j)].Update(
                        "Lx3", button_color=("#D4D4D4", "#8A1111"))
                elif(tabla[i][j] == "Lx2"):
                    tablero[(i, j)].Update(
                        "Lx2", button_color=("#D4D4D4", "#79118A"))
                elif(tabla[i][j] == "Px2"):
                    tablero[(i, j)].Update(
                        "Px2", button_color=("#D4D4D4", "#8A1155"))
                elif(tabla[i][j] == "Px3"):
                    tablero[(i, j)].Update(
                        "Lx2", button_color=("#D4D4D4", "#0F6F6C"))
                else:
                    tablero[(i, j)].Update(tabla[i][j],button_color=(
                        "#FCFF41", "#3D2929"),disabled_button_color=(
                        "#FCFF41", "#3D2929"),disabled=True)  # color y valor de la letra que ya estaba

    return board

claveA = []
for i in range(7):
    claveA.append(str(i))
sg.theme("DarkBlue")
tablero, backT = crearTablero()
datos = {"tablero": None, 'cambios': 3}
backT = cargarTablero(tablero, backT, datos)
tablero.read()
