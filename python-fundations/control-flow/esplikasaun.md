# Python Control Flow — Guide for Data Engineering
**Language: English | Level: Intermediate | Author: Abinda**

---

## Table of Contents

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

### Basic Structure

```python
if condition_1:
    # runs when condition_1 is True
elif condition_2:
    # runs when condition_2 is True
else:
    # runs when all conditions are False
```

### Example: Grade Validation

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

```python
# value_if_true if condition else value_if_false
status = "active" if user_id else "none"

# Use to assign a default value
name = data.get("name") or "Unknown"
```

### Logical Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both must be True | `x > 0 and x < 100` |
| `or` | At least one must be True | `x == 0 or x == 1` |
| `not` | Inverts the condition | `not is_empty` |
| `is` | Compares identity | `val is None` |
| `in` | Checks membership in list/dict | `key in data` |

> **📝 Note — `is` vs `==`:**
> - `==` compares **values** (are the contents the same?)
> - `is` compares **identity** (are they the exact same object in memory?)
>
> ```python
> a = [1, 2, 3]
> b = [1, 2, 3]
> print(a == b)   # True  — same value
> print(a is b)   # False — different objects in memory
>
> # Why use `is None` instead of `== None`?
> val = None
> print(val is None)   # ✅ Correct — recommended (PEP 8)
> print(val == None)   # ⚠️  Works but not recommended
> ```
>
> `None` is a **singleton** in Python — only one `None` object exists in the entire program, so `is` is always accurate and faster.

### Note for Data Engineering

> **Common practice:** `if` is heavily used for column validation, checking null values, or routing data to different tables based on record type.

```python
# Validation example in a pipeline
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

### Basic Structure

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

### Example: Iterate List of Dicts (Rows)

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

```python
from pathlib import Path

# Load all CSV files in a folder
for file in Path("data/").glob("*.csv"):
    print(f"Processing: {file.name}")
    # read the file...
```

### Note for Data Engineering

> **Common practice:** `for row in cursor.fetchall()` to process SQL query results, or `for file in Path(dir).glob("*.csv")` to batch-load files.

---

## 3. while loop

### How does it work?

`while` loop keeps running as long as the condition is `True`. Use it when you don't know exactly how many iterations are needed — e.g. retry logic, polling, or streaming data.

### Basic Structure

```python
counter = 0
while counter < 5:
    print(counter)
    counter += 1  # IMPORTANT: always update the condition!
```

### Infinite Loop with break

```python
while True:
    data = fetch_data()
    if not data:
        break  # stop loop when no more data
    process(data)
```

### Example: Retry Pattern — Common in Pipelines

```python
max_retries = 3
attempt = 0

while attempt < max_retries:
    try:
        result = connect_to_db()
        print("Connection successful!")
        break  # success, exit the loop
    except Exception as e:
        attempt += 1
        print(f"Attempt {attempt} failed: {e}")

if attempt == max_retries:
    print("All retries failed! Please check the connection.")
```

### Example: Polling — Wait for New Data

```python
import time

def pipeline_wait_for_data():
    while True:
        new_records = check_for_new_records()

        if new_records:
            process(new_records)
            print(f"Processed {len(new_records)} records.")
        else:
            print("No new data, waiting...")

        time.sleep(60)  # wait 1 minute before checking again
```

### ⚠️ Important Warning

> **Watch out for infinite loops!** Always make sure the `while` condition will eventually become `False`, or use `break` to exit. Otherwise, the program runs forever until manually stopped.

---

## 4. break / continue / pass

### break — Exit the Loop

Stops the entire loop immediately.

```python
data = [10, 25, None, 42, 8]

for val in data:
    if val is None:
        print("Found null value, stopping process!")
        break
    print(val)

# Output:
# 10
# 25
# Found null value, stopping process!
```

### continue — Skip an Iteration

Skips the current iteration and moves to the next one.

```python
data = [10, None, 25, None, 42]

for val in data:
    if val is None:
        continue  # skip null values
    print(val)

# Output:
# 10
# 25
# 42
```

### pass — Do Nothing

Placeholder — the code does nothing. Use when syntax requires a block but you have no logic yet.

```python
for item in data:
    if item < 0:
        pass  # TODO: handle negative values later
    else:
        process(item)
```

### for...else — Special Structure

The `else` block runs only when the loop finishes **without** hitting `break`.

```python
records = [
    {"id": 1, "error": False},
    {"id": 2, "error": False},
    {"id": 3, "error": False},
]

for row in records:
    if row["error"]:
        print(f"Error found in record {row['id']}")
        break
else:
    print("Validation successful! All records are valid.")

# Output: Validation successful! All records are valid.
```

### Comparison: break vs continue

| | `break` | `continue` |
|---|---|---|
| **Action** | Stops the entire loop | Skips only the current iteration |
| **Code after** | Does not run | Runs in the next iteration |
| **Use when** | Critical condition is found | Skipping invalid/null data |

---

## 5. List, Dict, Set Comprehension

### How does it work?

A compact way to create a new collection from an iteration. More Pythonic and faster than a regular `for` loop.

### Syntax

```python
# [expression for item in iterable if condition]

# List comprehension
squares = [x**2 for x in range(5)]              # [0, 1, 4, 9, 16]
evens   = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Dict comprehension
{key: value.upper() for key, value in data.items()}

# Set comprehension — automatically unique
unique_cities = {row["city"] for row in records}
```

### Comparison: for Loop vs Comprehension

```python
# Version with for loop
result = []
for x in numbers:
    if x > 0:
        result.append(x * 2)

# Version with list comprehension (same result)
result = [x * 2 for x in numbers if x > 0]
```

### DE Example: Data Transformation

```python
records = [
    {"id": 1, "name": "  Ana  ", "score": None},
    {"id": 2, "name": "Budi",    "score": 88},
    {"id": 3, "name": "Cici",    "score": 72},
]

# Filter invalid records and strip whitespace
valid = [
    {"id": r["id"], "name": r["name"].strip()}
    for r in records
    if r["score"] is not None
]

# Result: [{"id": 2, "name": "Budi"}, {"id": 3, "name": "Cici"}]
```

### DE Example: Dict Comprehension for Normalization

```python
# Normalize all column names (lowercase and strip whitespace)
raw_data = {"Name ": "ANA", " City": "DILI", "Score ": "85"}

clean_data = {
    key.strip().lower(): value.strip().title()
    for key, value in raw_data.items()
}

# Result: {"name": "Ana", "city": "Dili", "score": "85"}
```

### Generator Expression

```python
# Like list comprehension but uses () — does NOT create the full list in memory
# Efficient for large datasets

total = sum(row["value"] for row in records if row["value"] is not None)
```

> **Note:** Use a **generator** (with `()`) for large data — it doesn't load everything into memory at once. Use **list comprehension** (with `[]`) when you need to access elements multiple times.

---

## 6. Real DE Use Cases

### Complete ETL Pattern

```python
def process_etl(raw_data: list) -> tuple[list, list]:
    """
    ETL pipeline example with complete control flow.

    Params:
        raw_data: List of records from a data source

    Returns:
        (valid_results, error_list)
    """
    results = []
    errors  = []

    for i, row in enumerate(raw_data):

        # === VALIDATION ===

        # Check missing ID
        if row.get("id") is None:
            errors.append({"row": i, "reason": "ID is missing"})
            continue

        # Check null value
        if row.get("value") is None:
            errors.append({"row": i, "id": row["id"], "reason": "Null value"})
            continue

        # Check value range
        if not (0 <= row["value"] <= 10000):
            errors.append({"row": i, "id": row["id"], "reason": "Value out of range"})
            continue

        # === TRANSFORMATION ===

        # Categorize based on value
        if row["value"] > 8000:
            category = "premium"
        elif row["value"] > 4000:
            category = "standard"
        else:
            category = "basic"

        # Normalize string
        clean_name = row.get("name", "").strip().title() or "Unknown"

        # Build new record
        new_record = {
            "id":       row["id"],
            "name":     clean_name,
            "value":    row["value"],
            "category": category,
        }
        results.append(new_record)

    return results, errors


# Use the function
raw_data = [
    {"id": 1,    "name": "  tasi mane  ", "value": 9000},
    {"id": 2,    "name": "Dili port",      "value": 3500},
    {"id": None, "name": "Manufahi",       "value": 6000},   # error: ID missing
    {"id": 4,    "name": "Baucau",         "value": None},   # error: null value
    {"id": 5,    "name": "Viqueque",       "value": 12000},  # error: out of range
]

valid_records, error_list = process_etl(raw_data)

print(f"✅ Valid:  {len(valid_records)} records")
print(f"❌ Errors: {len(error_list)} records")

for e in error_list:
    print(f"  - Row {e['row']}: {e['reason']}")
```

### Expected Output

```
✅ Valid:  2 records
❌ Errors: 3 records
  - Row 2: ID is missing
  - Row 3: Null value
  - Row 4: Value out of range
```

### Batch File Loading with Retry

```python
import time
from pathlib import Path

def batch_load_files(folder: str, max_retries: int = 3):
    """Load all CSV files in a folder with retry logic."""
    success = []
    failed  = []

    for file in Path(folder).glob("*.csv"):
        attempt = 0

        while attempt < max_retries:
            try:
                data = read_csv(file)
                success.append(file.name)
                print(f"✅ {file.name} — success")
                break
            except Exception as e:
                attempt += 1
                print(f"⚠️  {file.name} attempt {attempt}: {e}")
                time.sleep(2)
        else:
            # Runs only when while ends without break (all retries failed)
            failed.append(file.name)
            print(f"❌ {file.name} — failed after {max_retries} attempts")

    return success, failed
```

---

## Quick Summary

| Concept | Use when | DE Example |
|---------|----------|------------|
| `if/elif/else` | Need to make decisions based on a condition | Validate columns, route data |
| `for` loop | Number of iterations is known, iterating a sequence | Process rows, batch load files |
| `while` loop | Number of iterations is unknown | Retry logic, polling, streaming |
| `break` | Critical condition is found, stop immediately | Stop on fatal error |
| `continue` | Skip invalid or irrelevant records | Skip null/bad rows |
| `pass` | Placeholder for logic not yet written | TODO blocks |
| Comprehension | Transform/filter a collection simply | Normalize data, clean columns |

---

## Exercises

1. **Basic:** Write a function that takes a list of numbers and returns a new list with only positive numbers (use list comprehension).

2. **Intermediate:** Create a validation function that takes a list of dictionaries `[{"name": ..., "age": ..., "email": ...}]` and separates valid from invalid records.

3. **Advanced:** Implement a retry pattern for a database connection — try to connect up to 5 times, with a 2-second wait between attempts. Print appropriate messages for success and failure.

---

*Continue to the next topic: **Functions and Error Handling** in Python for DE*


