def temperaturas_ciudad():
   
    temperaturas = []
    
    
    for i in range(10):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
                if -50 <= temp <= 60:  # Rango razonable
                    temperaturas.append(temp)
                    break
                else:
                    print("Temperatura fuera de rango (-50°C a 60°C)")
            except ValueError:
                print("Por favor ingrese un número válido")
    
    
    temp_maxima = max(temperaturas)
    temp_minima = min(temperaturas)
    promedio = sum(temperaturas) / len(temperaturas)
    
    
    dias_sobre_30 = sum(1 for temp in temperaturas if temp > 30)
  
    print(f"\n--- RESULTADOS TEMPERATURAS ---")
    print(f"Temperatura más alta: {temp_maxima}°C")
    print(f"Temperatura más baja: {temp_minima}°C")
    print(f"Promedio de temperaturas: {promedio:.1f}°C")
    print(f"Días por encima de 30°C: {dias_sobre_30}")
    
    return temperaturas


temperaturas_ciudad()
