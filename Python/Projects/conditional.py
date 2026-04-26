age = 16

if age >= 18:
    print("You are an adult.")
else: 
    print("You are a minor.")

grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")

"""
| Operator | Description           | Example           | Result |
| -------- | --------------------- | ----------------- | ------ |
| `==`     | Equal                 | `5 == 5`          | True   |
| `!=`     | Not equal             | `5 != 3`          | True   |
| `>`      | Greater than          | `10 > 2`          | True   |
| `<`      | Less than             | `2 < 5`           | True   |
| `>=`     | Greater or equal      | `7 >= 7`          | True   |
| `<=`     | Less or equal         | `4 <= 5`          | True   |
| `and`    | Both conditions true  | `x > 0 and y > 0` |        |
| `or`     | Either condition true | `x > 0 or y > 0`  |        |
| `not`    | Negates a condition   | `not x > 10`      |        |
"""

name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 13:
    print(f"Hello {name}! You are a kid!")
elif age < 20:
    print(f"Hello {name}! You are a teenager!")
else:
    print(f"Hello {name}! You are an adult!")