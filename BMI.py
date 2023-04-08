print("Welcome to the BMI Tracking app! This app is designed to help you calculate your body mass.")
print("\n-------------------------")

while True:
    #input functionality
    name = input("Please enter your name: ").upper()
    age = int(input("How old are you?: "))
    weight = float(input("How much do you weigh?: "))
    print("Please enter your height in meters.")
    height = float(input("What's your height?: "))

    # calculating for the BMI
    BMI = round(weight / height ** 2, 1)

    print("-------------------------")


    # logic
    if BMI <= 18.4:
        print("Name:", name, "\nAge:", age, "\nWeight:", weight,"kg", "\nHeight:", height,"m", "\nBMI:", BMI, "\nStatus: Underweight",
               "\nAdvice: Please consider eating food high in protein and carbohydrate.")
    elif BMI > 18.4 and BMI <= 24.9: 
        print("Name:", name, "\nAge:", age, "\nWeight:", weight,"kg", "\nHeight:", height,"m", "\nBMI:", BMI, "\nStatus: Normal", 
              "\nAdvice: You are fit. Keep it up!" )
    elif BMI > 24.9 and BMI <= 39.9: 
        print("Name:", name, "\nAge:", age, "\nWeight:", weight,"kg", "\nHeight:", height,"m", "\nBMI:", BMI, "\nStatus: Overweight", 
              "\nAdvice: Please consider exercising from time to time.")
    else:
        print("Name:", name, "\nAge:", age, "\nWeight:", weight,"kg", "\nHeight:", height,"m", "\nBMI:", BMI, "\nStatus: Obese",
               "\nAdvice: Please exercise more and seek medical advice also." )  
    
   #prompt user to restart
    restart = input("Do you want to restart the process? (y/n): ")

    if restart == "y":
        continue

    elif restart == "n":
        print("\n----------------------")
        print("Thank you for using this app. Do have a nice day.")
        break

    else:
        print("Invalid input. Please enter 'y' or 'n'") 