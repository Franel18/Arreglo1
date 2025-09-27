def invertir_arreglo():
    
    numeros = []
    
    
    for i in range(6):
        while True:
            try:
                num = float(input(f"Ingrese el número {i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Por favor ingrese un número válido")
    
    print(f"\nArreglo original: {numeros}")
    
    
    # Método 1: slicing
    invertido1 = numeros[::-1]
    print(f"Arreglo invertido (método 1): {invertido1}")
    
    # Método 2: función reversed()
    invertido2 = list(reversed(numeros))
    print(f"Arreglo invertido (método 2): {invertido2}")
    
    # Método 3: manual con bucle
    invertido3 = []
    for i in range(len(numeros)-1, -1, -1):
        invertido3.append(numeros[i])
    print(f"Arreglo invertido (método 3): {invertido3}")
    
    return numeros, invertido1


invertir_arreglo()
