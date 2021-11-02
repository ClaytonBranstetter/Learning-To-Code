'''
Author: Clayton Branstetter
KUID: 3089206
Date: 11/01/2021
Lab: lab#06
Last modified: 11/01/2021
Purpose: Functions
'''

# In[47]:


def last_digit(num):
    return num % 10


def remove_last_digit(num):
    if(num <= 9):
        return 0
    else:
        ch = str(num)
        ch = ch[:-1]
        return int(ch)


def add_digit(current_num, new_digit):
    n = str(current_num)+str(new_digit)
    return int(n)


def reverse(n):
    L = []
    for i in range(len(str(n))):

        L.append(last_digit(n))
        n = remove_last_digit(n)
    ch = ""
    for e in L:
        ch = ch+str(e)

    return int(ch)


def isPalindrome(num):
    x = reverse(num)
    if(x == num):
        return True
    else:
        return False


def count_digits(n):
    s = 1
    while(n//10 != 0):
        n = n//10
        s = s+1
    return s


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def print_menu():

    print(" 1) Count digits \n")
    print(" 2) Sum digits \n")
    print(" 3) Is Palindrome \n")
    print(" 4) Reverse \n")
    print(" 5) Exit \n")


# In[127]:


def main():

    print_menu()
    n = int(input("Please Choose from the menu\n"))
    while(n != 5):

        x = int(input("Enter The number desired: "))
        if(n == 1):
            print("The desired result is :", count_digits(x))
        elif(n == 2):
            print("The desired result is :", sum_digits(x))
        elif(n == 3):
            print("The desired result is :", isPalindrome(x))
        elif(n == 4):
            print("The desired result is :", reverse(x))
        print_menu()
        n = int(input("Please Choose Again: \n"))

    if(n == 5):
        print("We will quit the menu now")


# In[128]:
main()
