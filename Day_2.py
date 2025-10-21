print('Hello World!')
# comment command --> ctrl + /


# Use functions in Python
# function_name(input1 ,input2) -> input1 & input2 are arguments
print(1,2,'SIX') # 1 2 SIX
print(1,2,'SIX', sep='-')  # sep(separating) is a keyword argument (special input) -> 1-2-SIX
print(1,2,'SIX', sep='tab')  # sep(separating) is a keyword argument (special input) -> 1tab2tabSIX

# Data types
# NUMBERS
# int -> integer -> whole numbers (NO decimal point)
# float -> decimal numbers
# str -> string -> text (enclosed in single or double quotes)
# YES or NO -> bool -> boolean -> True or False
# NONE -> NoneType -> no value

# type(DATA) -> telling me the data type of DATA
print(type(123))        # <class 'int'>
print(type(12.34))      # <class 'float'>
print(type('Hello'))    # <class 'str'>
print(type(True))       # <class 'bool'>
print(type(None))       # <class 'NoneType'>