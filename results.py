def show_results(grades):
    for grade in grades:
        if grade >= 90:
            print(f"{grade} → Excelente")
        elif grade >= 70:
            print(f"{grade} → Aprobado")
        elif grade >= 60:
            print(f"{grade} → Regular")
        else:
            print(f"{grade} → Reprobado")
