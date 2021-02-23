import re
import sys

def validate_phone_number(phone_number):
    regex1 = '([0]?((77)|(55)|(91)|(99)|(98))[0-9]{6})|([0]?((77)|(55)|(91)|(99)|(98))[\- ]?[0-9]{2}[\- ][0-9]{2}[\- ][0-9]{2})|([0]?((77)|(55)|(91)|(99)|(98))[\- ]?[0-9]{3}[\- ]?[0-9]{3})'
    if re.fullmatch(regex1, phone_number):
        return True
    else:
        return False


def validate_email(email):
    regex2 = '^[a-zA-Z0-9]+[\.+_]?[a-zA-Z0-9]+[\@][a-z]*[\.][a-z]+'
    if re.fullmatch(regex2, email):
        return True
    else:
        return False


if __name__ == '__main__':
    phone_number = input("Enter a phone number: ")
    email = input("Enter an email: ")
    if validate_phone_number(phone_number):
        print("Yes")
    elif validate_phone_number(phone_number) == False:
        print("No")
    if validate_email(email):
        print("Yes")
    elif validate_email(email) == False:
        print("No")