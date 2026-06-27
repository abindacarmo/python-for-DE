# here are the exampless
# number 1

number = [x**2 for x in range(1,6)]
print(number)

# number 2

numbers = [5, 10, 15, 20]

print([x*2 for x in numbers])

# number 3

names = ["alice", "bob", "charlie"]

print([namess.upper() for namess in names])

# number 4

words = ["python", "java", "go", "rust"]

print([len(wordss) for wordss in words])


# number 5

numeros = list(range(1,11))

print([z for z in numeros if z % 2 == 0])

# number 6

numeross = [1, 2, 3, 4, 5]

print(["Even" if a % 2 == 0 else  "Odd" for a in numeross])

# number 7

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print([x for y in matrix for x in y])


# number 8
numbers = [1, 2, 3, 4, 5]

print({x: x**2 for x in numbers})

# number 9

words = ["apple", "banana", "kiwi"]

print({names: len(names) for names in words})

# nubmer 10
numbers = list(range(1, 11))

print({x: x**2 for x in numbers if x % 2 == 0})
