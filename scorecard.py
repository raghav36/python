import operator

# input student details
def get_student_details():
    student_details = {}
    total_students = int(input('Enter the total number of students'))
    if total_students <3:
        print('Total number of students cannot be less than 3')
    else:
        for i in range(0,total_students):
            student_name = str(input('Enter student name'))
            student_total_score = int(input('Enter student total score'))
            student_details[student_name] = student_total_score

    return student_details 

# rank 1 gets $500, rank 2 gets $300 and rank 3 gets $200
def awards_for_top_three_students(final_student_data):
    print('$500 awarded to {} for securing {}'.format(final_student_data[0][0], final_student_data[0][1]))
    print('$300 awarded to {} for securing {}'.format(final_student_data[1][0], final_student_data[1][1]))
    print('$200 awarded to {} for securing {}'.format(final_student_data[2][0], final_student_data[2][1]))

# scores greater than equal to 950 certificates of appreciation
def certificate_of_appreciation(final_ranking_of_students):
    for record in final_ranking_of_students:
        if record[1] >= 950:
            print("Congrats on your achievement {}".format(record[0]))

# final ranking of students and corresponding award
def appreciation_for_students(student_data):
    final_ranking_of_students = sorted(student_data.items(), key=operator.itemgetter(1), reverse=True)
    awards_for_top_three_students(final_ranking_of_students)
    certificate_of_appreciation(final_ranking_of_students)

student_data = get_student_details()
appreciation_for_students(student_data)
