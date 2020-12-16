# Homework
# Read more about if statement
# Implement option for B to compute the perimeter of the square
# Implement option AP, calculate both Area and Perimeter
# Implement for anything that is not A or B or AB let this end the program
# Create square2.py and do the homework there

#ANSWER

# Ask the user for username
username = input ("Enter Your Username: ")
# Display a welcome page
print ("Welcome", username)
# Ask the user to enter age
Age = int(input ("Please Enter Your Age: "))
# Ask the user for length of square
length = float(input ("Please enter the length of the square: "))
# Ask the user to select A or B for area or perimeter of square respectively
option = input("Enter A to calculate Area, B to calculate Perimeter or AB to calculate both Area and Perimeter: ")
# Caculate the area (A) and perimeter (B) using the input of the length
if option == "A":
    area = length * length
    print("Area: ",area)
elif option == "B":
    perimeter = 4 * length
    print ("Perimeter: ",perimeter)
elif option == "AB":
    area = length * length
    perimeter = 4 * length
    print("Area: ",area,"\n","Perimeter: ",perimeter)
else:
    exit()

#Answer 2
def factorial(x):
    if x==0:
        return 1
    else:
        return x * factorial (x-1)
x=int(input("Enter a number to compute factorial: "))
print ("Factorial of ",x," is: ",factorial(x))

#Answer 3

    
