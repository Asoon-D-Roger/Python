# '''Given an integer input the objective is to write a program to Check Whether a
# Number is a Prime or Not'''

# Example 1:
# Input : 11

# Example 2:
# Input : 5

# Example 3:
# Input : 10

# Sol:

def prime(num):
    if num <= 1:
        return False
# 'm using this cuz prrime num are divisible by 1 or by the num itself
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if prime(num):
    print(f"{num} is a Prime")

else:
    print(f"{num} is not a Prime")


# --------------------------------------------------------------------------------------------