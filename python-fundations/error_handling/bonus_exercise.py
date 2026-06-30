# number 1

try:
    file = open("exercise.py")
    print(file)
except FileNotFoundError:
    print("File not found.")
else:
    print("File opened successfully.")
finally:
    print("End of program.")

# number 2

try:
    file = open("example.py")
    print(file)
except FileNotFoundError:
    print("File not found.")
else:
    print("File opened successfully.")
finally:
    print("End of program.")
