quiz_dictionary = {}
user_scores = {}  # Create a dictionary to store user scores

while True:
    print("\nMenu:")
    print("1. Add Question")
    print("2. Take Quiz")
    print("3. View Scores")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        question = input("Enter a question: ")
        answer = input("Please enter the correct answer: ")
        quiz_dictionary[question] = answer
        print("Question added successfully!")

    elif choice == "2":
        number1 = int(input("Select the first number (2/3/5/4): "))
        number2 = int(input("Select the second number (1/2/5/8): "))
        number = number1 + number2
        if number > 10:
            print("Sorry! Please select numbers from the given list.")
        else:
            # You can add quiz logic here
            user_answer = input("Enter your answer: ")
            if user_answer == str(number):
                print("Your answer is correct!")
            else:
                print("Your answer is incorrect!")

    elif choice == "3":
        # Display user scores
        for user, score in user_scores.items():
            print(f"{user}: {score}")

    elif choice == "4":
        print("Program exit successfully!")
        break  # Exit the loop

    else:
        print("Thanks for taking part in this quiz. Have a nice day!")

# End of the program
