#prints the sentence "Yes - Spathiphyllum is the best 
#prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
#prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
#Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!

phase= str(input("Digite a palavras: "))

if phase == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif phase == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not [input]!")