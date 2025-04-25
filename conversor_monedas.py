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

def mostrar_historial():
    print("Historial:")
    print(json.dumps(cargar_historial(), indent=4))


def conversor():
    #Usamos try para validar la entrada ddel usuario 
    try:
        #le pedimos al usuario las variavles relevantes
        while True:

            moneda_tipo_original = input("Ingrese el tipo de moneda que tiene (USD/EUR/ARS/BRL): ").upper()
            
            #asignamos el valor de la moneda orijinal en vase al archivo "valores_monedas"
            match moneda_tipo_original:
                case "USD":
                    divisor = USD
                    break
                case "EUR":
                    divisor = EUR
                    break
                case "ARS":
                    divisor = ARS
                    break
                case "BRL":
                    divisor = BRL
                    break
                case _:
                    print("Moneda original no válida")  

        while True:

            moneda_tipo_cambio = input("Ingrese el tipo de moneda al que desea cambiar (USD/EUR/ARS/BRL): ").upper()             

            #asignamos el valor de la moneda a comvertir en vase al archivo "valores_monedas"
            match moneda_tipo_cambio:
                case "USD":
                    dividendo = USD
                    break
                case "EUR":
                    dividendo = EUR
                    break
                case "ARS":
                    dividendo = ARS
                    break
                case "BRL":
                    dividendo = BRL
                    break
                case _:
                    print("Moneda a convertir no válida")
        
        dinero_cantidad = float(input("¿Cuánto dinero tiene?: "))
                    
        #calculamos la ccantidad de la nueva moneda y se lo mostramos por pantalla
        dinero_final = dinero_cantidad * (dividendo / divisor)
        print(f"Resultado: {dinero_final:.2f} {moneda_tipo_cambio}")
    except:
        print("valores invalidos")

    #Se guarda la conversión en el historial.
    entrada_historial = {
        "de": moneda_tipo_original,
        "a": moneda_tipo_cambio,
        "cantidad": dinero_cantidad,
        "resultado": round(dinero_final, 2)
    }

    historial.append(entrada_historial)
    guardar_historial(historial)

#Ejecutamos la funcion para hacer la comvercion
conversor()

#Le preguntamos al usuario si decea ver el
ver_historial = input("desea ver el historial? (s/n)").lower
if ver_historial == "si":
    mostrar_historial()
