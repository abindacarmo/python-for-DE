# Python Basics: Variables, Data Types, and Operations

## Introduction

When learning Python, three fundamental concepts you need to understand are:

1. Variables
2. Data Types
3. Operations

These concepts are the foundation of almost every Python program.

---

# 1. Variables

A variable is a named container used to store data in a program.

Think of a variable as a labeled box where you can keep information and use it later.

## Example

```python
name = "Brigida"
age = 20
```

In this example:

- `name` stores the text `"Brigida"`
- `age` stores the number `20`

## Why Use Variables?

Variables help us:

- Store information
- Reuse data
- Make programs more flexible

Example:

```python
name = "Brigida"

print("Hello", name)
```

Output:

```text
Hello Brigida
```

---

# 2. Data Types

A data type defines the kind of value stored in a variable.

Python automatically determines the data type based on the assigned value.

## Common Data Types

| Data Type | Description | Example |
|------------|------------|---------|
| int | Integer numbers | 10, 25, -3 |
| float | Decimal numbers | 3.14, 2.5 |
| str | Text/String | "Hello" |
| bool | Boolean values | True, False |

## Integer (int)

```python
age = 20
```

## Float (float)

```python
height = 1.65
```

## String (str)

```python
name = "Brigida"
```

## Boolean (bool)

```python
is_student = True
```

## Checking Data Types

```python
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

# 3. Operations

Operations are actions performed on values or variables.

---

## Arithmetic Operations

Arithmetic operations are used for mathematical calculations.

| Operator | Name | Example |
|-----------|------|---------|
| + | Addition | 5 + 2 |
| - | Subtraction | 5 - 2 |
| * | Multiplication | 5 * 2 |
| / | Division | 5 / 2 |
| // | Floor Division | 5 // 2 |
| % | Modulus (Remainder) | 5 % 2 |
| ** | Exponentiation | 5 ** 2 |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Output:

```text
13
7
30
3.3333333333333335
3
1
1000
```

---

## Comparison Operations

Comparison operators compare two values and return either True or False.

| Operator | Meaning |
|-----------|---------|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

### Example

```python
age = 20

print(age > 18)
```

Output:

```text
True
```

---

## Logical Operations

Logical operators combine multiple conditions.

| Operator | Meaning |
|-----------|---------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses a Boolean value |

### Example

```python
age = 20
has_id = True

print(age >= 18 and has_id)
```

Output:

```text
True
```

---

# Complete Example

```python
name = "Brigida"
age = 20

is_adult = age >= 18

print(name)
print(age)
print(is_adult)
```

Output:

```text
Brigida
20
True
```

---

# Summary

- **Variable**: A container used to store data.
- **Data Type**: The type of data stored in a variable.
- **Operation**: An action performed on data.