print("Example number 1")

data = {
    "name": "abinda",
    "age": "twenty two"
}

result = {key: value.upper() for key, value in data.items()}

print(result)


print("example number 2")

print([x for x in range(5)])

print("example number 3")

print([x for x in range(10) if x % 3 == 0])

print("example number 4")

print([triple**2 for triple in range(5)])

print("example number 5")

print([x for x in range(1, 11) if x % 2 != 0])

print("example number 6")

print([x for x in range(1, 11) if x % 2 == 0])

print("example number 7")

print([x for x in range(20) if x % 2 == 0 and x % 3 == 0])


# example key: value
print("========")
print("example key: value")

print({x: x**2 for x in range(5)})


print("example number 2")

keys = ['a', 'b', 'c']
values = [1, 2, 3]

print({key: values for key, values in zip(keys, values)})


# example key: value
print("========")
print("example filter & strip")

records = [
    {"id": 1, "name": "Joao", "age": 17},
    {"id": 2, "name": "Maria", "age": 25},
    {"id": 3, "name": "Carlos", "age": 16},
    {"id": 4, "name": "Rosa", "age": 30},
]

print([{"id": r["id"], "name": r["name"]} for r in records if r["age"]  >= 18])


print("example number 2")

raw = {" Email ": "  ABINDA@TEST.COM  ", "Phone_Number ": " 7723456 "}

print({key.lower().strip(): value.lower().strip() for key, value in raw.items()})


print("generator expression")
import sys

list_comp = [x for x in range(1000)]
gen_exp = (x for x in range(1000))

print(sys.getsizeof(list_comp))
print(sys.getsizeof(gen_exp))