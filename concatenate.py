# Using atleast two ways in python concatenation, write a python code to show your full name.

# first way (using the join method)
firstName = "Ann"
lastName = "Augustine"
fullName = " ".join([firstName, lastName])

print(fullName)


# second way (using the plus operator)
print("Ann" + " " + "Augustine")


# write atleast two different ways to concatenate the following:
# i. "Hello World"
# ii. "I  will become a pro pythonista"

# using the format method
print(f'{"Hello"} {"World"}')


# using the += operator
affirmation = "I will become a"
affirmation += " pro pythonista"

print(affirmation)