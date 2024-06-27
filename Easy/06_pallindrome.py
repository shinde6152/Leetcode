#           write a program to check number is pallindrome or not




def rev_int(num):
    reverser_num = int(str(num)[::-1])
    return reverser_num

def check_pallindrome(num):
    num2 = rev_int(num)
    if num == num2:
        print("number is pallindrome",num)
        return check_pallindrome(int(input()))
    else:
        print("Enter correct pallindrome")
        return check_pallindrome(int(input()))


check_pallindrome(int(input()))