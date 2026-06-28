# here are the exampless
# number 1

text = "     Python Programming     "

print(text.strip())

# number 2 

languages = "Python,Java,C++,Go,Rust"

print(languages.split())

# number 3 

sentence = "Learning Python is fun"
print(sentence.split(" "))


# number 4 

colors = ["Red", "Green", "Blue"]
print("-".join(colors))

# number 5 

letters = ['P', 'Y', 'T', 'H', 'O', 'N']
print("".join(letters))

# number 6 

name = "Abinda"
country = "Timor-Leste"

print("hello, my name is {} and I live in {}".format(name, country))

# number 7 

name = "Alice"
age = 22

print(f"{name} is {age} years old")

# number 8 

text = "    apple banana orange grape    "

print(text.strip().split())

# number 9

text = "Python,Java,C++,Rust"

result = text.split(",")
print(" | ".join(result))

# number 10 

text = "    python,is,awesome    "

result = text.strip().split(",")

print(" ".join(result))

# nubmer 11
student = "    Abinda,21,Computer Science,Timor-Leste    "

result_student = student.strip().split(",")

data = result_student

print("Name: ", data[0])
print("Age:", data[1])
print("Major:", data[2])
print("City:", data[3])

# number 12
tags = "python, data science, machine learning, sql"

final_result = []

result = tags.split(",")

for tag in result:
    hmm = tag.strip()
    results = hmm.replace(" ", "_")
    bla = f"#{results}"
    final_result.append(bla)

print(final_result)

    
    
