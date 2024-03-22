lista_etapa_lavado = ["Llenado", "Lavado", "Enjuague", "Drenado", "Listo"]

for elemento in lista_etapa_lavado:
    print(elemento)

    if elemento == "Llenado" or elemento == "Listo":
        print("Puedo abrir la tapa")
    else:
        print("No puedo abrir la tapa, espere...")
    print("-------------------")
    