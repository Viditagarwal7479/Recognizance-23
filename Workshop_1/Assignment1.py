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

    y=x*x
    return y


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
    if string == string[::-1]:
        flag=True
    else:
        flag=False
    return flag


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
    else:
        return round(num**0.5,2)


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

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)-2):
            if(arr[j]>=arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
            
    return arr[len(arr)-1],arr[len(arr)-2]


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
    even = []
    odd = []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    even.sort()
    odd.sort()
    return even + odd


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

    det= A[0]*B[1]-A[1]*B[0]
    if(det==0):
        return None, None
    
    else:
        x=-((C[1]*B[0]-C[0]*B[1])/det)
        y=((C[1]*A[0]-C[0]*A[1])/det)
        return x,y

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
    new_str=""
    for i in string:
        if(i.upper())==i:
            new_str+=i.lower()
        else:
            new_str+=i.upper()
    return new_str


def is_prime(num):
    """
    This function returns True if the number is prime
    args:
        num (int)
    returns:
        flag (bool)
    """
    if num>1:
        for i in range(2,int(num/2+1)):
            if (num%i)==0 :
                return False
                break
          
    else:
        return True


def is_leap_year(year):
    """
    This function returns True if the year is leap year
    args:
        year (int)
    returns:
        flag (bool)
    """

    if year%4 !=0:
        flag = False

    else:
        if year%100 !=0:
            flag = True
        else:
            if year%400 ==0:
                flag = True
            else:
                flag = False
    return flag


def is_perfect_square(num):
    """
    This function returns True if the number is perfect square i.e. it is a square of some integer.
    args:
        num (int)
    returns:
        flag (bool)
    """

    for i in range (2,num):
        if i**2==num :
            return True
    return False


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
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return True
    else:
        return False

import numpy as n
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
    
    b=n.reshape(a,(2,3))
    return b

import numpy as np
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

    
    b=[]
    rev=np.flip(a)
    n=len(a)
    for i in range(0,n-1):
        if i%3==0:
            b.append(rev[i])
            
    return b

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
    s = string.split()[::-1]
    split_s=[]
    for i in s:
        split_s.append(i)
    new_str=" ".join(split_s)
    return new_str


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

    # Code Here
    dict={}
    n=len(string)
    for i in string:
        if i!=0 and i!=' ':
            dict[i]=0
    for i in string:
        if i!=0 and i!=' ':
            dict[i]=dict[i]+1
    return dict


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
    new_string=""
    for i in string:
        if i.isalnum() or i==' ':
            new_string=new_string+i
    return new_string


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

    # Code Here
    n = len(input_tuple)
    list1=list(input_tuple)
    for i in range(0, n):
        for j in range(0, (n - i - 1)):
            if list1[j][1] > list1[j+1][1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    output_tuple=tuple(list1)
    return output_tuple


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

    # Code Here
    l = []
    t= string.split()
    for i in t:
        if any(ch.isalpha() for ch in i) and any(ch.isdigit() for ch in i):
            l.append(i)
    new_String=" ".join(l)
    return new_String


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

    # Code Here
    dict={'Characters': 0, 'Numbers': 0, 'Symbols': 0}
    for i in string:
        if i.isalpha():
            dict['Characters']+=1
        elif i.isdigit():
            dict['Numbers']+=1
        elif i!=' ':
            dict['Symbols']+=1
    return dict


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

    # Code Here
    new_str=""
    for i in string:
        if i.isalpha() or i.isdigit() or i==' ':
          new_str+=i
        else:
          new_str+="#"
    return new_str
