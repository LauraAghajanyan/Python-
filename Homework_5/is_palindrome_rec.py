def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-2])
        else:
            return False


s = input("Input a string: ")
if palindrome(s):
    print("Yes")
else:
    print("No")


