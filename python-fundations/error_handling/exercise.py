# here are the examples
# number 1

try:
    number = int(input("input dados: "))
    print(number)
except ValueError:
    print("invalid input")

# number 2 

try:
    age = int(input("input your age: "))
    print(age)

except ValueError:
    print("Please enter a valid number.")


# number 3 

try: 
    y = int(input("input number: "))
    z = 100 / y
    print(z)

except ZeroDivisionError:
    print("Cannot divide by zero.")


# number 4 

try:
    number = int(input("input number: "))
    print(number)
except ValueError as e:
    print(e)


# number 5 

try:
    number = int(input("input number: "))
    print(number)

except ValueError:
    print("Invalid")

else:
    print("Success")

# number 6 
try:
    file = open("data.csv")
except FileNotFoundError:
    print("File not Found")

finally:
    print("Program Success")

try:
    age = int(input("input your age: "))
    print(age)
except ValueError:
    print("invalid input")

finally:
    print("Program Success")

# number 7

age = int(input("input your age: "))
if age < 0:
    raise ValueError("age cannot be negative")

# number 8
class InvalidAgeError(Exception):
    pass

age = int(input("your age: "))
if age < 0:
    raise InvalidAgeError("Age cannot be negative.")


# number 9
class PasswordError(Exception):
    pass

password = input("your password: ")
if len(password) < 8:
    raise PasswordError("Password must contain at least 8 characters.")

else:
    print("Registration successful.")


# number 10 
try:
    y = int(input("number 1: "))
    x = 100 / y 
    print(x)
except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid number!")

finally:
    print("Program finished.")

