def square(x):
    """
    This is a demo function
    Where in you just return square of the number
    args:
        x (int)
    returns:
        y (int)
    ex:
        x = 5
        ## then
        y = 25
    """

    def square(x):
        y=x**2
        return y
        print(square(5))


def word_is_palindrome(string):
    """
    This function returns True if the given string is
    a Palindrome
    args:
        string (str)
    returns:
        flag (bool)
    ex:
        string = 'abcba'
        ## then
        flag = True
    """
my_str = 'aIbohPhoBiA'
my_str = my_str.casefold()
if my_str == my_str[::-1]:
    print("True")
else:
    print("False")
    


def sqrt_of_numbers(num):
    """
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float) rounded off upto 2 decimal places.
    ex:
        num = 27
        ## then
        sqroot = 5.20
    """
    if num < 0:
        raise ValueError('Number must be positive')

        
def sqrt_of_numbers(x):
    y=x**(1/2)
    return y
print(sqrt_of_numbers(27))

def Maximum(arr):
    """
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    ex:
        arr = [1, 2, 3, 4, 5]
        ## then
        Max1, Max2 = 5, 4
    """

def maximum(arr):
    sorted(arr)
    print("max1,max2")
    return arr[-1],arr[-2]
print(maximum(arr=[1,2,3,4,5]))


def even_sort(arr):
    """
    This function sorts the array giving higher preference to even numbers
    args:
        arr (list)
    returns:
        sort_arr (list)
    ex:
        arr = [15, 2, 6, 88, 7]
        ## then
        sort_arr = [2, 6, 88 ,7 ,15]
        ## This is any even number is smaller than any odd number
    """

def even_sort(arr):
    sorted(arr)
    newarray1=[]
    newarray2=[]
    for i in arr:
        if i%2==0:
            newarray1.append[i]
        else:
            newarray2.append[i]
    return  newarray1 + newarray2
print(even_sort(arr=[1,2,3,4,5]))     
    


def eqn_solver(A, B, C):
    """
    This function solves a two variable system
    i.e.,
        A = [ 1, 2 ]
        B = [ 3, 4 ]
        C = [ 5, 6 ]
        then it means
        1x + 3y = 5
        2x + 4y = 6
        Hence you are required to find x, y for such a linear system
    args:
        A, B, C (list, list, list) representing coefficients in the equation
    returns:
        x, y (float, float)
    """



def swap_case(string):
    """
    This function swaps the case of the string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string = 'Hello World'
        ## then
        string = 'hELLO wORLD'
    """
def swap_case(string):
    
    newstring = string.swapcase()
    return newstring
print(swap_case(string="asDFgh"))


def is_prime(num):
    """
    This function returns True if the number is prime
    args:
        num (int)
    returns:
        flag (bool)
    """
num = 57
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print("False")
            break
    else:
        print(num, "")
else:
    print("False")



def is_leap_year(year):
    """
    This function returns True if the year is leap year
    args:
        year (int)
    returns:
        flag (bool)
    """

year = 2000
if (year % 400 == 0) and (year % 100 == 0):
    print("True")
elif (year % 4 ==0) and (year % 100 != 0):
    print("True")
else:
    print("False")


def is_perfect_square(num):
    """
    This function returns True if the number is perfect square i.e. it is a square of some integer.
    args:
        num (int)
    returns:
        flag (bool)
    """

    # Code Here
    return None


def is_perfect_number(num):
    """
    This function returns True if the number is perfect number.
    A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
    For example 6 is a perfect number because 1+2+3 = 6
    args:
        num (int)
    returns:
        flag (bool)
    ex:
        num = 6
        ## then
        flag = True

        num = 7
        ## then
        flag = False
    """
def is_Perfect( n ):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n/i
        i += 1
    return (True if sum == n and n!=1 else False)
print(is_Perfect( 28 ))



def resize_array(a):
    """
    This function resizes a 1D array to 2D array of size 2x3
    args:
        a (np.array) of size 1x6
    returns:
        b (np.array) of size 2x3
    ex:
        a = np.array([1, 2, 3, 4, 5, 6])
        ## then
        b = np.array([[1, 2, 3], [4, 5, 6]])
    """

import numpy as np
arr1 = np.array([1,2,3,4,5,6])
arr2 = arr1.reshape((3,2))
arr2


def reverse_step_array(a):
    """
    This function returns the reversed array with step size of 3.
    args:
        a (np.array)
    returns:
        b (np.array)
    ex:
        a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        ## then
        b = np.array([9, 6, 3])
    """
def reverse_words(s):
    str = " "
    for i in s:
        str = i + str
    return str
print(reverse_words(s = 'World Again Hello'))


def reverse_words(string):
    """
    This function reverses the words in the string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string = 'Hello Again World'
        ## then
        string = 'World Again Hello'
    """

    # Code Here
    return None


def count_characters(string):
    """
    This function counts the frequency of characters(ignore spaces as characters) in the input string.
    args:
        string (str)
    returns:
        dict (dict)
    ex:
        string = 'Hello World'
        ## then
        dict = {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1}
    """

input_string = 'Hello World'
mySet = set(input_string)
for element in mySet:
    countOfChar = 0
    for character in input_string:
        if character == element:
            countOfChar += 1
    print("'{}' = {}".format(element, countOfChar))


def remove_special_characters(string):
    """
    This function removes the special characters from the input string. Special characters are those which are not letters or numbers.
    args:
        string (str)
    returns:
        string (str)
    ex:
        str = 'Hello, World! 123$ th15 1s 4 t35t str1ng'
        ## then
        str = 'Hello World 123 th15 1s 4 t35t str1ng'
    """

string = 'Hello World'
print(string)
string2 = string.replace('o', "")
print(string2)


def sort_tuple_of_tuples(input_tuple):
    """
    This function sorts the input tuple of tuples by the second item.
    args:
        input_tuple (tuple)
    returns:
        input_tuple (tuple)
    ex:
        input_tuple: (('a', 55), ('z', 1), ('f', 37), ('w', 19))
        ## then
        input_tuple: (('z', 1), ('w', 19), ('f', 37), ('a', 55))
    """

def last(n): return n[1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([('a', 55), ('z', 1), ('f', 37), ('w', 19)]))



def alpha_numeric_words(string):
    """
    This function finds words with both alphabets and numbers from an input string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string: "Hey there33 how11 are you1"
        ## then
        string: "there33 how11 you1"
    """

test_str = 'Hey there33 how11 are you1'
print("The original string is : " + test_str)
res = []
temp = test_str.split()
for idx in temp:
    if any(chr.isalpha() for chr in idx) and any(chr.isdigit() for chr in idx):
        res.append(idx)
str2 = str(res)
print(str2)
print("Words with alphabets and numbers : " + str(res))


def count_them_all(string):
    """
    This function counts all letters, digits, and special symbols from an input string.
    args:
        string (str)
    returns:
        dict (dict)
    ex:
        string: "IdDk3837#$fsd%%"
        ## then
        dict: {'Characters': 7, 'Numbers': 4, 'Symbols': 4}
    """



def hash_supremacy(string):
    """
    This function replaces each special symbol with '#' in the input string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string: "&He was a^%$ great @guy"
        ## then
        string: "#He was a### great #guy"
    """

string = "&He was a^%$ great @guy"
print(string)
import re
string2 = re.sub("[^A-Za-z, ]", "#",string)
print(string2)
