# List & Dictionary Comprehensions in Python

---

# Part 1 — English Version

## What is Comprehension?

A **comprehension** is a short and elegant way to create a new collection (such as a list, dictionary, or set) from an existing iterable.

Instead of writing multiple lines using a `for` loop, Python allows us to write everything in a single readable line.

Think of comprehension as:

> "Create a new collection by transforming each item from another collection."

Comprehensions make your code:

- Shorter
- Cleaner
- Easier to read
- More Pythonic

---

# Why Use Comprehensions?

Without comprehension:

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)
```

Output

```python
[1, 4, 9, 16, 25]
```

With List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

Output

```python
[1, 4, 9, 16, 25]
```

The result is exactly the same, but the code is much shorter.

---

# List Comprehension Syntax

General syntax

```python
[new_value for item in iterable]
```

Example

```python
numbers = [1, 2, 3, 4, 5]

double = [number * 2 for number in numbers]

print(double)
```

Output

```python
[2, 4, 6, 8, 10]
```

Explanation

```
number * 2      -> new value
for number      -> loop variable
in numbers      -> iterable
```

---

# Example 1 — Square Numbers

Traditional way

```python
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number ** 2)

print(result)
```

Using comprehension

```python
numbers = [1, 2, 3, 4, 5]

result = [number ** 2 for number in numbers]

print(result)
```

Output

```python
[1, 4, 9, 16, 25]
```

---

# Example 2 — Convert Strings to Uppercase

```python
names = ["john", "alice", "bob"]

uppercase = [name.upper() for name in names]

print(uppercase)
```

Output

```python
['JOHN', 'ALICE', 'BOB']
```

---

# Example 3 — Get String Length

```python
words = ["python", "java", "go"]

lengths = [len(word) for word in words]

print(lengths)
```

Output

```python
[6, 4, 2]
```

---

# List Comprehension with if

You can filter items using an `if` statement.

Syntax

```python
[new_value for item in iterable if condition]
```

Example

```python
numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
```

Output

```python
[2,4,6,8,10]
```

Only even numbers are included.

---

# Example — Odd Numbers

```python
numbers = [1,2,3,4,5,6]

odd = [number for number in numbers if number % 2 != 0]

print(odd)
```

Output

```python
[1,3,5]
```

---

# Conditional Expression (if...else)

Syntax

```python
[value_if_true if condition else value_if_false for item in iterable]
```

Example

```python
numbers = [1,2,3,4,5]

labels = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print(labels)
```

Output

```python
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

# Nested List Comprehension

Example

```python
matrix = [
    [1,2],
    [3,4],
    [5,6]
]

flatten = [number for row in matrix for number in row]

print(flatten)
```

Output

```python
[1,2,3,4,5,6]
```

Equivalent to

```python
flatten = []

for row in matrix:
    for number in row:
        flatten.append(number)
```

---

# Dictionary Comprehension

Dictionary comprehension creates dictionaries in one line.

Syntax

```python
{
    key: value
    for item in iterable
}
```

---

# Example 1

```python
numbers = [1,2,3,4,5]

squares = {number: number ** 2 for number in numbers}

print(squares)
```

Output

```python
{
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
```

---

# Example 2

```python
names = ["Alice", "Bob", "Charlie"]

length = {name: len(name) for name in names}

print(length)
```

Output

```python
{
    'Alice':5,
    'Bob':3,
    'Charlie':7
}
```

---

# Dictionary Comprehension with if

```python
numbers = [1,2,3,4,5,6]

even_square = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_square)
```

Output

```python
{
    2:4,
    4:16,
    6:36
}
```

---

# When Should You Use Comprehensions?

Use comprehensions when:

✅ Creating a new list

✅ Creating a new dictionary

✅ Filtering data

✅ Transforming data

Avoid comprehensions when:

❌ The logic becomes too complex.

If the comprehension is difficult to read, use a normal `for` loop instead.

Readable code is always better.

---

# Traditional Loop vs Comprehension

Traditional

```python
result = []

for x in numbers:
    result.append(x * 2)
```

Comprehension

```python
result = [x * 2 for x in numbers]
```

Both are correct.

The second version is shorter and more Pythonic.

---

# Summary

List Comprehension

```python
[value for item in iterable]
```

With filter

```python
[value for item in iterable if condition]
```

With if...else

```python
[value_if_true if condition else value_if_false for item in iterable]
```

Dictionary Comprehension

```python
{
    key: value
    for item in iterable
}
```

---

# Part 2 — Penjelasan Bahasa Indonesia

## Apa itu Comprehension?

Comprehension adalah cara singkat untuk membuat **list**, **dictionary**, atau koleksi lainnya hanya dalam satu baris kode.

Daripada menggunakan beberapa baris `for` loop, Python menyediakan sintaks yang lebih ringkas dan mudah dibaca.

Misalnya, kita ingin membuat list baru yang berisi kuadrat dari setiap angka.

Tanpa comprehension:

```python
hasil = []

for angka in [1,2,3]:
    hasil.append(angka ** 2)
```

Dengan comprehension:

```python
hasil = [angka ** 2 for angka in [1,2,3]]
```

Hasilnya sama, tetapi kode menjadi jauh lebih singkat.

---

## Struktur List Comprehension

```python
[nilai_baru for item in iterable]
```

Artinya:

- `nilai_baru` → nilai yang ingin dimasukkan ke list baru.
- `item` → variabel sementara.
- `iterable` → objek yang dapat diulang (list, tuple, string, dll).

Contoh:

```python
angka = [1,2,3]

hasil = [x * 2 for x in angka]
```

Prosesnya:

```
1 × 2 = 2
2 × 2 = 4
3 × 2 = 6
```

Hasil:

```python
[2,4,6]
```

---

## Filter menggunakan if

Comprehension juga bisa menyaring data.

Contoh:

```python
angka = [1,2,3,4,5,6]

genap = [x for x in angka if x % 2 == 0]
```

Artinya:

> Masukkan hanya angka yang habis dibagi 2.

Hasil:

```python
[2,4,6]
```

---

## if...else di dalam Comprehension

Kita juga bisa memberikan nilai berbeda sesuai kondisi.

```python
angka = [1,2,3,4]

hasil = [
    "Genap" if x % 2 == 0 else "Ganjil"
    for x in angka
]
```

Hasil:

```python
['Ganjil', 'Genap', 'Ganjil', 'Genap']
```

---

## Nested List Comprehension

Nested comprehension digunakan jika kita memiliki data bertingkat.

Misalnya:

```python
matrix = [
    [1,2],
    [3,4]
]
```

Menjadi:

```python
[1,2,3,4]
```

Menggunakan:

```python
[number for row in matrix for number in row]
```

Cara kerjanya sama seperti dua `for` yang bersarang.

---

## Dictionary Comprehension

Jika List Comprehension menghasilkan list, maka Dictionary Comprehension menghasilkan dictionary.

Contoh:

```python
angka = [1,2,3]

hasil = {
    x: x ** 2
    for x in angka
}
```

Hasil:

```python
{
    1:1,
    2:4,
    3:9
}
```

---

## Kapan Menggunakan Comprehension?

Gunakan comprehension ketika:

- ingin membuat list baru,
- ingin membuat dictionary baru,
- ingin memfilter data,
- ingin mengubah data menjadi bentuk baru.

Namun, jika logikanya terlalu rumit dan sulit dipahami, lebih baik gunakan `for` loop biasa agar kode tetap mudah dibaca.

---

# Kesimpulan

List Comprehension adalah cara singkat untuk membuat list baru.

Dictionary Comprehension adalah cara singkat untuk membuat dictionary baru.

Sintaks yang paling sering digunakan:

List

```python
[x for x in data]
```

Dengan filter

```python
[x for x in data if kondisi]
```

Dengan if...else

```python
["Genap" if x % 2 == 0 else "Ganjil" for x in data]
```

Dictionary

```python
{
    x: x ** 2
    for x in data
}
```

Comprehension membuat kode menjadi lebih ringkas, lebih bersih, dan merupakan salah satu gaya penulisan Python yang paling sering digunakan oleh programmer profesional.
