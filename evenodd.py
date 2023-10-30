# Input a number
number = int(input("Enter a number:"))

# Check if the number is greater than zero and print "Number is positive" if it is
if number > 0:
    print("Number is positive")

# Check if the number is less than zero and print "Number is negative" if it is
elif number < 0:
    print("Number is negative")

# If the number is not greater than zero and not less than zero, it must be zero
else:
    print("Number is zero")
