import sys

if __name__ == '__main__':
    totalStudents = int(raw_input())
    students = {}

    for student in range(0, totalStudents):
        name = raw_input()
        grade = float(raw_input())
        students[name] = grade

    if len(students) == 2:
        print min(students)
        sys.exit()

    # Remove all occurences of minimum grade
    students = {
        name: grade
        for name, grade in students.items()
        if min(students.values()) != grade
    }

    # Store all occurences of minimum (second) grade
    students = {
        name for name, grade in students.items() if
        grade == min(students.values())
    }

    print '\n'.join(sorted(students))
