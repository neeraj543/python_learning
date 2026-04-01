# Day 1 - 30DaysOfPython Challenge

# print(2 + 3)             # addition(+)
# print(3 - 1)             # subtraction(-)
# print(2 * 3)             # multiplication(*)
# print(3 / 2)             # division(/)
# print(3 ** 2)            # exponential(**)
# print(3 % 2)             # modulus(%)
# print(10 // 3)            # Floor division operator(//)
# print(len("HelloWorld"))

# # Checking data types
# print(type(10))          # Int
# print(type(3.14))        # Float
# print(type(1 + 3j))      # Complex number
# print(type('Asabeneh'))  # String
# print(type([1, 2, 3]))   # List
# print(type({'name':'Asabeneh'})) # Dictionary
# print(type({9.8, 3.14, 2.7}))    # Set
# print(type((9.8, 3.14, 2.7)))    # Tuple


## Day two

# first_name = input('What is your name?')
# age = input('What is your age?')
# print(first_name)
# print(age)

# first_name = "neeraj" 
# is_married = True
# print('First_name =', first_name); 
# print(' First_name =', len(first_name))
# print('Is married =', is_married)



num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10


first_name = 'Neeraj'
print(list(first_name))