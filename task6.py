# 🟡 Intermediate Level
# Write a function to find the largest number in a list.

list1 = [1,3,7,0,8,2,5,9,6]
def max_value(x):
    max = list1[0]
    for num in list1:
        if max < num:
            max = num
    return max
print("The maximum value is: ",max_value(list1))

print("---------"*10)
# Write a function to find the smallest number in a list.

list1 = [1,3,7,8,2,5,9,6,-1]
def min_value(x):
    min = list1[0]
    for num in list1:
        if min > num:
            min = num
    return min
print("The minimum value is: ",min_value(list1))

print("---------"*10)
# Create a function to count the number of vowels in a string.

str1 = "Student"
def count_vowel(str1):
    vowel = 0
    consonant = 0
    for i in str1:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vowel += 1
        else:
            consonant += 1
    return vowel, consonant
print("The vowel and consonant letters are: ", count_vowel(str1))

print("---------"*10)
# Write a function to calculate factorial of a number.

def fact(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial
print("The factorial of a number is: ", fact(5))

print("---------"*10)
# Create a function to check if a number is prime.

def check_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
n = int(input("Enter the number: "))
if check_prime(n):
    print(f"The number is prime")
else:
    print("The number is not prime")

print("---------"*10)
# Write a function to reverse a string.

def rev_str(str1):
    rev = ""
    for char in str1:
        rev = char + rev
    return rev
str1 = input("Enter any string: ")
print("The reverse of the string: ",rev_str(str1))

print("---------"*10)
# Write a function to check if a string is a palindrome (same forward and backward)

def is_palindrome(str2):
    rev = ""
    for char in str2:
        rev = char + rev
    return rev == str2

print("Palindrome: ", is_palindrome("hello"))