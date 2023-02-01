def gradingStudents(grades):
    output = []
    for grade in grades:
        if grade < 38:
            output.append(grade)
        else:
            check = 5 - (grade % 5)
            if check < 3:
                rdd = grade + check
                output.append(rdd)
            else:
                output.append(grade)
    return output


# test code
grades = [73, 67, 38, 33]
print(gradingStudents(grades))  # [75, 67, 40, 33]
