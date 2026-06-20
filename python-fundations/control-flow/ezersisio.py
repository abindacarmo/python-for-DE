# exercise number 1
# basic

number = [3, -2, 1, 0]

def show_positive_number(number):
    return [i for i in number if i > 0]

print(show_positive_number(number))



#number 2
#intermediate

dicti = [
    {"name": "Abinda Carmo", "age": 22, "email": "abindacarmo@gmail.com"},
    {"name": "Dito Carmo", "age": 19, "email": "abindacarmo@gmail.com"},
    {"name": "", "age": 18, "email": "abindacarmo@gmail.com"}
]

def validate_record(dicti):
    valid = []
    invalid = []

    for row in dicti:
        if row["name"] == "" or row["age"] < 0 or "@"  not in row["email"]:
            invalid.append(row)
        
        else:
            valid.append(row)
        
    return valid, invalid

valid_result, invalid_result = validate_record(dicti)
print("valid:", valid_result )
print("invalid: ", invalid_result)

    
# example number 3
# advanced


import time

max_retries = 5
attempt = 0

while attempt < max_retries:
    try:
        print("Connection success!")
        break

    except Exception as a:
        attempt += 1
        print(f"try {attempt} fail: {e}")
        time.sleep(2)

if attempt == max_retries:
    print("Fail to Connect after 5 tried!")

