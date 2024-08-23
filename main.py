import datetime
#  # Calculate your age based on the current year and your birth year.

birthYear:int=int(input("Please enter your age : "))
currentYear:int=datetime.datetime.now().year
print(f"Your age is : {currentYear-birthYear}")

#  #  - Write a program that calculates the area of a rectangle using length and width variables.

lenghth:int=int(input("enter lenghth of rectangle : "))
width:int=int(input("enter width of the rectangle : "))
print(f"the Area of rectangle is : {lenghth*width}")

# #  - Write a program that calculates the area of a circle.

radius:int= int(input("Enter the radius of the circle : "))
area:int= 3.14*radius
print(f"The Radius of circle is : {area}")


# #  - Write a program that calculates the area of the cube.

side:int = int(input("Enter the one side lenghth of cube : "))
print(f"Area of cube is : {6*side**2}")

# #  - Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.

temp:int= int(input ("Enter temperature in Farenheit : "))
temp1:int= ((32*temp-32)* 5/9)
print(f"the temperature in Celsius is : {temp1}")

temp= int(input ("Enter temperature in Celsius : "))
temp1 =((9/5*temp)+32)
print(f"the temperature in Fahrenheit is : {temp1}")

# #  - Convert a given number of seconds into minutes and seconds using variables.

sec:int= int(input("Enter time in seconds : "))
mins:int=sec//60
seconds:int=sec%60
print(f"the minutes are :{mins} and  the seconds are : {seconds}")

# #  - Write a program that calculates the percentage.

value:int= int(input("Enter the Value : "))
percentage:int= int(input("Enter the percentage value : "))
print(f"the percentage is: {value/100*percentage}")


#Write a program that calculates the BMI using height and weight variables

height:int= int(input("Enter the height of person in meters: "))
weight:int= int(input("Enter the weight of person in kgs: "))
print(f"the BMI of the person is : {weight/(height*height)}")


#write a program that calculates the volume of a cylinder using the formula

radius:int= int(input("Enter the radius of the circle : "))
height:int=int(input("Enter the height of the cylinder : "))
area:int= 3.14*(radius*radius)*height
print(f"The Area of cylinder is : {area}")


