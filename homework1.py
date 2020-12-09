#Question 1

#Convert your program to accept user's input for the length variable and use
#the input to compute the area of a square

length = int(input("Please enter the length of square:"))
area = length * length
print(area)

#Question 2

#Create a programme that displays your name and complete mailing address
#formatted in an envelope address manner. Your program does not need to read
#any inut from the user.
#psuedocodes: Write a program that displays the following
#Your name
#Your address
#Your phone number

name = ("Chizoba Rita Enechukwu")
address = ("Plot 30/31, Area 8 OPIC Estate, Agbara, Ogun State")
phone_number = 2348134482616
print (name, address, phone_number, sep="\n")

#Question 3

#Using only the concept taught in class, write a program that accepts a
#user's name and prints it 10 times

name = input("Please enter your name:")
print(10 * (name +"\n"))
