#leer n cantidad de notas y
#decir si es aprendizaje inicial, fundamental, satisfactorio o avanzado
#mostrar todas las notas.

def classify_grade(grade):
    if grade < 60:
        return "Aprendizaje inicial"
    elif 60 <= grade < 70:
        return "Fundamental"
    elif 70 <= grade < 90:
        return "Satisfactorio"
    else:
        return "Avanzado"


def read_grades():
    grades = []
    try:
        amount = int(input("¿Cuántas notas desea ingresar?"))
    except ValueError:
        print("Debe ingresar un número válido.")
        return grades

    for i in range(amount):
        while True:
            try:
                grade = int(input(f"INgrese la nota #{i+1}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("La nota debe ser entre 0 y 100.")
            except ValueError:
                print("Ingrese un número entero.")
    return grades


def show_results(grades):
    print("\n=== Resultado ===")
    for grade in grades:
        print(f"Nota: {grade} → {classify_grade(grade)}")


def main():
    user_grades = read_grades()
    show_results(user_grades)


main()
