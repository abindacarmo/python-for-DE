# Python Control Flow — Guide for Data Engineering
# Python Control Flow — Panduan untuk Data Engineering

**Language: English | Level: Intermediate | Author: Abinda**
**Bahasa: Indonesia | Level: Menengah | Penulis: Abinda**

---

## Table of Contents
## Daftar Isi

1. [if / elif / else](#1-if--elif--else)
2. [for loop](#2-for-loop)
3. [while loop](#3-while-loop)
4. [break / continue / pass](#4-break--continue--pass)
5. [List, Dict, Set Comprehension](#5-list-dict-set-comprehension)
6. [Real DE Use Cases](#6-real-de-use-cases)

---

## 1. if / elif / else

### How does it work?

`if` is used to make decisions based on a condition. If the condition is `True`, the code inside runs. If `False`, it moves to `elif` or `else`.

### Bagaimana cara kerjanya?

`if` dipakai untuk mengambil keputusan berdasarkan suatu kondisi. Kalau kondisinya `True`, kode di dalamnya akan dijalankan. Kalau `False`, Python akan lanjut cek `elif` atau `else`.

### Basic Structure
### Struktur Dasar

```python
if condition_1:
    # runs when condition_1 is True
elif condition_2:
    # runs when condition_2 is True
else:
    # runs when all conditions are False
```

```python
if kondisi_1:
    # jalan kalau kondisi_1 True
elif kondisi_2:
    # jalan kalau kondisi_2 True
else:
    # jalan kalau semua kondisi False
```

### Example: Grade Validation
### Contoh: Validasi Nilai

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(grade)  # Output: "B"
```

### Ternary (One Line)
### Ternary (Satu Baris)

```python
# value_if_true if condition else value_if_false
status = "active" if user_id else "none"

# Use to assign a default value
name = data.get("name") or "Unknown"
```

```python
# nilai_jika_true if kondisi else nilai_jika_false
status = "aktif" if user_id else "tidak ada"

# Dipakai untuk memberi nilai default
nama = data.get("name") or "Tidak Diketahui"
```

### Logical Operators
### Operator Logika

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both must be True | `x > 0 and x < 100` |
| `or` | At least one must be True | `x == 0 or x == 1` |
| `not` | Inverts the condition | `not is_empty` |
| `is` | Compares identity | `val is None` |
| `in` | Checks membership in list/dict | `key in data` |

| Operator | Arti | Contoh |
|----------|------|--------|
| `and` | Kedua sisi harus True | `x > 0 and x < 100` |
| `or` | Cukup salah satu True | `x == 0 or x == 1` |
| `not` | Membalik kondisi | `not is_empty` |
| `is` | Membandingkan identitas | `val is None` |
| `in` | Cek keanggotaan di list/dict | `key in data` |

> **📝 Note — `is` vs `==`:**
> - `==` compares **values** (are the contents the same?)
> - `is` compares **identity** (are they the exact same object in memory?)
>
> **📝 Catatan — `is` vs `==`:**
> - `==` membandingkan **nilai** (apakah isinya sama?)
> - `is` membandingkan **identitas** (apakah objek yang sama persis di memori?)

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  — same value / nilai sama
print(a is b)   # False — different objects in memory / objek berbeda di memori

# Why use `is None` instead of `== None`?
# Kenapa pakai `is None` bukan `== None`?
val = None
print(val is None)   # ✅ Correct — recommended (PEP 8) / Benar — direkomendasikan (PEP 8)
print(val == None)   # ⚠️  Works but not recommended / Bisa jalan tapi tidak disarankan
```

> `None` is a **singleton** in Python — only one `None` object exists in the entire program, so `is` is always accurate and faster.
>
> `None` adalah **singleton** di Python — hanya ada **satu** objek `None` di seluruh program, jadi `is` selalu akurat dan lebih cepat.

### Note for Data Engineering
### Catatan untuk Data Engineering

> **Common practice:** `if` is heavily used for column validation, checking null values, or routing data to different tables based on record type.
>
> **Praktik umum:** `if` banyak dipakai untuk validasi kolom, mengecek nilai null, atau merutekan data ke tabel berbeda berdasarkan tipe record.

```python
# Validation example in a pipeline
# Contoh validasi di sebuah pipeline
def validate_record(row):
    if row.get("id") is None:
        return False, "ID is missing"
    if row.get("value") < 0:
        return False, "Negative value"
    return True, "OK"
```

---

## 2. for loop

### How does it work?

`for` loop iterates over a sequence (list, tuple, dict, string, range). It stops automatically when the sequence ends.

### Bagaimana cara kerjanya?

`for` loop melakukan iterasi atas sebuah sequence (list, tuple, dict, string, range). Loop ini berhenti otomatis saat sequence-nya habis.

### Basic Structure
### Struktur Dasar

```python
# Iterate over a list
for item in data_list:
    print(item)

# With index — use enumerate()
for i, item in enumerate(data_list):
    print(i, item)

# Iterate over a dictionary
for key, value in data.items():
    print(key, "→", value)

# range(start, stop, step)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

```python
# Iterasi atas sebuah list
for item in data_list:
    print(item)

# Dengan index — pakai enumerate()
for i, item in enumerate(data_list):
    print(i, item)

# Iterasi atas dictionary
for key, value in data.items():
    print(key, "→", value)

# range(mulai, berhenti, langkah)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

### Example: Iterate List of Dicts (Rows)
### Contoh: Iterasi List Berisi Dictionary (Rows)

```python
rows = [
    {"id": 1, "name": "Ana",  "city": "Dili"},
    {"id": 2, "name": "Budi", "city": "Baucau"},
    {"id": 3, "name": "Cici", "city": "Dili"},
]

for row in rows:
    print(f"ID: {row['id']} | Name: {row['name']}")

# Output:
# ID: 1 | Name: Ana
# ID: 2 | Name: Budi
# ID: 3 | Name: Cici
```

### Example: zip() — Combine Two Lists
### Contoh: zip() — Menggabungkan Dua List

```python
names  = ["Ana", "Budi", "Cici"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Output:
# Ana: 85
# Budi: 92
# Cici: 78
```

### Example: Iterate Multiple Files (Batch)
### Contoh: Iterasi Banyak File Sekaligus (Batch)

```python
from pathlib import Path

# Load all CSV files in a folder
# Muat semua file CSV di sebuah folder
for file in Path("data/").glob("*.csv"):
    print(f"Processing: {file.name}")  # Memproses: {file.name}
    # read the file... / baca file ini...
```

### Note for Data Engineering
### Catatan untuk Data Engineering

> **Common practice:** `for row in cursor.fetchall()` to process SQL query results, or `for file in Path(dir).glob("*.csv")` to batch-load files.
>
> **Praktik umum:** `for row in cursor.fetchall()` untuk memproses hasil query SQL, atau `for file in Path(dir).glob("*.csv")` untuk memuat banyak file sekaligus (batch).

---

## 3. while loop

### How does it work?

`while` loop keeps running as long as the condition is `True`. Use it when you don't know exactly how many iterations are needed — e.g. retry logic, polling, or streaming data.

### Bagaimana cara kerjanya?

`while` loop terus berjalan selama kondisinya `True`. Dipakai kalau kamu belum tahu pasti berapa kali iterasi dibutuhkan — misalnya retry logic, polling, atau streaming data.

### Basic Structure
### Struktur Dasar

```python
counter = 0
while counter < 5:
    print(counter)
    counter += 1  # IMPORTANT: always update the condition!
                  # PENTING: selalu update kondisinya!
```

### Infinite Loop with break
### Infinite Loop dengan break

```python
while True:
    data = fetch_data()
    if not data:
        break  # stop loop when no more data
               # hentikan loop kalau data sudah habis
    process(data)
```

### Example: Retry Pattern — Common in Pipelines
### Contoh: Retry Pattern — Umum di Pipeline

```python
max_retries = 3
attempt = 0

while attempt < max_retries:
    try:
        result = connect_to_db()
        print("Connection successful!")  # Koneksi berhasil!
        break  # success, exit the loop / berhasil, keluar dari loop
    except Exception as e:
        attempt += 1
        print(f"Attempt {attempt} failed: {e}")  # Percobaan {attempt} gagal: {e}

if attempt == max_retries:
    print("All retries failed! Please check the connection.")
    # Semua percobaan gagal! Silakan cek koneksinya.
```

### Example: Polling — Wait for New Data
### Contoh: Polling — Menunggu Data Baru

```python
import time

def pipeline_wait_for_data():
    while True:
        new_records = check_for_new_records()

        if new_records:
            process(new_records)
            print(f"Processed {len(new_records)} records.")
            # Memproses {len(new_records)} record.
        else:
            print("No new data, waiting...")  # Tidak ada data baru, menunggu...

        time.sleep(60)  # wait 1 minute before checking again
                         # tunggu 1 menit sebelum cek lagi
```

### ⚠️ Important Warning
### ⚠️ Peringatan Penting

> **Watch out for infinite loops!** Always make sure the `while` condition will eventually become `False`, or use `break` to exit. Otherwise, the program runs forever until manually stopped.
>
> **Hati-hati dengan infinite loop!** Selalu pastikan kondisi `while` pada akhirnya akan menjadi `False`, atau gunakan `break` untuk keluar. Kalau tidak, program akan berjalan terus-menerus sampai dihentikan manual.

---

## 4. break / continue / pass

### break — Exit the Loop
### break — Keluar dari Loop

Stops the entire loop immediately.
Menghentikan seluruh loop secara langsung.

```python
data = [10, 25, None, 42, 8]

for val in data:
    if val is None:
        print("Found null value, stopping process!")
        # Ditemukan nilai null, menghentikan proses!
        break
    print(val)

# Output:
# 10
# 25
# Found null value, stopping process!
```

### continue — Skip an Iteration
### continue — Melewati Satu Iterasi

Skips the current iteration and moves to the next one.
Melewati iterasi saat ini dan lanjut ke iterasi berikutnya.

```python
data = [10, None, 25, None, 42]

for val in data:
    if val is None:
        continue  # skip null values / lewati nilai null
    print(val)

# Output:
# 10
# 25
# 42
```

### pass — Do Nothing
### pass — Tidak Melakukan Apa-apa

Placeholder — the code does nothing. Use when syntax requires a block but you have no logic yet.

Placeholder — kode ini tidak melakukan apa-apa. Dipakai saat sintaksis membutuhkan sebuah blok tapi kamu belum punya logikanya.

```python
for item in data:
    if item < 0:
        pass  # TODO: handle negative values later
              # TODO: tangani nilai negatif nanti
    else:
        process(item)
```

### for...else — Special Structure
### for...else — Struktur Spesial

The `else` block runs only when the loop finishes **without** hitting `break`.

Blok `else` hanya jalan kalau loop selesai **tanpa** terkena `break`.

```python
records = [
    {"id": 1, "error": False},
    {"id": 2, "error": False},
    {"id": 3, "error": False},
]

for row in records:
    if row["error"]:
        print(f"Error found in record {row['id']}")
        # Ditemukan error di record {row['id']}
        break
else:
    print("Validation successful! All records are valid.")
    # Validasi berhasil! Semua record valid.

# Output: Validation successful! All records are valid.
```

### Comparison: break vs continue
### Perbandingan: break vs continue

| | `break` | `continue` |
|---|---|---|
| **Action** | Stops the entire loop | Skips only the current iteration |
| **Code after** | Does not run | Runs in the next iteration |
| **Use when** | Critical condition is found | Skipping invalid/null data |

| | `break` | `continue` |
|---|---|---|
| **Aksi** | Menghentikan seluruh loop | Hanya melewati iterasi saat ini |
| **Kode setelahnya** | Tidak dijalankan | Dijalankan di iterasi berikutnya |
| **Dipakai saat** | Ditemukan kondisi kritis | Melewati data invalid/null |

---

## 5. List, Dict, Set Comprehension

### How does it work?

A compact way to create a new collection from an iteration. More Pythonic and faster than a regular `for` loop.

### Bagaimana cara kerjanya?

Cara ringkas untuk membuat koleksi baru dari sebuah iterasi. Lebih Pythonic dan lebih cepat dibanding `for` loop biasa.

### Syntax
### Sintaksis

```python
# [expression for item in iterable if condition]
# [ekspresi for item in iterable if kondisi]

# List comprehension
squares = [x**2 for x in range(5)]              # [0, 1, 4, 9, 16]
evens   = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Dict comprehension
{key: value.upper() for key, value in data.items()}

# Set comprehension — automatically unique
# Set comprehension — otomatis unik
unique_cities = {row["city"] for row in records}
```

### Comparison: for Loop vs Comprehension
### Perbandingan: for Loop vs Comprehension

```python
# Version with for loop / Versi dengan for loop
result = []
for x in numbers:
    if x > 0:
        result.append(x * 2)

# Version with list comprehension (same result)
# Versi dengan list comprehension (hasil sama)
result = [x * 2 for x in numbers if x > 0]
```

### DE Example: Data Transformation
### Contoh DE: Transformasi Data

```python
records = [
    {"id": 1, "name": "  Ana  ", "score": None},
    {"id": 2, "name": "Budi",    "score": 88},
    {"id": 3, "name": "Cici",    "score": 72},
]

# Filter invalid records and strip whitespace
# Filter record invalid dan hapus spasi berlebih
valid = [
    {"id": r["id"], "name": r["name"].strip()}
    for r in records
    if r["score"] is not None
]

# Result: [{"id": 2, "name": "Budi"}, {"id": 3, "name": "Cici"}]
# Hasil: [{"id": 2, "name": "Budi"}, {"id": 3, "name": "Cici"}]
```

### DE Example: Dict Comprehension for Normalization
### Contoh DE: Dict Comprehension untuk Normalisasi

```python
# Normalize all column names (lowercase and strip whitespace)
# Normalisasi semua nama kolom (huruf kecil dan hapus spasi)
raw_data = {"Name ": "ANA", " City": "DILI", "Score ": "85"}

clean_data = {
    key.strip().lower(): value.strip().title()
    for key, value in raw_data.items()
}

# Result: {"name": "Ana", "city": "Dili", "score": "85"}
# Hasil: {"name": "Ana", "city": "Dili", "score": "85"}
```

### Generator Expression
### Generator Expression

```python
# Like list comprehension but uses () — does NOT create the full list in memory
# Efficient for large datasets
#
# Mirip list comprehension tapi pakai () — TIDAK membuat list penuh di memori
# Efisien untuk dataset besar

total = sum(row["value"] for row in records if row["value"] is not None)
```

> **Note:** Use a **generator** (with `()`) for large data — it doesn't load everything into memory at once. Use **list comprehension** (with `[]`) when you need to access elements multiple times.
>
> **Catatan:** Gunakan **generator** (dengan `()`) untuk data besar — tidak memuat semuanya ke memori sekaligus. Gunakan **list comprehension** (dengan `[]`) kalau kamu butuh akses elemen berkali-kali.

---

## 6. Real DE Use Cases
## 6. Contoh Penggunaan Nyata di DE

### Complete ETL Pattern
### Pola ETL Lengkap

```python
def process_etl(raw_data: list) -> tuple[list, list]:
    """
    ETL pipeline example with complete control flow.
    Contoh pipeline ETL dengan control flow lengkap.

    Params:
        raw_data: List of records from a data source
        raw_data: List record dari sebuah sumber data

    Returns:
        (valid_results, error_list)
    """
    results = []
    errors  = []

    for i, row in enumerate(raw_data):

        # === VALIDATION === / === VALIDASI ===

        # Check missing ID / Cek ID yang hilang
        if row.get("id") is None:
            errors.append({"row": i, "reason": "ID is missing"})
            continue

        # Check null value / Cek nilai null
        if row.get("value") is None:
            errors.append({"row": i, "id": row["id"], "reason": "Null value"})
            continue

        # Check value range / Cek rentang nilai
        if not (0 <= row["value"] <= 10000):
            errors.append({"row": i, "id": row["id"], "reason": "Value out of range"})
            continue

        # === TRANSFORMATION === / === TRANSFORMASI ===

        # Categorize based on value / Kategorikan berdasarkan nilai
        if row["value"] > 8000:
            category = "premium"
        elif row["value"] > 4000:
            category = "standard"
        else:
            category = "basic"

        # Normalize string / Normalisasi string
        clean_name = row.get("name", "").strip().title() or "Unknown"

        # Build new record / Susun record baru
        new_record = {
            "id":       row["id"],
            "name":     clean_name,
            "value":    row["value"],
            "category": category,
        }
        results.append(new_record)

    return results, errors


# Use the function / Gunakan fungsinya
raw_data = [
    {"id": 1,    "name": "  tasi mane  ", "value": 9000},
    {"id": 2,    "name": "Dili port",      "value": 3500},
    {"id": None, "name": "Manufahi",       "value": 6000},   # error: ID missing / ID hilang
    {"id": 4,    "name": "Baucau",         "value": None},   # error: null value / nilai null
    {"id": 5,    "name": "Viqueque",       "value": 12000},  # error: out of range / di luar rentang
]

valid_records, error_list = process_etl(raw_data)

print(f"✅ Valid:  {len(valid_records)} records")
print(f"❌ Errors: {len(error_list)} records")

for e in error_list:
    print(f"  - Row {e['row']}: {e['reason']}")
```

### Expected Output
### Output yang Diharapkan

```
✅ Valid:  2 records
❌ Errors: 3 records
  - Row 2: ID is missing
  - Row 3: Null value
  - Row 4: Value out of range
```

### Batch File Loading with Retry
### Pemuatan File Batch dengan Retry

```python
import time
from pathlib import Path

def batch_load_files(folder: str, max_retries: int = 3):
    """Load all CSV files in a folder with retry logic."""
    """Muat semua file CSV di sebuah folder dengan retry logic."""
    success = []
    failed  = []

    for file in Path(folder).glob("*.csv"):
        attempt = 0

        while attempt < max_retries:
            try:
                data = read_csv(file)
                success.append(file.name)
                print(f"✅ {file.name} — success")  # — berhasil
                break
            except Exception as e:
                attempt += 1
                print(f"⚠️  {file.name} attempt {attempt}: {e}")
                # percobaan {attempt}: {e}
                time.sleep(2)
        else:
            # Runs only when while ends without break (all retries failed)
            # Jalan hanya kalau while selesai tanpa break (semua retry gagal)
            failed.append(file.name)
            print(f"❌ {file.name} — failed after {max_retries} attempts")
            # — gagal setelah {max_retries} percobaan

    return success, failed
```

---

## Quick Summary
## Ringkasan Singkat

| Concept | Use when | DE Example |
|---------|----------|------------|
| `if/elif/else` | Need to make decisions based on a condition | Validate columns, route data |
| `for` loop | Number of iterations is known, iterating a sequence | Process rows, batch load files |
| `while` loop | Number of iterations is unknown | Retry logic, polling, streaming |
| `break` | Critical condition is found, stop immediately | Stop on fatal error |
| `continue` | Skip invalid or irrelevant records | Skip null/bad rows |
| `pass` | Placeholder for logic not yet written | TODO blocks |
| Comprehension | Transform/filter a collection simply | Normalize data, clean columns |

| Konsep | Dipakai Saat | Contoh DE |
|--------|--------------|-----------|
| `if/elif/else` | Perlu mengambil keputusan berdasarkan kondisi | Validasi kolom, merutekan data |
| `for` loop | Jumlah iterasi diketahui, iterasi sebuah sequence | Proses rows, batch load file |
| `while` loop | Jumlah iterasi tidak diketahui | Retry logic, polling, streaming |
| `break` | Ditemukan kondisi kritis, langsung berhenti | Berhenti karena error fatal |
| `continue` | Melewati record yang invalid/tidak relevan | Lewati baris null/rusak |
| `pass` | Placeholder untuk logika yang belum ditulis | Blok TODO |
| Comprehension | Transformasi/filter koleksi secara ringkas | Normalisasi data, bersihkan kolom |

---

## Exercises
## Latihan

1. **Basic:** Write a function that takes a list of numbers and returns a new list with only positive numbers (use list comprehension).

   **Dasar:** Buat sebuah fungsi yang menerima list angka dan mengembalikan list baru berisi hanya angka positif (gunakan list comprehension).

2. **Intermediate:** Create a validation function that takes a list of dictionaries `[{"name": ..., "age": ..., "email": ...}]` and separates valid from invalid records.

   **Menengah:** Buat sebuah fungsi validasi yang menerima list dictionary `[{"name": ..., "age": ..., "email": ...}]` dan memisahkan record yang valid dari yang tidak valid.

3. **Advanced:** Implement a retry pattern for a database connection — try to connect up to 5 times, with a 2-second wait between attempts. Print appropriate messages for success and failure.

   **Lanjutan:** Implementasikan retry pattern untuk koneksi database — coba konek sampai 5 kali, dengan jeda 2 detik antar percobaan. Cetak pesan yang sesuai untuk keberhasilan dan kegagalan.

---

*Continue to the next topic: **Functions and Error Handling** in Python for DE*
*Lanjut ke topik berikutnya: **Functions dan Error Handling** di Python for DE*