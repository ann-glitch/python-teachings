# 1. Determine the temperature of a room and decide by showing "the room is cold" if the temperature is less than
# or equal to 16 otherwise show the message " the room is warm"

temperature = input("What is the current room temperature?: ")
temperature = int(temperature)

if temperature <= 16:
    print("The room is cold")
else:
    print("The room is warm")    

# 2. Ask a user to indicate his name and based on the feedback received, decide and show if the person is called "Nana"
# the message "you are Nana and your name in akan means king or chief but if you were a Ga, you would be called "Nii or Naa."
# Otherwise if the person's name isn't nana, show his original name includling the message "welcome to the python class."

name = input("What is your name?: ")

if name == "Nana":
    print("You are", name, "and your name in Akan means 'king' or 'chief' but if you were a Ga, you would be called 'Nii or Naa'")
else: 
    print(name, "welcome to the python class!")    