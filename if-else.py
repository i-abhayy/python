'''program1'''
x=10
if(x%2==0):
    print("x is even")
else:
    print("x is odd")

'''program2'''
x=25
if(x>0):
    print(" number is positive")
else:
    print("number is negative")

'''program3'''
markss = int(input("enter your marks:"))
if(markss>=90):
    print("grade is A")
elif(markss>=70):
    print("grade is b")
else:
    print("grade is c")

'''program4'''
x=int(input("enter a number:"))
if(x%3==0 and x%5==0):
    print("fizzBuzz")
elif x%3==0:
    print("fizz")
elif x%5==0:
    print("buzz")
else:
    print(x)

'''program5'''
x=int(input("enter year:"))
if x%4==0 and x%100!=0 or x%400==0:
  print("leap year") 
else:
    print("not a leap year")

'''program6'''
num1 = int(input("enter num 1 : "))
num2=int(input("enter number 2: "))
num3=int(input("enter number 3: "))
if num1>=num2 and num1>=num3:
    print("num1 is largrest")
elif num2>=num1 and num2>=num3:
    print("num2 is largest")
else:
    print("num3 is largest")
 
 #program 7
num = int(input("enter a number:"))
if num>0:
    if num%2==0:
        print("number is positive and even")
    else:
        print("number is odd and positive")
elif num<0:
    if num%2==0:
        print("number is negative and even")
    else:
        print("number is negative  and odd")
else:
    print("number is zero")

#program 8
letr= chr(input("enter a character"))
if 'A'<=letr<='Z':
    print("letter is uppercase")
elif 'a'<= letr <='z':
    print("lette is lower case")
elif '0'<= letr <='9':
    print("letter is a digit")
else:
    print("leter is special symbol")

#program 9
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
#program 10
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10        # get last digit
    reverse = reverse * 10 + digit
    num = num // 10         # remove last digit

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")

# program 11
a= int(input(" enter side a :"))
b= int(input(" enter side b:"))
c= int(input("enter side b:"))
if a==b==c:
    print("triagnle is euilateral")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid Triangle")
elif a==b and b==c and c==a:
    print ("triagnle is isosceles")
else:
    print("triangle is scalene")

#program 12 
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Leap year check
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = True
else:
    leap = False

# Month logic
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    if leap:
        print("29 days")
    else:
        print("28 days")
else:
    print("Invalid month")

#program 13
num = int(input("Enter a number: "))
original = num

# Step 1: Count digits
temp = num
count = 0

while temp > 0:
    temp = temp // 10
    count += 1

# Step 2: Calculate Armstrong sum
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** count
    temp = temp // 10

# Step 3: Check result
if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

