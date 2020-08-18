
def elegirimagen(*tupla, dificultad = 'Medio'):
    Facil = {'PD':'./letras/imgpre2/rojo.png', 'IC':'./letras/imgpre2/amarillo.png', 'LD':'./letras/imgpre2/azul.png', 'LT':'./letras/imgpre2/verde.png', 'PT':'./letras/imgpre2/naranja.png', 'NORMAL':'./letras/imgpre2/blanco.png'}
    Medio = {'PD':'./letras/imgpre/PD.png', 'IC':'./letras/imgpre/IC.png', 'LD':'./letras/imgpre/LD.png', 'LT':'./letras/imgpre/LT.png', 'PT':'./letras/imgpre/PT.png', 'NORMAL':'./imagenes/img1.png'}
    Dificil = {'PD':'./letras/imgpre3/naranja.png', 'IC':'./letras/imgpre3/gris.png', 'LD':'./letras/imgpre3/celeste.png', 'LT':'./letras/imgpre3/verdeagua.png', 'PT':'./letras/imgpre3/rojo.png', 'NORMAL':'./letras/imgpre3/verde.png'}
    PT=[(0,0),(0,7),(0,14),(7,0),(7,14),(14,0),(14,7),(14,14)]
    LD=[(0,3),(0,11),(2,6),(2,8),(3,0),(3,7),(3,14),(6,2),(6,6),(6,8),(6,12),(7,3),(7,11),(8,2),(8,6),(8,8),(8,12),(11,0),(11,7),(11,14),(12,6),(12,8),(14,3),(14,11)]
    PD=[(1,1),(2,2),(3,3),(4,4),(4,10),(3,11),(2,12),(1,13),(13,1),(12,2),(11,3),(10,4),(10,10),(11,11),(12,12),(13,13)]
    LT=[(1,5),(5,5),(9,5),(13,5),(1,9),(5,9),(9,9),(13,9),(5,1),(5,13),(9,1),(9,13)]
    CTRAL=[(7,7)]
    if dificultad == 'Facil':
        if tupla in PT:
            return Facil['PT']
        elif tupla in LD:
            return Facil['LD']
        elif tupla in PD:
            return Facil['PD']
        elif tupla in LT:
            return Facil['LT']
        elif tupla in CTRAL:
            return Facil['IC']
        else:
            return Facil['NORMAL']
    elif dificultad == 'Medio':
        if tupla in PT:
            return Medio['PT']
        elif tupla in LD:
            return Medio['LD']
        elif tupla in PD:
            return Medio['PD']
        elif tupla in LT:
            return Medio['LT']
        elif tupla in CTRAL:
            return Medio['IC']
        else:
            return Medio['NORMAL']
    elif dificultad == 'Dificil':
        if tupla in PT:
            return Dificil['PT']
        elif tupla in LD:
            return Dificil['LD']
        elif tupla in PD:
            return Dificil['PD']
        elif tupla in LT:
            return Dificil['LT']
        elif tupla in CTRAL:
            return Dificil['IC']
        else:
            return Dificil['NORMAL']
