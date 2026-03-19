'BASIC PROGRAMS IN PYTHON'
'''What will be the output of:
x = 5, y = 2, print(x / y)

What is the data type of:
x = "10"

Convert the following into integer:
x = "25"

Find the error (if any):
name = Abhay
print(name)

What will be the output of:
a = 10, b = 3, print(a // b)

What is the difference between:
"5" + "5"
and
5 + 5

What will be the output of:
x = True, y = False, print(x + y)

Identify the data type of:
x = (1, 2, 3)

What will this print:
print(type(3.0))

What will be the output of:
name = "Abhay", age = 19
print("My name is", name, "and I am", age)'''


'''PROGRAM =1'''
X=5
Y=2
print(X/Y)

'''PROGRGRAM=2'''
x=10
print(type(x))

'''PROGRAM=3'''
x="25"
y=int(x)
print(y)

'''PROGRAM=4'''
name= "abhay"
print(name)

'''PROGRAM=5'''
a=10
b=3
print(a//b)
'''Using // applies flooring, so it drops the decimal part and returns 3 (an integer in this case) because both operands are integers.'''

'''PROGRAM=6'''
"5"+"5"
5+5
'''first one is string so it will print 55 in string and seoond one is integer so it will print 10 in integer'''

'''PROGRAM=7'''
x=True
y=False
print(x+y)
'''In Python, the boolean values True and False are treated as integers when used in arithmetic operations. True is equivalent to 1 and False is equivalent to 0. Therefore, when you add True (1) and False (0), the result is 1.'''

'''PROGRAM=8'''
print(type(3.0 ))
'''it will print <class 'float'> because 3.0 is a floating-point number in Python.'''

'''PROGRAM=9'''
name = "Abhay"
age = 19
print("My name is", name, "and I am", age)

'''PROGRAM=10'''
x = 10
print("Value is: " + x)
'''This code will raise a TypeError because you cannot concatenate a string ("Value is: ") with an integer (x) directly. To fix this, you can convert the integer to a string using the str() function:'''