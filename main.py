# Justin Goff
# CIS 261
# WK8 Lab 1: Iteration and Recursion


def iteration(x):
    total = 1
    for i in range(2,x+1):
        total *= i;
    return total

def recursion(x):
    if x <= 1:
        return 1
    else:
        return(x * recursion(x-1))


print("Factorial results using an iterative function")
print(f"0! = {iteration(0)}\n5! = {iteration(5)}\n10! = {iteration(10)}\n25! = {iteration(25)}\n50! = {iteration(50)}\n100! = {iteration(100)}")
print("Factorial results using a recursive function")
print(f"0! = {recursion(0)}\n5! = {recursion(5)}\n10! = {recursion(10)}\n24! = {recursion(25)}\n50! = {recursion(50)}\n100! = {recursion(100)}")