# Insert marks obtained in an exam
marks = int(input("Enter a number:"))

# Check if marks are greater than or equal to 90, assign "A+"
if marks >= 90:
    print("A+")
    print("congratulations,You are the topper of the year")
# Check if marks are greater than or equal to 80, assign "A"
elif marks >= 80:
    print("A")
    print("well done, you perform well,next time work more")
# Check if marks are greater than or equal to 70, assign "B+"
elif marks >= 70:
    print("B+")
    print("well done")
# Check if marks are greater than or equal to 60, assign "B"
elif marks >= 60:
    print("B")
# Check if marks are greater than or equal to 50, assign "C+"
elif marks >= 50:
    print("C+")
# Check if marks are greater than or equal to 40, assign "C"
elif marks >= 40:
    print("C")
# Check if marks are less than 40, assign "FAIL"
else:
    print("FAIL")
