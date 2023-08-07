def check_string_properties(s):
    # Check if the string has any alphanumeric characters
    is_alnum = False
    for char in s:
        if char.isalnum():
            is_alnum = True
            break

    # Check if the string has any alphabetical characters
    is_alpha = False
    for char in s:
        if char.isalpha():
            is_alpha = True
            break

    # Check if the string has any digits
    is_digit = False
    for char in s:
        if char.isdigit():
            is_digit = True
            break

    # Check if the string has any lowercase characters
    is_lower = False
    for char in s:
        if char.islower():
            is_lower = True
            break

    # Check if the string has any uppercase characters
    is_upper = False
    for char in s:
        if char.isupper():
            is_upper = True
            break

    return is_alnum, is_alpha, is_digit, is_lower, is_upper

# Read input string
input_string = input().strip()

# Call the function and print the output
result = check_string_properties(input_string)
for value in result:
    print(value)
