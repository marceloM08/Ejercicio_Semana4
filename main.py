from grades import read_grades
from results import show_results

def main():
    user_grades = read_grades()
    show_results(user_grades)

if __name__ == "__main__":
    main()
