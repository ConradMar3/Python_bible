#Ask user for name
name = input("What is your name?: ")

#Ask user for age
age = input("How old are you?: ")

#City
city = input("Where do you live?: ")

#Love doing
love = input("What do you love doing?: ")

#Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love)

#Print output
print(output)
