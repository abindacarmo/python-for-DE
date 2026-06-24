# Python Functions

## English Version

# Introduction

A function is a reusable block of code designed to perform a specific task. Functions help make code more organized, readable, and maintainable.

Instead of writing the same code multiple times, you can place it inside a function and call it whenever needed.

---

# Creating a Function with `def`

Functions are created using the `def` keyword.

## Syntax

```python
def function_name():
    # code block
```

## Example

```python
def greet():
    print("Hello, World!")
```

Calling the function:

```python
greet()
```

Output:

```text
Hello, World!
```

### Explanation

* `def` defines a function.
* `greet` is the function name.
* `()` contains parameters.
* `:` starts the function body.

---

# Parameters and Arguments

Parameters are variables listed in a function definition.

Arguments are the actual values passed to the function.

## Example

```python
def greet(name):
    print(f"Hello, {name}")
```

Calling the function:

```python
greet("Abinda")
```

Output:

```text
Hello, Abinda
```

### Explanation

* `name` is a parameter.
* `"Abinda"` is an argument.

---

# The `return` Statement

The `return` keyword sends a value back from a function.

## Example

```python
def add(a, b):
    return a + b
```

Using the returned value:

```python
result = add(5, 3)

print(result)
```

Output:

```text
8
```

### Why Use `return`?

Without `return`, the result cannot easily be reused.

```python
def multiply(a, b):
    return a * b

x = multiply(2, 4)

print(x + 10)
```

Output:

```text
18
```

---

# Default Parameters

A parameter can have a default value.

## Example

```python
def greet(name="Friend"):
    print(f"Hello, {name}")
```

Calling without an argument:

```python
greet()
```

Output:

```text
Hello, Friend
```

Calling with an argument:

```python
greet("Abinda")
```

Output:

```text
Hello, Abinda
```

---

# Multiple Parameters

Functions can accept multiple parameters.

## Example

```python
def profile(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")
```

Calling the function:

```python
profile("Abinda", 21)
```

Output:

```text
Name: Abinda
Age: 21
```

---

# `*args`

Sometimes we do not know how many arguments will be passed.

`*args` allows a function to accept a variable number of positional arguments.

## Example

```python
def show_numbers(*args):
    print(args)
```

Calling the function:

```python
show_numbers(1, 2, 3, 4)
```

Output:

```text
(1, 2, 3, 4)
```

### Important Note

`args` is stored as a tuple.

## Practical Example

```python
def total(*args):
    result = 0

    for number in args:
        result += number

    return result
```

Calling the function:

```python
print(total(1, 2, 3))
print(total(10, 20, 30, 40))
```

Output:

```text
6
100
```

---

# `**kwargs`

`**kwargs` allows a function to accept a variable number of keyword arguments.

Keyword arguments are stored as a dictionary.

## Example

```python
def profile(**kwargs):
    print(kwargs)
```

Calling the function:

```python
profile(
    name="Abinda",
    age=21,
    major="Informatics"
)
```

Output:

```python
{
    'name': 'Abinda',
    'age': 21,
    'major': 'Informatics'
}
```

### Accessing Values

```python
def profile(**kwargs):
    print(kwargs["name"])
```

Calling the function:

```python
profile(name="Abinda")
```

Output:

```text
Abinda
```

---

# Combining Parameters, `*args`, and `**kwargs`

You can use all of them together.

## Example

```python
def information(name, *args, **kwargs):
    print("Name:", name)
    print("Args:", args)
    print("Kwargs:", kwargs)
```

Calling the function:

```python
information(
    "Abinda",
    21,
    "Informatics",
    city="Dili",
    country="Timor-Leste"
)
```

Output:

```text
Name: Abinda
Args: (21, 'Informatics')
Kwargs: {'city': 'Dili', 'country': 'Timor-Leste'}
```

---

# Parameter Order

The correct order is:

```python
def function_name(
    normal_parameter,
    *args,
    **kwargs
):
    pass
```

Example:

```python
def example(a, b=10, *args, **kwargs):
    pass
```

---

# Summary

| Concept            | Description                             |
| ------------------ | --------------------------------------- |
| `def`              | Creates a function                      |
| `return`           | Returns a value                         |
| Parameters         | Variables inside a function             |
| Arguments          | Values passed to a function             |
| Default Parameters | Parameters with default values          |
| `*args`            | Variable positional arguments (tuple)   |
| `**kwargs`         | Variable keyword arguments (dictionary) |

---

# Indonesian Version

# Pendahuluan

Function adalah blok kode yang dapat digunakan kembali untuk melakukan tugas tertentu. Function membantu membuat kode lebih rapi, mudah dibaca, dan mudah dipelihara.

Daripada menulis kode yang sama berulang kali, kita cukup membuat function dan memanggilnya kapan saja diperlukan.

---

# Membuat Function dengan `def`

Function dibuat menggunakan keyword `def`.

## Sintaks

```python
def nama_function():
    # blok kode
```

## Contoh

```python
def sapa():
    print("Halo Dunia!")
```

Memanggil function:

```python
sapa()
```

Output:

```text
Halo Dunia!
```

### Penjelasan

* `def` digunakan untuk membuat function.
* `sapa` adalah nama function.
* `()` berisi parameter.
* `:` menandakan awal blok function.

---

# Parameter dan Argument

Parameter adalah variabel yang didefinisikan di dalam function.

Argument adalah nilai yang dikirim saat function dipanggil.

## Contoh

```python
def sapa(nama):
    print(f"Halo, {nama}")
```

Pemanggilan:

```python
sapa("Abinda")
```

Output:

```text
Halo, Abinda
```

### Penjelasan

* `nama` adalah parameter.
* `"Abinda"` adalah argument.

---

# Statement `return`

Keyword `return` digunakan untuk mengembalikan nilai dari sebuah function.

## Contoh

```python
def tambah(a, b):
    return a + b
```

Penggunaan:

```python
hasil = tambah(5, 3)

print(hasil)
```

Output:

```text
8
```

### Mengapa Menggunakan `return`?

Karena nilai yang dihasilkan dapat digunakan kembali.

```python
def kali(a, b):
    return a * b

x = kali(2, 4)

print(x + 10)
```

Output:

```text
18
```

---

# Default Parameters

Parameter dapat memiliki nilai bawaan.

## Contoh

```python
def sapa(nama="Teman"):
    print(f"Halo, {nama}")
```

Pemanggilan tanpa argument:

```python
sapa()
```

Output:

```text
Halo, Teman
```

Pemanggilan dengan argument:

```python
sapa("Abinda")
```

Output:

```text
Halo, Abinda
```

---

# Multiple Parameters

Function dapat menerima lebih dari satu parameter.

## Contoh

```python
def biodata(nama, umur):
    print(f"Nama: {nama}")
    print(f"Umur: {umur}")
```

Pemanggilan:

```python
biodata("Abinda", 21)
```

Output:

```text
Nama: Abinda
Umur: 21
```

---

# `*args`

Digunakan ketika jumlah argument yang diterima tidak diketahui.

## Contoh

```python
def tampilkan_angka(*args):
    print(args)
```

Pemanggilan:

```python
tampilkan_angka(1, 2, 3, 4)
```

Output:

```text
(1, 2, 3, 4)
```

### Catatan Penting

`args` disimpan dalam bentuk tuple.

## Contoh Praktis

```python
def total(*args):
    hasil = 0

    for angka in args:
        hasil += angka

    return hasil
```

Pemanggilan:

```python
print(total(1, 2, 3))
print(total(10, 20, 30, 40))
```

Output:

```text
6
100
```

---

# `**kwargs`

Digunakan untuk menerima banyak keyword argument.

Data disimpan dalam bentuk dictionary.

## Contoh

```python
def biodata(**kwargs):
    print(kwargs)
```

Pemanggilan:

```python
biodata(
    nama="Abinda",
    umur=21,
    jurusan="Informatika"
)
```

Output:

```python
{
    'nama': 'Abinda',
    'umur': 21,
    'jurusan': 'Informatika'
}
```

### Mengakses Nilai

```python
def biodata(**kwargs):
    print(kwargs["nama"])
```

Pemanggilan:

```python
biodata(nama="Abinda")
```

Output:

```text
Abinda
```

---

# Menggabungkan Parameter, `*args`, dan `**kwargs`

## Contoh

```python
def informasi(nama, *args, **kwargs):
    print("Nama:", nama)
    print("Args:", args)
    print("Kwargs:", kwargs)
```

Pemanggilan:

```python
informasi(
    "Abinda",
    21,
    "Informatika",
    kota="Dili",
    negara="Timor-Leste"
)
```

Output:

```text
Nama: Abinda
Args: (21, 'Informatika')
Kwargs: {'kota': 'Dili', 'negara': 'Timor-Leste'}
```

---

# Urutan Parameter

Urutan yang benar:

```python
def nama_function(
    parameter_biasa,
    *args,
    **kwargs
):
    pass
```

Contoh:

```python
def contoh(a, b=10, *args, **kwargs):
    pass
```

---

# Ringkasan

| Konsep            | Penjelasan                                     |
| ----------------- | ---------------------------------------------- |
| `def`             | Membuat function                               |
| `return`          | Mengembalikan nilai                            |
| Parameter         | Variabel dalam function                        |
| Argument          | Nilai yang dikirim ke function                 |
| Default Parameter | Parameter dengan nilai bawaan                  |
| `*args`           | Menampung banyak argument (tuple)              |
| `**kwargs`        | Menampung banyak keyword argument (dictionary) |
|                   |                                                |
