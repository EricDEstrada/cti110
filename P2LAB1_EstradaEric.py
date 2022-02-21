user_int = int(input('Enter integer (32 - 126):\n'))

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
user_float = (input('Enter float:\n')) #reads float
user_char = (input('Enter character:\n')) #reads characters
user_str = (input('Enter string:\n')) #reads string
print(user_int,user_float,user_char,user_str,) #Should print out with spaces between
# FIXME (2): Output the four values in reverse
print(user_str,user_char,user_float,user_int) #Prints in reverse
# FIXME (3): Convert the integer to a characer, and output that character
print(str(user_int) + " converted to a character is " + chr(user_int))