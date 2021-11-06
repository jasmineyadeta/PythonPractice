# function to find average marks
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_mark = sum_of_marks/total_subjects
    return average_mark

# function to calculate grade and return it
def grading_scale(average_mark):
    if average_mark >= 80:
        grade = "A"
    elif average_mark >= 60 and average_mark < 80:
        grade = "B"
    elif average_mark >= 50 and average_mark < 60:
        grade = "C"
    else:
        grade = "F"
    return(grade)

marks = [55,64, 75, 80, 65, 99, 50]
average_marks = find_average_marks(marks)
print ("Your average mark is:", average_marks)
grade = grading_scale(average_marks)
print ("Your grade is:", grade)
