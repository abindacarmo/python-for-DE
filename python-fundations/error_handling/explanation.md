# Python Error Handling
## Try, Except, Finally, Else, and Custom Exceptions

---

# 🇺🇸 English Version

# Introduction

When we write programs, errors are unavoidable.

For example:

- A user enters text instead of a number.
- A file does not exist.
- The internet connection is lost.
- A database cannot be reached.

If we don't handle these errors, Python stops the program immediately and displays an error message called a **Traceback**.

Example:

```python
number = int(input("Enter a number: "))
```

Input:

```
abc
```

Output:

```
ValueError: invalid literal for int()
```

The program crashes.

To prevent this, Python provides **Exception Handling**.

---

# What is an Exception?

An **Exception** is an event that interrupts the normal flow of a program.

Instead of crashing, we can catch the exception and decide what to do.

Python uses:

- try
- except
- else
- finally
- raise

to handle exceptions.

---

# Basic Syntax

```python
try:
    # Code that may raise an error
except:
    # Code executed if an error occurs
```

Example

```python
try:
    number = int(input("Enter a number: "))
    print(number)

except:
    print("Invalid input!")
```

Output

```
Enter a number:
abc

Invalid input!
```

Instead of crashing, the program continues.

---

# How try Works

Python executes the code inside `try`.

If no error occurs:

```
try
 ↓
No Error
 ↓
Continue Program
```

If an error occurs:

```
try
 ↓
Exception
 ↓
except
 ↓
Continue Program
```

---

# Catching Specific Exceptions

Instead of catching everything, catch only the errors you expect.

Example

```python
try:
    number = int(input("Number: "))
except ValueError:
    print("Please enter a valid integer.")
```

---

# Multiple Exceptions

```python
try:
    number = int(input("Number: "))
    result = 10 / number

except ValueError:
    print("Input must be a number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Input

```
0
```

Output

```
Cannot divide by zero.
```

---

# Catching Multiple Exceptions Together

```python
try:
    number = int(input())
    result = 10 / number

except (ValueError, ZeroDivisionError):
    print("Invalid input.")
```

---

# Getting the Error Message

```python
try:
    number = int(input())
except ValueError as e:
    print(e)
```

Output

```
invalid literal for int() with base 10
```

`e` stores the exception object.

---

# The else Block

`else` runs only if **no exception occurs**.

```python
try:
    number = int(input("Number: "))
except ValueError:
    print("Invalid")

else:
    print("Everything is OK.")
```

Flow

```
try
 ↓
No Error
 ↓
else
```

---

# The finally Block

`finally` always executes.

Even if an exception occurs.

Example

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program finished.")
```

Output

```
File not found.
Program finished.
```

---

# Why finally is Important

Usually used for:

- Closing files
- Closing database connections
- Closing network connections
- Cleaning temporary files

Example

```python
file = None

try:
    file = open("data.txt")

except FileNotFoundError:
    print("Missing file.")

finally:
    if file:
        file.close()
```

---

# Complete Example

```python
try:
    number = int(input("Number: "))
    result = 100 / number

except ValueError:
    print("Please enter a number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program ended.")
```

---

# Raising Exceptions

Sometimes we want to create an error ourselves.

Use `raise`.

Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Output

```
ValueError: Age cannot be negative.
```

---

# Why Raise Exceptions?

To stop invalid data early.

Example

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance.")

    return balance - amount
```

---

# Custom Exceptions

We can create our own exception classes.

Syntax

```python
class MyError(Exception):
    pass
```

---

Example

```python
class InvalidAgeError(Exception):
    pass
```

Using it

```python
age = -2

if age < 0:
    raise InvalidAgeError("Age cannot be negative.")
```

---

# More Realistic Example

```python
class InvalidPasswordError(Exception):
    pass


def register(password):

    if len(password) < 8:
        raise InvalidPasswordError(
            "Password must contain at least 8 characters."
        )

    print("Registration successful.")
```

Usage

```python
try:
    register("abc")

except InvalidPasswordError as e:
    print(e)
```

Output

```
Password must contain at least 8 characters.
```

---

# Exception Hierarchy

```
BaseException
      │
  Exception
      │
 ├── ValueError
 ├── TypeError
 ├── FileNotFoundError
 ├── IndexError
 ├── KeyError
 ├── ZeroDivisionError
 └── YourCustomError
```

---

# Common Built-in Exceptions

| Exception | Description |
|------------|-------------|
| ValueError | Wrong value |
| TypeError | Wrong data type |
| IndexError | Invalid list index |
| KeyError | Dictionary key missing |
| FileNotFoundError | File does not exist |
| ZeroDivisionError | Division by zero |
| NameError | Variable not defined |

---

# Best Practices

✅ Catch specific exceptions.

```python
except ValueError:
```

Instead of

```python
except:
```

---

✅ Keep try blocks small.

Bad

```python
try:
    # 100 lines
```

Good

```python
try:
    value = int(input())
```

---

✅ Use finally for cleanup.

---

✅ Raise exceptions when invalid data appears.

---

✅ Create custom exceptions for large projects.

---

# Common Mistakes

❌ Using empty except

```python
except:
    pass
```

This hides every error.

---

❌ Ignoring exceptions

```python
except:
    pass
```

Never ignore errors unless you have a reason.

---

❌ Using exceptions instead of normal logic.

Wrong

```python
try:
    print(numbers[100])

except:
    pass
```

Better

```python
if len(numbers) > 100:
    print(numbers[100])
```

---

# Summary

Python Error Handling consists of:

- try
- except
- else
- finally
- raise
- custom exceptions

These tools make programs:

- safer
- cleaner
- easier to debug
- more reliable

---

# 🇮🇩 Versi Bahasa Indonesia

# Pendahuluan

Saat kita membuat program, **error adalah hal yang tidak bisa dihindari**.

Contohnya:

- Pengguna memasukkan huruf padahal program meminta angka.
- File yang ingin dibuka ternyata tidak ada.
- Koneksi internet terputus.
- Database gagal diakses.

Jika error tidak ditangani, Python akan langsung menghentikan program dan menampilkan **Traceback**.

Karena itu, Python menyediakan **Error Handling** atau **Exception Handling** agar program tetap berjalan dengan baik.

---

# Apa itu Exception?

**Exception** adalah sebuah kejadian yang menyebabkan alur normal program terganggu.

Daripada program langsung berhenti, kita bisa menangkap error tersebut dan menentukan tindakan yang harus dilakukan.

Python menyediakan:

- `try`
- `except`
- `else`
- `finally`
- `raise`

untuk menangani exception.

---

# try dan except

Sintaks dasar:

```python
try:
    # kode yang mungkin menghasilkan error
except:
    # dijalankan jika terjadi error
```

Contoh:

```python
try:
    angka = int(input("Masukkan angka: "))
    print(angka)
except:
    print("Input tidak valid!")
```

Jika pengguna memasukkan `abc`, program tidak akan berhenti, tetapi akan menampilkan pesan **"Input tidak valid!"**.

---

# Cara Kerja try

Python menjalankan kode di dalam `try`.

Jika **tidak ada error**, program langsung melanjutkan ke bagian berikutnya.

Jika **terjadi error**, Python akan langsung berpindah ke blok `except`.

---

# Menangkap Error Tertentu

Lebih baik menangkap error yang memang diperkirakan akan terjadi.

Contoh:

```python
try:
    angka = int(input())
except ValueError:
    print("Masukkan angka yang benar.")
```

---

# Menangani Banyak Exception

```python
try:
    angka = int(input())
    hasil = 10 / angka

except ValueError:
    print("Input harus berupa angka.")

except ZeroDivisionError:
    print("Tidak boleh membagi dengan nol.")
```

---

# Menampilkan Pesan Error

```python
try:
    angka = int(input())
except ValueError as e:
    print(e)
```

Variabel `e` menyimpan informasi detail tentang error.

---

# else

`else` hanya dijalankan jika **tidak ada exception**.

```python
try:
    angka = int(input())
except ValueError:
    print("Input salah.")
else:
    print("Input berhasil.")
```

---

# finally

`finally` akan **selalu dijalankan**, baik terjadi error maupun tidak.

Biasanya digunakan untuk:

- menutup file
- menutup koneksi database
- membersihkan resource
- menutup koneksi jaringan

Contoh:

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File tidak ditemukan.")
finally:
    print("Program selesai.")
```

---

# raise

`raise` digunakan untuk membuat exception sendiri.

```python
umur = -1

if umur < 0:
    raise ValueError("Umur tidak boleh negatif.")
```

---

# Mengapa Menggunakan raise?

Karena kita bisa menghentikan program saat data yang diterima tidak valid.

Contoh:

```python
def tarik_uang(saldo, jumlah):

    if jumlah > saldo:
        raise ValueError("Saldo tidak cukup.")

    return saldo - jumlah
```

---

# Custom Exception

Kita juga bisa membuat exception sendiri.

```python
class InvalidAgeError(Exception):
    pass
```

Penggunaan:

```python
umur = -2

if umur < 0:
    raise InvalidAgeError("Umur tidak boleh negatif.")
```

---

# Contoh Proyek Sederhana

```python
class PasswordError(Exception):
    pass


def register(password):

    if len(password) < 8:
        raise PasswordError(
            "Password minimal harus 8 karakter."
        )

    print("Registrasi berhasil.")
```

Pemanggilan:

```python
try:
    register("abc")
except PasswordError as e:
    print(e)
```

---

# Hirarki Exception

```
BaseException
      │
  Exception
      │
 ├── ValueError
 ├── TypeError
 ├── IndexError
 ├── KeyError
 ├── FileNotFoundError
 ├── ZeroDivisionError
 └── Custom Exception
```

---

# Exception yang Paling Sering Digunakan

| Exception | Penjelasan |
|------------|------------|
| ValueError | Nilai tidak sesuai |
| TypeError | Tipe data salah |
| IndexError | Index list tidak ada |
| KeyError | Key dictionary tidak ditemukan |
| FileNotFoundError | File tidak ada |
| ZeroDivisionError | Membagi dengan nol |
| NameError | Variabel belum dibuat |

---

# Best Practices

- Tangkap exception yang spesifik.
- Jangan gunakan `except:` tanpa alasan.
- Gunakan `finally` untuk membersihkan resource.
- Gunakan `raise` untuk memvalidasi data.
- Gunakan custom exception pada proyek yang lebih besar.

---

# Kesalahan yang Sering Dilakukan

### 1. Menggunakan `except:` kosong

```python
except:
    pass
```

Hal ini menyembunyikan semua error dan membuat proses debugging menjadi sulit.

### 2. Mengabaikan Exception

```python
except:
    pass
```

Sebaiknya selalu tampilkan atau catat error jika memang perlu ditangani.

### 3. Menggunakan Exception untuk Logika Biasa

Kurang baik:

```python
try:
    print(data[100])
except:
    pass
```

Lebih baik:

```python
if len(data) > 100:
    print(data[100])
```

---

# Ringkasan

Error Handling di Python terdiri dari:

- `try`
- `except`
- `else`
- `finally`
- `raise`
- Custom Exception

Dengan memahami semua konsep ini, program yang kita buat akan menjadi:

- lebih aman
- lebih stabil
- lebih mudah di-debug
- lebih profesional
