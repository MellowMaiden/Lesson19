#Lesson 19
#Range(10)=these are the numbers from 0 to 9

#Example 1 :write a program taht prints from 0 to 9
for x in range(10):# x starts at 0 and finished at 9
    print(x)# this line is repeated , starting at 0 and finished at 9

#Example 2:
for x in range(5):
    print("Hello")#这个会打印五次hello

#Examle 3: write a program that prints the suqare numbers , starting at 1 and ending at 100
for x in range(1,11):
    print(f"{x} squared is {x**2}")

#Example 4: write a program that print the even numbers  starting at 2 and finishing on 100.
#There are two ways to do this
#First way
for x in range(1,51):
    print(2*x)
#Second way
for x in range(1,101):
    if x%2 == 0:
        print(x)

#Example 5: write a program that calculates 1+2+3+...+99+100.
total = 0
for N in range(1,101):
    total += N
print(total)

#Example 6:
P = 1
for n in range(1,6):
    P *= n
print(P)

#Example 7:
def factorial(N):
    P=1
    for n in range(1,N+1):
        P*=n
    return(P)
print(factorial(6))

#Example 8:
name = ""
sign = -1
for x in "Stephen":
    sign *=-1
    if sign ==1:
        name += x.upper()
    else:
        name += x.lower()
print(name)
