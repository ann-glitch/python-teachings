# Write 5 prompt statements to ask about favorite word, second favorite word, favorite personality
# in the world, name of pets and favorite body parts.

# favWord = input("What is your favorite word?: ")
# secondFavWord = input("What is your second favorite word?: ")
# favPersonality = input("What is your favorite personality?: ")
# nameOfPets = input("What is the name of your pet?: ")
# favBodyPart = input("What is your favorite body part?: ")

# message = "Hello it's been nice knowing you. Your favorite word is " + favWord + " and your second favorite word is " + secondFavWord + " I love your favorite personality which is " + favPersonality + " and your lovely pet name which is " + nameOfPets +  " and finally your favorite body part which is " + favBodyPart
# print(message)


# prompt a user to indicate the number of books read in a month and based on that deduce the number of books he reads in a year.
# numberOfBooksRead = input("How many books do you read in a month?: ")
# answer = int(numberOfBooksRead) * 12
# print("You will read", answer, "books in a year." )

#second
# numberOfBooksRead = input("How many books do you read in a month?: ")
# numberOfBooksRead = int(numberOfBooksRead) 
# print(numberOfBooksRead * 12)

# third
# numberOfBooksRead = int(input("How many books do you read in a month?: "))
# print(numberOfBooksRead * 12)


# ASSIGNMENT
# prompt someone to indicate the number of hours he/she works in a month. Also require from the person to indicate
# his/her rates per hour then based on that deduce his/her salary for the (a) month and (b) the year.

hoursWorked = input("What is the number of hours you work in a month?: ")
hoursWorked = int(hoursWorked)
ratePerHour = input("What is your rate per hour?: ")
ratePerHour = int(ratePerHour)

monthlySalary =  hoursWorked * ratePerHour

print("Your monthly salary is", monthlySalary, "cedis and your annual salary is", monthlySalary * 12, "cedis.")

