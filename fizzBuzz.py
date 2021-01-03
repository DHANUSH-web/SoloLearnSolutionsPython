'''
FizzBuzz
-------------------------------------------------------------------------
FizzBuzz is a well known programming assignment, asked during interviews.

The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
It takes an input n and outputs the numbers from 1 to n.
For each multiple of 3, print "Solo" instead of the number.
For each multiple of 5, prints "Learn" instead of the number.
For numbers which are multiples of both 3 and 5, output "SoloLearn".

You need to change the code to skip the even numbers, so that the logic only applies to odd numbers in the range.
Remember, the continue statement can be used to skip a loop iteration.
'''
n = int(input())

for x in range(1, n, 2):
    n1=x%3
    n2=x%5

    if n1==0 and n2!=0:
        print("Solo")
    elif n2==0 and n1!=0:
        print("Learn")
    elif n1==0 and n2==0:
        print("SoloLearn")
    else:
        print(x)
