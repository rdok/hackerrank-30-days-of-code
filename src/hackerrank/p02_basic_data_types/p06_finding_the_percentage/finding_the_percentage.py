if __name__ == '__main__':
    total_students = int(raw_input())
    students = {}

    for _ in range(total_students):
        line = raw_input().split()
        name, scores = line[0], map(float, line[1:])
        students[name] = scores

    query_name = raw_input()

    grades = students[query_name]

    print "%.2f" % (sum(grades) / float(len(grades)))
