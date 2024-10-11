students = [
    ["OLGA",20, 49],
    ["NZIZA", 23, 60],
    ["KEZA", 15, 65],
    ["ANNA", 13, 50],
    ["MWIZA", 13, 68]
]
students_sorted_by_grade = sorted(students, key=lambda student: student[2])

for student in students_sorted_by_grade:
    print(student)