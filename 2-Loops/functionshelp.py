# function to find averge marks
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks


# calculate the grade and return it
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = "A"
    elif average_marks >= 60:
        grade = "B"
    elif average_marks >= 50:
        grade = "C"
    elif average_marks >= 40:
        grade = "D"
    else:
        grade = "F"
    return grade


marks = [55, 64, 75, 80, 34]

average_marks = find_average_marks(marks)
print("Your average is: ", average_marks)


grade = compute_grade(average_marks)
print("Your make is", grade)
