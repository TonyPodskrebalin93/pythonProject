grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


def get_average_grades_students(students: set, grades: list) -> dict:
    average_grades_students = {}
    students = sorted(students)
    for i in range(len(students)):
        average_grades_students[students[i]] = sum(grades[i]) / len(grades[i])
    return average_grades_students


res = get_average_grades_students(students, grades)
print(res)