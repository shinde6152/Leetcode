
#       write a program to check string


def check_pallindrome(str1):
    str2 = str1[::-1]
    if str1 == str2:
        print("pallindrome", str1)

check_pallindrome(input())
