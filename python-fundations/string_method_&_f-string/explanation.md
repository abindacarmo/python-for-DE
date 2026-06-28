# String Methods & F-Strings in Python

---

## ENGLISH VERSION

### 1. Introduction to String Methods
String methods are built-in functions in Python used to manipulate and work with text (strings). Strings are sequences of characters, and Python provides many useful methods to handle them easily.

---

### 2. `strip()` Method
The `strip()` method removes whitespace (or specified characters) from the beginning and end of a string.

Example:
```python
text = "   Hello World   "
print(text.strip())
```

Output:
```
Hello World
```

---

### 3. `split()` Method
The `split()` method breaks a string into a list based on a separator.

Example:
```python
text = "apple,banana,orange"
print(text.split(","))
```

Output:
```
['apple', 'banana', 'orange']
```

---

### 4. `join()` Method
The `join()` method combines elements of a list into a single string.

Example:
```python
fruits = ['apple', 'banana', 'orange']
print(", ".join(fruits))
```

Output:
```
apple, banana, orange
```

---

### 5. String Formatting

#### a. `format()` method
Used to insert values into a string.

```python
name = "Abinda"
age = 21

print("My name is {} and I am {} years old".format(name, age))
```

Output:
```
My name is Abinda and I am 21 years old
```

---

#### b. f-Strings (Recommended)
f-strings are a modern and easier way to format strings.

```python
name = "Abinda"
age = 21

print(f"My name is {name} and I am {age} years old")
```

Output:
```
My name is Abinda and I am 21 years old
```

---

### 6. Summary
- `strip()` → removes spaces
- `split()` → converts string into list
- `join()` → converts list into string
- `format()` → inserts values into string
- `f-string` → modern way to format strings

---
  
## VERSÃO EM BAHASA INDONESIA

### 1. Pengantar String Methods
String methods adalah fungsi bawaan Python yang digunakan untuk memanipulasi teks (string). String adalah kumpulan karakter, dan Python menyediakan banyak metode untuk memudahkan pengolahan teks.

---

### 2. `strip()` Method
`strip()` digunakan untuk menghapus spasi atau karakter tertentu di awal dan akhir string.

Contoh:
```python
text = "   Hello World   "
print(text.strip())
```

Hasil:
```
Hello World
```

---

### 3. `split()` Method
`split()` digunakan untuk memecah string menjadi list berdasarkan pemisah.

Contoh:
```python
text = "apel,jeruk,pisang"
print(text.split(","))
```

Hasil:
```
['apel', 'jeruk', 'pisang']
```

---

### 4. `join()` Method
`join()` digunakan untuk menggabungkan elemen list menjadi string.

Contoh:
```python
buah = ['apel', 'jeruk', 'pisang']
print(", ".join(buah))
```

Hasil:
```
apel, jeruk, pisang
```

---

### 5. String Formatting

#### a. `format()` method
Digunakan untuk memasukkan nilai ke dalam string.

```python
nama = "Abinda"
umur = 21

print("Nama saya {} dan umur saya {}".format(nama, umur))
```

Hasil:
```
Nama saya Abinda dan umur saya 21
```

---

#### b. f-Strings (Lebih direkomendasikan)
f-string adalah cara modern dan lebih mudah untuk formatting string.

```python
nama = "Abinda"
umur = 21

print(f"Nama saya {nama} dan umur saya {umur}")
```

Hasil:
```
Nama saya Abinda dan umur saya 21
```

---

### 6. Ringkasan
- `strip()` → menghapus spasi
- `split()` → mengubah string jadi list
- `join()` → menggabungkan list jadi string
- `format()` → memasukkan nilai ke string
- `f-string` → cara modern formatting string

