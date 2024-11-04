import random
import json

def cargar_palabras():
    with open('palabras-disponibles.json', 'r') as file:
        data = json.load(file)
        return data['palabras']

def seleccionar_palabra(palabras):
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    return progreso

def juego():
    palabras = cargar_palabras()
    palabra_seleccionada = seleccionar_palabra(palabras)
    letras_adivinadas = set()
    intentos = 6

    print("¡Bienvenido al juego de adivinanza de palabras!")
    
    while intentos > 0:
        print(f"\nPalabra: {mostrar_progreso(palabra_seleccionada, letras_adivinadas)}")
        print(f"Intentos restantes: {intentos}")
        print("Letras adivinadas:", ' '.join(sorted(letras_adivinadas)))
        
        letra = input("Adivina una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue
        
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta otra.")
            continue
        
        letras_adivinadas.add(letra)

        if letra not in palabra_seleccionada:
            intentos -= 1
            print(f"Letra '{letra}' no está en la palabra.")
        
        if all(letra in letras_adivinadas for letra in palabra_seleccionada):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_seleccionada}")
            break
    else:
        print(f"¡Perdiste! La palabra era: {palabra_seleccionada}")

if __name__ == "__main__":
    juego()
