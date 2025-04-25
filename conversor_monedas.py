import json
import os
from valores_monedas import USD, EUR, ARS, BRL

HISTORIAL_FILE = "historial.json"

#Función para cargar historial desde el archivo.
def cargar_historial():
    if os.path.exists(HISTORIAL_FILE):
        with open(HISTORIAL_FILE, "r") as file:
            return json.load(file)
    else:
        return []

#Función para guardar en el archivo de historial.
def guardar_historial(historial):
    with open(HISTORIAL_FILE, "w") as file:
        json.dump(historial, file, indent=4)

#Función que pregunta al usuario si desea borrar o no el historial.
borrar = input("¿Querés borrar el historial? (s/n): ").lower()
if borrar == "s":
    guardar_historial([])
    print("Historial borrado.")

#Se carga el historial actual.
historial = cargar_historial()


moneda_tipo_original = input("Ingrese el tipo de moneda que tiene: ").upper()
moneda_tipo_cambio = input("Ingrese el tipo de moneda al que desea cambiar: ").upper()
dinero_cantidad = float(input("¿Cuánto dinero tiene?: "))

match moneda_tipo_original:
    case "USD":
        divisor = USD
    case "EUR":
        divisor = EUR
    case "ARS":
        divisor = ARS
    case "BRL":
        divisor = BRL
    case _:
        print("Moneda original no válida")
        exit()

match moneda_tipo_cambio:
    case "USD":
        dividendo = USD
    case "EUR":
        dividendo = EUR
    case "ARS":
        dividendo = ARS
    case "BRL":
        dividendo = BRL
    case _:
        print("Moneda a convertir no válida")
        exit()

dinero_final = dinero_cantidad * (dividendo / divisor)
print(f"Resultado: {dinero_final:.2f} {moneda_tipo_cambio}")

#Se guarda la conversión en el historial.
entrada_historial = {
    "de": moneda_tipo_original,
    "a": moneda_tipo_cambio,
    "cantidad": dinero_cantidad,
    "resultado": round(dinero_final, 2)
}

historial.append(entrada_historial)
guardar_historial(historial)
