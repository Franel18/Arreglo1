def ventas_semana():
    ventas = []
    
    
    for i in range(7):
        while True:
            try:
                venta = float(input(f"Ingrese las ventas del día {i+1}: "))
                if venta >= 0:
                    ventas.append(venta)
                    break
                else:
                    print("Las ventas no pueden ser negativas")
            except ValueError:
                print("Por favor ingrese un número válido")
    
    
    total_semana = sum(ventas)
    promedio_diario = total_semana / 7
    venta_maxima = max(ventas)
    dia_maximo = ventas.index(venta_maxima) + 1
    
    
    print(f"\n--- RESULTADOS ---")
    print(f"Total vendido en la semana: ${total_semana:.2f}")
    print(f"Promedio diario: ${promedio_diario:.2f}")
    print(f"Día con mayor venta: Día {dia_maximo} (${venta_maxima:.2f})")
    
    return ventas


ventas_semana()
