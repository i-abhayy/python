'''THEORY (Quick but Complete)

Type casting means converting one data type into another.

1. Types of Casting

Implicit Casting: Python automatically converts one data type to another. Example: int + float → float

Explicit Casting: Manually converting using functions like:

int()

float()

str()

bool()

2. Common Conversions

String to Int: int("10") → 10

String to Float: float("10.5") → 10.5

Int to Float: float(10) → 10.0

Int to String: str(10) → "10"

3. Important Rules

int() removes decimal, does not round.

float() works with numeric strings.

bool() depends on emptiness:

0, "", [], () → False

Non-zero, non-empty → True

input() always returns string.

4. Truthy and Falsy Values

Falsy values:

0

""

[]

None

False

Everything else is Truthy.

5. Common Errors

ValueError: invalid conversion (int("abc"))

TypeError: unsupported operation ("10" + 5)

6. Special Cases

" 45 " → valid for int()

"12.5" → cannot directly convert to int

"False" → bool("False") = True (non-empty string)'''


'''# Python Type Casting – Questions Set

1. Convert a string "50" into an integer and store it.

2. Convert a float value 25.7 into an integer.

3. Convert an integer 100 into a string and concatenate it with "Score: ".

4. Convert a string "45.7" into an integer using proper steps.

5. Convert a boolean value True into an integer.

6. Convert "True" and "False" strings into actual boolean values correctly.

7. Convert an empty string "" into a boolean.

8. Convert the integer 0 into a boolean.

9. Convert a list [1, 0, 9] into a boolean.

10. Convert the string "0" into a boolean such that final result becomes True.

11. Take user input and safely convert it into integer. If conversion fails, store 0.

12. Convert the string "12.8" into an integer.

13. Convert the string " 45 " (with spaces) into an integer.

14. Take user input and convert it into integer. If input is empty, store -1.

15. Add "10" (string) and 5.5 (float) and store result as float.

16. Take input (string number), convert to integer and check if number > 50. Store True/False.

17. Take 3 numbers as input (strings), convert into integers and store in a list.

18. Take multiple numbers as input in one line and convert them into a list of integers.

19. Convert string "0" into boolean using logic.

20. Convert price "199.9" into integer (remove decimal).
'''

'''Program 1'''
x = "50" 
y = int(x)

'''Program 2'''
x = 25.7 
y = int(x)

'''Program 3'''
x = 100 
result = "Score: " + str(x)

'''Program 4'''
x = "45.7" 
y = float(x) 
z = int(y)

'''Program 5'''
is_on = True 
x = int(is_on)

'''Program 6'''
x = "True"
y = "False" 
a = (x.lower() == "true")
b = (y.lower() == "true")

'''Program 7'''
x = "" 
is_on = bool(x)

'''Program 8'''
x = 0 
is_on = bool(x)

'''Program 9'''
nums = [1, 0, 9] 
is_on = bool(nums)

'''Program 10'''
x = "0" 
a = bool(int(x) + 1)

'''Program 11'''
try: age = int(input("Enter age: ")) 
except: age = 0

'''Program 12'''
x = "12.8" 
z = int(float(x))

'''Program 13'''
x = int(" 45 ")

'''Program 14'''
age_input = input("Enter age: ")
try:
    age = int(age_input)
except:
    age = -1

'''Program 15'''
x = "10" 
y = 5.5 
result = int(x) + y

'''Program 16'''
age = int(input("Enter age: ")) 
result = age > 50

'''Program 17'''
nums = [ int(input("Enter number 1: ")), 
        int(input("Enter number 2: ")), 
        int(input("Enter number 3: ")) ]

'''Program 18'''
nums = list(map(int, input("Enter numbers: ").split()))

'''Program 19'''
x = "0" 
a = (x == "0")

'''Program 20'''
price = "199.9"
price_int = int(float(price)) 