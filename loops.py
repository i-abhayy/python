#Write a program using for loop to print numbers from 1 to 5
for i in range(1,6):
    print(i)

#Write a program using for loop to print even numbers from 2 to 10
for i in range(2,11,2):
    print (i)

#Write a program using for loop to find sum of numbers from 1 to 10
sum=0
for i in range(1,11):
    sum+=i
print(sum)

#Write a program using for loop to: print table of a number (e.g., 5)
mul=5
for i in range(1,11):
 print(mul,"x",i,"=",mul*1)

#Write a program using for loop to count how many numbers from 1 to 20 are divisible by 3
count=0
for i in range(1,21):
   if i%3==0:
      count+=1
print( count)

#Write a program to find the factorial of a number (n = 5)\
fac= 1
for i in range(1,6):
   fac*=i
print(fac)

#Write a program to: reverse a number using for loop
num = int(input("Enter a number: "))
temp = num
reverse = 0

# count digits first
count = 0
t = num
while t > 0:
    t //= 10
    count += 1

for i in range(count):
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print(reverse)

#Write a program using for loop to:check whether a number is prime
num= int(input("enter the number"))
if num<=1:
   print("not prime")
else:
   print("prime")

   for i in range(2,num):
      if num%i==0:
         is_prime= False
         break
if is_prime:
   print("prime")
else:
   print("not prime")

#Write a program using for loop to:print all prime numbers from 1 to 20
for i in range(1,21):
   if i<=1:
      continue
   is_prime=True
   for j in range(2,i):
         if i%j==0:
            is_prime= False
            break
   if is_prime:
         print("i")

#Write a program to:count how many prime numbers are between 1 and 50
count= 0 
for i in range (1,51):
   if i<=1:
      continue
   is_prime=True
   for j in range(2,i):
         if i%j==0:
            is_prime= False
            break
   if is_prime:
    count+=i
print(count)

#Print numbers from 1 to 5 using while loop
i=1
while i<=5:
   print(i)
   i+=1
 
#Write a program using while loop to: find sum of numbers from 1 to 10
i=1
total = 0
while i<=10:
   total+=i
   i+=1
   print(total) 
#Write a program using while loop to:reverse a number
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)


   



