# example number 1

# you can uncomment this example bellow

# def total(*args):
#     resultado = 0

#     for numero in args:
#         resultado += numero

#     return resultado


# n1 = int(input("input numeru: "))
# n2 = int(input("input numeru: "))

# print(total(n1, n2**2))

# basic example 1

def greating(name):
    return f"Halooo {name}"


print(greating("Abinda"))


# example 2

def plus(x, y):
    result = 0

    for i in x, y:
        result += i

    return result

print(plus(5, 3))


# example 3

def from_city(city="Timor-Leste"):
    print(f"Welcome to {city}")


from_city()
from_city("Indonesia")

# example 4

def total(*args):
    result = 0

    for i in args:
        result += i
    
    return result

print(total(1,2,3,4))

# example 4

def biodata(**kwargs):
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])
    print("Major:", kwargs["major"])

biodata(
    name="Abinda",
    age=22,
    major="Informatics"
)


# example 5

def student_information(name, age, *args, **kwargs):
    print("Name: ",name)
    print("Hobbies: ", args)
    print("Information: ", kwargs)


student_information(
    "Abinda",
    21,
    "Coding",
    "Gaming",
    live="Dili",
    city="Timor-Leste"
)




