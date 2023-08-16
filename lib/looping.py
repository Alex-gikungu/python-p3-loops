#!/usr/bin/env python3
def happy_new_year():
    for count in range(10, 0,-1):
        print(count)
    print("Happy New Year!")

happy_new_year()


def square_integers(int_list):
    for sum in range(1,6,+1):
        print(sum**2) 

square_integers(sum)      


def square_integers(int_list):
    squared_list = []  
    for num in int_list:
        squared_list.append(num ** 2) 
    return squared_list


result = square_integers([1, 2, 3, 4, 5])
print(result)  



def fizzbuzz():
    for num in range(1, 101): 
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()






