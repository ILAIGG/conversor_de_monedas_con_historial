import json
from valores_monedas import USD, EUR, ARS, BRL

moneda_tipo_original = input("ingrese el tipo de moneda que tiene :").upper()

moneda_tipo_cambio = input("ingrese el tipo de moneda al que decea cambiar :").upper()

dinero_cantidad = int(input("cuanto dinero tiene? :"))

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
        print("Moneda original no válida")


    
dinero_final = dinero_cantidad*(dividendo/divisor)

print(dinero_final)


