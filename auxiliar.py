
def elegirimagen(*tupla):
    DIC={"PD":'./letras/imgpre/PD.png',"IC":'./letras/imgpre/IC.png',"LD":'./letras/imgpre/LD.png',
"LT":'./letras/imgpre/LT.png',"PT":'./letras/imgpre/PT.png',"NORMAL":'./imagenes/img1.png'}
    PT=[(0,0),(0,7),(0,14),(7,0),(7,14),(14,0),(14,7),(14,14)]
    LD=[(0,3),(0,11),(2,6),(2,8),(3,0),(3,7),(3,14),(6,2),(6,6),(6,8),(6,12),(7,3),(7,11),(8,2),(8,6),(8,8),(8,12),(11,0),(11,7),(11,14),(12,6),(12,8),(14,3),(14,11)]
    PD=[(1,1),(2,2),(3,3),(4,4),(4,10),(3,11),(2,12),(1,13),(13,1),(12,2),(11,3),(10,4),(10,10),(11,11),(12,12),(13,13)]
    LT=[(1,5),(5,5),(9,5),(13,5),(1,9),(5,9),(9,9),(13,9),(5,1),(5,13),(9,1),(9,13)]
    CTRAL=[(7,7)]
    if tupla in PT:
        return DIC["PT"]
    elif tupla in LD:
        return DIC["LD"]
    elif tupla in PD:
        return DIC["PD"]
    elif tupla in LT:
        return DIC["LT"]
    elif tupla in CTRAL:
        return DIC["IC"]
    else:
        return DIC["NORMAL"]
