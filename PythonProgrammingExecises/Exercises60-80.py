### Python Programming Exercises
### Question 60~80

### Question 69 - Generator/yield
"""Please write a program using generator to print the
numbers which can be divisible by 5 and 7 between 0 and
n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:
100

Then, the output of the program should be:

0,35,70


Hints: Use yield to produce the next value in generator.

In case of input data being supplied to the question,
it should be assumed to be a console input.

Solution:"""
def Q69_1(n):
    i = 0
    k = 35 # 5 and 7 are primes, so the n must be divisible by 35
    while True:
        x = i*k

        if x <= n:
            i += 1
            yield x

        else:
            break

def Q69(n):
    s = ""
    for i in Q69_1(n):
        s += f"{i}, "

    print (s[:-2])

print("_"*30, "Question 69", sep='\n')
Q69(100)


### Question 70 - Assert Expression
"""Please write assert statements to verify that
every number in the list [2,4,6,8] is even.

Hints: Use "assert expression" to make assertion.

Solution:"""
def Q70(LIST: list[int]):
    for n in LIST:
        assert n%2 == 0

    print("All number in list are even")

print("_"*30, "Question 70", sep='\n')
Q70([2,4,6,8])


### Question 71 - Evaluate Expression "eval()"
"""Please write a program which accepts basic mathematic
expression from console and print the evaluation result.

Example: If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38

Hints: Use eval() to evaluate an expression.

Solution:"""

def Q71(s:str):
    return eval(s)

print("_"*30, "Question 71", sep='\n')
print(Q71("35+3"))

### Question 72 - Binary Search
"""Please write a binary search function which searches
an item in a sorted list. The function should return the
index of element to be searched in the list.

Hints: Use if/elif to deal with conditions.

Solution:"""

testcase = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

def Q72(sorted_list: list, target):
    lp = 0
    rp = len(sorted_list)-1
    i = None

    while i!=lp and i!=rp:
        i = (lp+rp)//2
        if sorted_list[i] == target:
            return i

        elif sorted_list[i] > target:
            rp = i-1

        elif sorted_list[i] < target:
            lp = i+1
    
print("_"*30, "Question 72", sep='\n')
print(Q72(testcase, 7))


### Question 73