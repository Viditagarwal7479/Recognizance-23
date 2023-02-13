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

    # Code Here
    return x**2


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

    # Code Here
    for i in range(len(string)-1):
        if string[i] == string[-1-i]:
            flag = True
            continue
        else:
            flag = False
            break
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

    # Code Here
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

    # Code Here
    max1 = max(arr)
    arr.remove(max1)
    max2 = max(arr)
    return max1, max2


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

    # Code Here
    e=[]
    o=[]
    for i in arr:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    e.sort()
    o.sort()
    return e+o


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

    # Code Here
    return (C[1](B[0]/B[1]) - C[0])/(A[1](B[0]/B[1]) - A[0]), (C[1](A[0]/A[1]) - C[0])/(B[1](A[0]/A[1]) - B[0])


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

    # Code Here
    new = ''
    for i in string:
        if i.isupper():
            new+=i.lower()
        else:
            new+=i.upper()
    return new


def is_prime(num):
    """
    This function returns True if the number is prime
    args:
        num (int)
    returns:
        flag (bool)
    """

    # Code Here
    if num == 1:
        flag = False
    elif num==2:
        flag=True
    else:
        i=2
        while i<num:
            if num%i!=0:
                flag=True
                i+=1
                continue
            else:
                flag=False
                break
    return flag


def is_leap_year(year):
    """
    This function returns True if the year is leap year
    args:
        year (int)
    returns:
        flag (bool)
    """

    # Code Here
    if year%100==0:
        if year%4==0:
            flag = True
        else:
            flag = False
    elif year%4==0:
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

    # Code Here
    return int(num*0.5)*2 == num


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

    # Code Here
    i=1
    div = []
    while i<num:
        if num%i==0:
            div.append(i)
            i+=1
        else:
            i+=1
    return num == sum(div)


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

    # Code Here
    return a.reshape(2,3)


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

    # Code Here
    return a[-1::-3]


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
    new = ''
    for i in string.split():
        new = ' '+i+new
    return new


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
    d = {}
    for i in string:
        d[i] = string.count(i)
    d.pop(' ')
    return d


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

    # Code Here
    new = ''
    for i in string:
        if i.isalnum() or i==' ':
            new+=i
    return new


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
    return sorted(input_tuple,key=lambda n:n[1])


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
    new=''
    for i in string.split():
        if i.isalnum() and not (i.isalpha() or i.isnumeric()):
            new += i+' '
    return new


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
    d={}
    char=0
    num=0
    sym=0
    for i in string:
        if i.isaplha():
            char +=1
        elif i.isnumeric():
            num+=1
        else:
            sym+=1
    d['Characters']=char
    d['Numbers']=num
    d['Symbols']=sym
    return d


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
    new=''
    for i in string:
        if i.isalnum() or i==' ':
            new+=i
        else:
            new+='#'
    return new
