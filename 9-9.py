import re


# Write a def(task1) regular expression that matches a string containing only lowercase letters and digits.
# Input: "hello123"
# Output: True
def task1(string):
    return bool(re.match(r'^[a-z0-9]+$', string))


# Write a def(task2) regular expression that matches a string containing at least one uppercase letter.
# Input: "Hello"
# Output: True
def task2(string):
    return bool(re.match(r'[A-Z]+', string))


# Write a def(task3) regular expression that matches a string containing a valid IPv4 address.
# Input: "192.168.1.1"
# Output: True
def task3(string):
    return bool(re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', string))


# Write a def(task4) regular expression that matches a string containing a valid time in the format of "HH:MM:SS".
# Input: "12:34:56"
# Output: True
def task4(string):
    return bool(re.match(r'^([0-1][0-9]|2[0-3]):([0-5][0-9]){2}$', string))


# Write a def(task5) regular expression that matches a string containing a valid US postal code in the format of "NNNNN" or "NNNNN-NNNN".
# Input: "12345" or "12345-6789"
# Output: True
def task5(string):
    return bool(re.match(r'^\d{5}(?:-\d{4})?$', string))


# Write a def(task6) regular expression that matches a string containing a valid username, with the following criteria:
# only contains lowercase letters, numbers, underscores, and hyphens, and is between 6 and 12 characters long.
# Input: "john_doe-123"
# Output: True
def task6(string):
    return bool(re.match(r'^[a-z0-9_-]{6,12}$', string))


# Write a def(task7) regular expression that matches a string containing a valid credit card number (either 15 or 16 digits, starting with either 4, 5, or 6).
# Input: "4512-3456-7890-1234"
# Output: True
def task7(string):
    return bool(re.match(r'^[456]\d{3}(?:-?\d{4}){3}$', string))


# Write a def(task8) regular expression that matches a string containing a valid social security number (in the format of ###-##-####).
# Input: "123-45-6789"
# Output: True
def task8(string):
    return bool(re.match(r'^\d{3}-\d{2}-\d{4}$', string))


# Write a def(task9) regular expression that matches a string containing a valid password, with the following criteria:
# at least one uppercase letter, one lowercase letter, one digit, one special character (@, #, $, or %), and at least 8 characters long.
# Input: "Passw0rd#"
# Output: True
def task9(string):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$', string))


# Write a def(task10) regular expression that matches a string containing a valid IPv6 address.
# Input: "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
# Output: True.
def task10(string):
    return bool(re.match(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$', string))
