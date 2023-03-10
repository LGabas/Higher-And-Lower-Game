import random
from art import logo,vs
from game_data import data

# ----------------------- FUNCIONES --------------------------------
def presentacion ():
    """FUNCION PARA IMPRIMIR POR PANTALLA LAS ELECCIONES A ELEGIR"""
    print(logo)
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")

def chequeo_respuesta(eleccion,number_a,number_b):
    """FUNCION PARA VERIFICAR SI LA RESPUESTA FUE CORRECTA O INCORRECTA"""
    respuesta = 0
    if eleccion == 'A':
        eleccion = number_a
        if eleccion > number_b:
            return respuesta
        else:
            return respuesta + 1
            
    elif eleccion == 'B':
        eleccion = number_b
        if eleccion > number_a:
            return respuesta
        else:
            return respuesta + 1

def nueva_presentacion ():
    """FUNCION PARA IMPRIMIR POR PANTALLA LAS NUEVAS ELECCIONES A ELEGIR"""
    print(logo)
    print(f"You're right! Current score: {score}.\nCompare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")

def nueva_eleccion (compare_a,compare_b):
    """FUNCION PARA GENERAR UNA NUEVA ELECCION DE PERSONAJES A COMPARAR"""
    compare_a = compare_b
    compare_b = random.choice(data)
    data.remove(compare_b)
    
    return compare_a,compare_b
    
        
# ----------------------- PRINCIPAL --------------------------------

compare_a = random.choice(data)
data.remove(compare_a)
compare_b = random.choice(data)
data.remove(compare_b)
presentacion()

end_game = False
score = 0
eleccion = input("Who has more followers? Type 'A' or 'B': ").upper()

while not end_game:
    
    number_a = compare_a['follower_count']
    number_b = compare_b['follower_count']
    
    respuesta = chequeo_respuesta(eleccion,number_a,number_b)
    
    if respuesta == 0:
        score += 1
        compare_a,compare_b = nueva_eleccion(compare_a,compare_b)
        nueva_presentacion()
        eleccion = input("\nWho has more followers? Type 'A' or 'B': ").upper()
    else:
        end_game = True
    
print(f"\nSorry, that's wrong. Final Score: {score}")

   
        
        
        
        
        
        

    