import sys

if __name__ == '__main__':
    totalStudents = int( raw_input() )
    students = {}

    for student in range(0, totalStudents):
        studentName = raw_input()
        studentGrade = float( raw_input() )
        students[ studentName ] = studentGrade

    lowestGrade = min( students )

    print lowestGrade

    '''
    students = filter( lambda grade: grade != lowestGrade, students)
    

    secondLowestGrade = min( students )

    #print lambda studentName: stud
    '''
