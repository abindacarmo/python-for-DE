# Modules, Packages & Virtual Environment (venv)

> Learn how Python organizes code and manages project dependencies.

---

# Table of Contents

1. What is a Module?
2. Creating Your Own Module
3. Importing Modules
4. Different Ways to Import
5. Built-in Modules
6. Third-party Modules
7. What is pip?
8. Installing Packages
9. requirements.txt
10. What is a Package?
11. Creating Your Own Package
12. __init__.py
13. Relative vs Absolute Imports
14. Virtual Environment (venv)
15. Creating and Activating venv
16. Installing Packages inside venv
17. Deactivating venv
18. Best Practices
19. Common Mistakes
20. Summary

---

# 1. What is a Module?

## English

A module is simply a Python file that contains Python code.

A module can contain:

- Variables
- Functions
- Classes
- Constants

Instead of writing everything inside one file, Python lets us separate code into multiple modules.

Example:

```
math_utils.py
```

```python
def add(a, b):
    return a + b
```

Another file:

```python
import math_utils

print(math_utils.add(5, 3))
```

Output

```
8
```

Why use modules?

- Better organization
- Code reuse
- Easier maintenance
- Cleaner projects

---

## Bahasa Indonesia

Module adalah sebuah file Python (.py) yang berisi kode Python.

Isi module dapat berupa:

- Variable
- Function
- Class
- Constant

Daripada semua kode ditulis dalam satu file yang sangat panjang, Python memungkinkan kita membaginya menjadi beberapa file.

Contoh:

```
math_utils.py
```

```python
def add(a, b):
    return a + b
```

Kemudian dipanggil dari file lain.

Keuntungan module:

- Program lebih rapi
- Kode dapat digunakan kembali
- Lebih mudah dipelihara
- Lebih mudah dibaca

---

# 2. Creating Your Own Module

## English

Example:

calculator.py

```python
def multiply(a, b):
    return a * b
```

main.py

```python
import calculator

print(calculator.multiply(4,5))
```

Output

```
20
```

Python automatically searches for calculator.py in the current folder.

---

## Bahasa Indonesia

Misalnya kita membuat file:

```
calculator.py
```

Lalu di file lain:

```
main.py
```

Kita bisa menggunakan

```python
import calculator
```

Python akan mencari file tersebut pada folder yang sama.

---

# 3. Importing Modules

## English

Basic import

```python
import math
```

Use

```python
print(math.sqrt(16))
```

Output

```
4.0
```

---

## Bahasa Indonesia

Cara paling dasar adalah menggunakan

```python
import math
```

Kemudian semua fungsi dipanggil menggunakan nama module.

Contoh

```python
math.sqrt(16)
```

---

# 4. Different Ways to Import

## English

### Import entire module

```python
import math
```

---

### Import specific function

```python
from math import sqrt

print(sqrt(25))
```

---

### Import multiple functions

```python
from math import sqrt, pi
```

---

### Import everything

```python
from math import *
```

Not recommended.

---

### Import with alias

```python
import numpy as np
```

or

```python
import pandas as pd
```

---

## Bahasa Indonesia

Ada beberapa cara melakukan import.

### Import seluruh module

```python
import math
```

### Import satu function

```python
from math import sqrt
```

### Import beberapa function

```python
from math import sqrt, pi
```

### Import semua

```python
from math import *
```

Tidak disarankan karena membuat kode sulit dibaca.

### Menggunakan alias

```python
import numpy as np
```

Alias membuat penulisan lebih singkat.

---

# 5. Built-in Modules

## English

Python already includes many useful modules.

Examples

- math
- random
- datetime
- os
- pathlib
- json
- csv
- statistics

Example

```python
import random

print(random.randint(1,10))
```

---

## Bahasa Indonesia

Python sudah menyediakan banyak module bawaan.

Contohnya:

- math
- random
- datetime
- os
- pathlib
- csv
- json

Tidak perlu install lagi.

---

# 6. Third-party Modules

## English

Third-party modules are created by other developers.

Examples

- pandas
- numpy
- requests
- flask
- django
- matplotlib

These packages must be installed.

Example

```bash
pip install pandas
```

---

## Bahasa Indonesia

Third-party module adalah module yang dibuat oleh developer lain.

Misalnya:

- pandas
- numpy
- requests

Harus diinstall terlebih dahulu menggunakan pip.

---

# 7. What is pip?

## English

pip is Python's package manager.

It downloads libraries from PyPI.

Example

```bash
pip install requests
```

---

## Bahasa Indonesia

pip adalah package manager milik Python.

Fungsinya untuk menginstall library dari internet.

Contoh

```bash
pip install requests
```

---

# 8. Installing Packages

## English

Install

```bash
pip install pandas
```

Upgrade

```bash
pip install --upgrade pandas
```

Uninstall

```bash
pip uninstall pandas
```

Show installed packages

```bash
pip list
```

---

## Bahasa Indonesia

Install

```bash
pip install pandas
```

Update

```bash
pip install --upgrade pandas
```

Hapus

```bash
pip uninstall pandas
```

Melihat package

```bash
pip list
```

---

# 9. requirements.txt

## English

A requirements.txt file stores project dependencies.

Example

```
pandas==2.3.0
numpy==2.2.0
requests==2.32.0
```

Install all packages

```bash
pip install -r requirements.txt
```

Generate file

```bash
pip freeze > requirements.txt
```

---

## Bahasa Indonesia

requirements.txt digunakan untuk menyimpan daftar package yang digunakan project.

Contoh

```
pandas==2.3.0
numpy==2.2.0
```

Install semuanya

```bash
pip install -r requirements.txt
```

Membuat file otomatis

```bash
pip freeze > requirements.txt
```

---

# 10. What is a Package?

## English

A package is a folder containing multiple modules.

Example

```
project/

    utils/

        math.py

        string.py

        __init__.py
```

Packages help organize large projects.

---

## Bahasa Indonesia

Package adalah kumpulan beberapa module di dalam satu folder.

Biasanya terdapat file

```
__init__.py
```

yang menandakan folder tersebut sebagai package.

---

# 11. Creating Your Own Package

## English

Structure

```
shop/

    __init__.py

    payment.py

    cart.py
```

Import

```python
from shop import payment
```

---

## Bahasa Indonesia

Misalnya membuat folder

```
shop
```

Di dalamnya terdapat beberapa module.

Kemudian dapat dipanggil menggunakan

```python
from shop import payment
```

---

# 12. __init__.py

## English

This file tells Python that the directory is a package.

It may also contain initialization code.

---

## Bahasa Indonesia

File ini digunakan untuk menandai folder sebagai package.

Sekarang pada Python modern file ini sering kali boleh kosong.

---

# 13. Relative vs Absolute Imports

## English

Absolute

```python
from shop.payment import pay
```

Relative

```python
from .payment import pay
```

Absolute imports are generally preferred.

---

## Bahasa Indonesia

Absolute import menggunakan path lengkap.

Relative import menggunakan titik (`.`) untuk menunjukkan lokasi relatif.

Untuk project besar biasanya lebih disarankan menggunakan absolute import.

---

# 14. Virtual Environment (venv)

## English

A virtual environment creates an isolated Python environment for a project.

Without venv:

All projects share the same installed packages.

With venv:

Each project has its own packages.

Advantages

- Avoid version conflicts
- Cleaner projects
- Easier deployment

---

## Bahasa Indonesia

Virtual Environment adalah lingkungan Python yang terpisah untuk setiap project.

Tanpa venv:

Semua project menggunakan package yang sama.

Dengan venv:

Setiap project memiliki package sendiri.

Keuntungan:

- Tidak bentrok versi
- Lebih rapi
- Mudah dipindahkan

---

# 15. Creating and Activating venv

## English

Create

```bash
python -m venv .venv
```

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Deactivate

```bash
deactivate
```

---

## Bahasa Indonesia

Membuat virtual environment

```bash
python -m venv .venv
```

Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Keluar dari virtual environment

```bash
deactivate
```

---

# 16. Installing Packages inside venv

## English

Once activated:

```bash
pip install pandas
```

The package is installed only inside the virtual environment.

---

## Bahasa Indonesia

Setelah venv aktif,

semua package yang diinstall hanya berlaku untuk project tersebut.

---

# 17. Deactivating venv

## English

Simply run

```bash
deactivate
```

This returns to the global Python environment.

---

## Bahasa Indonesia

Cukup jalankan

```bash
deactivate
```

Maka kita kembali ke Python global.

---

# 18. Best Practices

## English

✔ Use one venv per project

✔ Never commit the venv folder

✔ Commit requirements.txt

✔ Organize code into modules

✔ Group related modules into packages

---

## Bahasa Indonesia

Beberapa praktik terbaik:

- Gunakan satu venv untuk setiap project
- Jangan upload folder venv ke GitHub
- Simpan requirements.txt
- Pisahkan kode menjadi module
- Gunakan package untuk project besar

---

# 19. Common Mistakes

## English

❌ Forgetting to activate venv

❌ Installing packages globally

❌ Using

```python
from module import *
```

❌ Deleting requirements.txt

❌ Mixing project dependencies

---

## Bahasa Indonesia

Kesalahan yang sering terjadi:

- Lupa mengaktifkan venv
- Install package secara global
- Menggunakan import *
- Tidak membuat requirements.txt
- Semua project memakai package yang sama

---

# 20. Summary

## English

In this chapter you learned:

- Modules
- Packages
- Imports
- pip
- requirements.txt
- __init__.py
- Virtual environments
- Best practices

These concepts are essential for every professional Python developer.

---

## Bahasa Indonesia

Pada bab ini kita telah mempelajari:

- Module
- Package
- Import
- pip
- requirements.txt
- __init__.py
- Virtual Environment (venv)
- Best Practices

