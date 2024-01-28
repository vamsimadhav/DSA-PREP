## Read input as specified in the question.
## Print output as specified in the question.

val = input()

if (val >= 'A' and val <= 'Z'):
    print(1)
elif val >= 'a' and val <= 'z':
    print(0)
else:
    print(-1)



"""
Learnings
In Python we can't cast to `int` data type directly, for it we have `ord()` and `chr()' functions
ord -> Gives the ascii value
chr -> Gives the character value

"""
