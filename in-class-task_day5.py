# ### In-class Task:

# Write a program to check the input $x$ :

# If $x$ is an even number that is not divisible by 3, print "B" instead, and print "C" instead if yes.

# Instead, if $x$ is not an even number, print "D"

# Test cases:

# $x = 3$ -> D

# $x = 4$ -> B

# $x = 12$ -> C

# $x = 182$ -> B

# $x = 0$ -> C

# $x = -7$ -> D

# $x = 1.5$ -> D

number = float(input())
if number % 2 == 0:
    if number % 3 != 0 :
        print("B")
    else :
        print("C")
else :
    print("D")