import random

pistas1 = [
    {"Sospechosos": "Jonny", "Persona_Inocente": False, "Habitaciones": "El patio", "Camaras_Activadas": True, "Armas": "El machete", "Arma_En_Lugar": True},
    {"Sospechosos": "Rober", "Persona_Inocente": True, "Habitaciones": "El sotano", "Camaras_Activadas": False, "Armas": "El bate", "Arma_En_Lugar": True},
    {"Sospechosos": "Arturo", "Persona_Inocente": True, "Habitaciones": "La sala", "Camaras_Activadas": True, "Armas": "El cuchillo", "Arma_En_Lugar": False},
    {"Sospechosos": "Jenny", "Persona_Inocente": True, "Habitaciones": "El atico", "Camaras_Activadas": True, "Armas": "La palanca", "Arma_En_Lugar": True},
    {"Sospechosos": "Danna", "Persona_Inocente": True, "Habitaciones": "La cocina", "Camaras_Activadas": True, "Armas": "El hacha", "Arma_En_Lugar": True}
]

pistas2 = [
    {"Sospechosos": "Jonny", "Persona_Inocente": True, "Habitaciones": "El patio", "Camaras_Activadas": True, "Armas": "El machete", "Arma_En_Lugar": False},
    {"Sospechosos": "Rober", "Persona_Inocente": False, "Habitaciones": "El sotano", "Camaras_Activadas": True, "Armas": "El bate", "Arma_En_Lugar": True},
    {"Sospechosos": "Arturo", "Persona_Inocente": True, "Habitaciones": "La sala", "Camaras_Activadas": True, "Armas": "El cuchillo", "Arma_En_Lugar": True},
    {"Sospechosos": "Jenny", "Persona_Inocente": True, "Habitaciones": "El atico", "Camaras_Activadas": False, "Armas": "La palanca", "Arma_En_Lugar": True},
    {"Sospechosos": "Danna", "Persona_Inocente": True, "Habitaciones": "La cocina", "Camaras_Activadas": True, "Armas": "El hacha", "Arma_En_Lugar": True}
]

pistas3 = [
    {"Sospechosos": "Jonny", "Persona_Inocente": True, "Habitaciones": "El patio", "Camaras_Activadas": True, "Armas": "El machete", "Arma_En_Lugar": True},
    {"Sospechosos": "Rober", "Persona_Inocente": True, "Habitaciones": "El sotano", "Camaras_Activadas": True, "Armas": "El bate", "Arma_En_Lugar": False},
    {"Sospechosos": "Arturo", "Persona_Inocente": False, "Habitaciones": "La sala", "Camaras_Activadas": True, "Armas": "El cuchillo", "Arma_En_Lugar": True},
    {"Sospechosos": "Jenny", "Persona_Inocente": True, "Habitaciones": "El atico", "Camaras_Activadas": True, "Armas": "La palanca", "Arma_En_Lugar": True},
    {"Sospechosos": "Danna", "Persona_Inocente": True, "Habitaciones": "La cocina", "Camaras_Activadas": False, "Armas": "El hacha", "Arma_En_Lugar": True}
]

pistas4 = [
    {"Sospechosos": "Jonny", "Persona_Inocente": True, "Habitaciones": "El patio", "Camaras_Activadas": False, "Armas": "El machete", "Arma_En_Lugar": True},
    {"Sospechosos": "Rober", "Persona_Inocente": True, "Habitaciones": "El sotano", "Camaras_Activadas": True, "Armas": "El bate", "Arma_En_Lugar": True},
    {"Sospechosos": "Arturo", "Persona_Inocente": True, "Habitaciones": "La sala", "Camaras_Activadas": True, "Armas": "El cuchillo", "Arma_En_Lugar": True},
    {"Sospechosos": "Jenny", "Persona_Inocente": False, "Habitaciones": "El atico", "Camaras_Activadas": True, "Armas": "La palanca", "Arma_En_Lugar": True},
    {"Sospechosos": "Danna", "Persona_Inocente": True, "Habitaciones": "La cocina", "Camaras_Activadas": True, "Armas": "El hacha", "Arma_En_Lugar": False}
]

pistas5 = [
    {"Sospechosos": "Jonny", "Persona_Inocente": True, "Habitaciones": "El patio", "Camaras_Activadas": True, "Armas": "El machete", "Arma_En_Lugar": True},
    {"Sospechosos": "Rober", "Persona_Inocente": True, "Habitaciones": "El sotano", "Camaras_Activadas": True, "Armas": "El bate", "Arma_En_Lugar": True},
    {"Sospechosos": "Arturo", "Persona_Inocente": True, "Habitaciones": "La sala", "Camaras_Activadas": False, "Armas": "El cuchillo", "Arma_En_Lugar": True},
    {"Sospechosos": "Jenny", "Persona_Inocente": True, "Habitaciones": "El atico", "Camaras_Activadas": True, "Armas": "La palanca", "Arma_En_Lugar": False},
    {"Sospechosos": "Danna", "Persona_Inocente": False, "Habitaciones": "La cocina", "Camaras_Activadas": True, "Armas": "El hacha", "Arma_En_Lugar": True}
]


def seleccionar_caso():
    numero_aleatorio = random.randint(1, 5)

    if numero_aleatorio == 1:
        return pistas1
    elif numero_aleatorio == 2:
        return pistas2
    elif numero_aleatorio == 3:
        return pistas3
    elif numero_aleatorio == 4:
        return pistas4
    else:
        return pistas5

def hacer_pregunta(Dato_buscado, categoria_buscada, Caso_buscado):
    encontrado = False
    
    for pista in Caso_buscado:
        if pista[categoria_buscada] == Dato_buscado:
            print(f"\nInformación de: {Dato_buscado}:")
            if pista["Persona_Inocente"] == True:
                print(f"{pista['Sospechosos']} ha demostrado ser inocente, estuvo en")
            else:
                print(f"{pista['Sospechosos']} no parece ser inocente, dice haber estado en")
            if pista["Camaras_Activadas"] == True:
                print(f"{pista['Habitaciones']}, que está en buen estado aquí no pasó nada.")
            else:
                print(f"{pista['Habitaciones']}, que está en muy mal estado aquí pasó algo malo.")
            if pista["Arma_En_Lugar"] == True:
                print(f"{pista['Armas']} se encontró en su lugar, no ha sido usado.")
            else:
                print(f"{pista['Armas']} no se encontró en su lugar, esto es muy sospechoso...")
            encontrado = True
            break

    if not encontrado:
        print(f"{Dato_buscado} no encontrado en la lista de pistas.")

def seleccionar_categoria ():
    print("\n\nTienes 3 posibles catiegorias: Sospechosos, Habitaciones y Armas\n")
    Categoria=input("Escoje: ")
    return Categoria

def seleccionar_dato (categoria_buscada):
    if categoria_buscada=="Sospechosos":
        print("Los posibles sospechosos son: Jonny, Rober, Arturo, Jenny o Danna\n")
        Dato=input("Escoje: ")
        return Dato
    if categoria_buscada=="Habitaciones":
        print("Las posibles habitaciones son: La cocina, La sala, El patio, El atico o El sotano\n")
        Dato=input("Escoje: ")
        return Dato
    if categoria_buscada=="Armas":
        print("Las posibles Armas son: El cuchillo, El hacha, El bate, La palanca y El machete\n")
        Dato=input("Escoje: ")
        return Dato
       
def Corroborar_crimen (Caso_buscado, Sospecha_personaje, Sospecha_habitacion, Sospecha_arma):
    Culpable=0
    for pista in Caso_buscado:
        if pista["Sospechosos"] == Sospecha_personaje :
            if pista["Persona_Inocente"] == False:
                Culpable=Culpable+1
    for pista in Caso_buscado:
        if pista["Habitaciones"] == Sospecha_habitacion :
            if pista["Camaras_Activadas"] == False:
                Culpable=Culpable+1
    for pista in Caso_buscado:
        if pista["Armas"] == Sospecha_arma :
            if pista["Arma_En_Lugar"] == False:
                Culpable=Culpable+1
    return Culpable

while True:
    
    print("Eres el detective a cargo de investigar un asesinato en la mansión.\nHay 5 sospechosos, 5 habitaciones y 5 posibles armas.\nTienes 5 Policias listos para investigar un solo dato:\nA un sospecho, una habitacion en concreto o un Arma.\nSon buenos policias, cada uno te dira quien, en donde y el arma relacionada a su investigación.\nTu debes descubrir al asesino, la habitación del crimen y el arma homicida.")
    print("\nDile a tus investigadores:\nla categoría (sospecho, habitación o arma)\nY el dato especifico a buscar (Jonny, Sala, Cuchillo etc..)\nQue comience la busqueda:\n\n")
    Caso_buscado = seleccionar_caso()
    
    for i in range(5):
        categoria_buscada = seleccionar_categoria()
        Dato_buscado = seleccionar_dato(categoria_buscada)
        hacer_pregunta(Dato_buscado, categoria_buscada, Caso_buscado)
        
    Sospecha_personaje=input("Es la hora detective, quien es el asesino? (Jonny, Rober, Arturo, Jenny o Danna)\n")
    Sospecha_habitacion=input("Es la hora detective, donde fue el asesinato? (La cocina, La sala, El patio, El atico o El sotano)\n")
    Sospecha_arma=input("Es la hora detective, cual arma se usó? (El cuchillo, El hacha, El bate, La palanca y El machete)\n")   
    
    print("El detective concluye que el asisino es: ",Sospecha_personaje,".\nEl crimen se cometió en ",Sospecha_habitacion,".\nCon ",Sospecha_arma,".\n")
    
    Culpable=Corroborar_crimen(Caso_buscado, Sospecha_personaje, Sospecha_habitacion, Sospecha_arma)
    if Culpable==3:
        print("Felicitaciones detective, el caso a sido resuelto correctamente, el asesino irá a prisión :D")
    else:
        print("Hemos fallado, el asesino no a podido ser procesado y ahora está libre :C")
    
    break   