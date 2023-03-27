# Write a sample school grading program to accept a student name, course and score
# and then output them.

student_name = input("What is your name?: ")
student_course= input("Can you name any one of the courses you took last semester?: ")
course_score = input("What was the score you got in the above mentioned course?: ")
course_score = int(course_score)

if course_score >= 80:
    print("Name:", student_name, "\nCourse:", student_course, "\nScore:", course_score, "\nGrade: A. Excellent.")
elif course_score >= 75:
    print("Name:", student_name, "\nCourse:", student_course, "\nScore:", course_score, "\nGrade: B+. Very good.")
elif course_score >= 70:
    print("Name:", student_name, "\nCourse:", student_course, "\nScore:", course_score, "\nGrade: B. Good.")
elif course_score >= 65:
    print("Name:", student_name, "\nCourse:", student_course, "\nScore:", course_score, "\nGrade: C+. Pass")
elif course_score >= 60:
    print("Name:", student_name, "\nCourse:", student_course, "\nScore:", course_score, "\nGrade: C. Pass")
elif course_score >= 55 :
    print("Name:", student_name, "\nCourse:", student_course, "\nScore:", course_score, "\nGrade: D+. Can do better.")
elif course_score >= 50 :
    print("Name:", student_name, "\nCourse:", student_course, "\nScore:", course_score, "\nGrade: D. Can do better.") 
elif course_score < 50:
    print("Name:", student_name, "\nCourse:", student_course, "\nScore:", course_score, "\nGrade: F. You need to sit up.")
else:
    print("Invalid input")        

   
                        