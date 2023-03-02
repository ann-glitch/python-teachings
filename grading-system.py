# Write a sample school grading program to accept a student name, course and score
# and then output them.

studentName = input("What is your name?: ")
studentCourse = input("Can you name any one of the courses you took last semester?: ")
CourseScore = input("What was the score you got on the above mentioned course?: ")
CourseScore = int(CourseScore)

if CourseScore >= 80:
    print(studentName, "you got", CourseScore, "in", studentCourse, "and hence your grade is A")
elif CourseScore >= 75:
    print(studentName, "you got", CourseScore, "in", studentCourse, "and hence your grade is B+")
elif CourseScore >= 70:
    print(studentName, "you got", CourseScore, "in", studentCourse, "and hence your grade is B")
elif CourseScore >= 65:
    print(studentName, "you got", CourseScore, "in", studentCourse, "and hence your grade is C+")
elif CourseScore >= 60:
    print(studentName, "you got", CourseScore, "in", studentCourse, "and hence your grade is C")
elif CourseScore >= 55 :
    print(studentName, "you got", CourseScore, "in", studentCourse, "and hence your grade is D+")
elif CourseScore >= 50 :
    print(studentName, "you got", CourseScore, "in", studentCourse, "and hence your grade is D") 
else:
    print(studentName, "you got", CourseScore, "in", studentCourse, "and hence your grade is F. You need to sit up")    

                            
