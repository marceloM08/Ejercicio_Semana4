def Read_Grades():
grades = []
    try:
        cantidad = int(input("¿Cuántas notas desea ingresar? "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return notas

    for i in range(cantidad):
        while True:
            try:
                nota = int(input(f"Ingrese la nota #{i+1}: "))
                if 0 <= nota <= 100:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")
    return notas
