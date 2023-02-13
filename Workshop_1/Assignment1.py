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

    y = x**2
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
    if(string == string[::-1]):
        return True
    else:
        return False

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
    if num<0:
        raise ValueError("Number must be positive")
    x = round(num**(0.5),2)
    return x


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

    max1= 0
    max2 = 0
    for i in arr:
        if (i>max):
            max1 = i
    l = []
    for i in arr:
        if(i == max1):
            continue
        else:
            l.append(i)
    for i in l:
        if(i>max2):
            max2 = i
    
        
    return max1,max2


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
    arr.sort()
    l = []
    for i in arr:
        if (i%2 == 0):
            l.append(i)
    for i in arr:
        if(i in l):
            continue
        else:
            l.append(i)
    return l


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

    for i in range(0,2):
        A[i] = A[i]*B[0]
    C[0] = C[0]*B[0]
    for i in range(0,2):
        B[i] = B[i]*A[0]
    C[1] = C[1]*A[0]
    
    y = (C[0] - C[1])/(A[1] - B[1])
    x = (C[0] - A[1])/A[0]
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

    toggle_str = ''
    for i in range(len(string)):
        if(string[i] >= 'a' and string[i] <= 'z'): 
            toggle_str = toggle_str + chr(ord(string[i]) - 32)
        elif(string[i] >= 'A' and string[i] <= 'Z'):
            toggle_str = toggle_str + chr(ord(string[i]) + 32)
        else:
            toggle_str = toggle_str + string[i]
        return toggle_str


def is_prime(num):
    """
    This function returns True if the number is prime
    args:
        num (int)
    returns:
        flag (bool)
    """
    flag = 0
    x= int(num**(0.5))
    for i in range(2,x+1):
                   if(num%i == 0):
                        flag = 1
                        break
                   
    if flag == 0 :
                   return True
    else:
                   return False

def is_leap_year(year):
    """
    This function returns True if the year is leap year
    args:
        year (int)
    returns:
        flag (bool)
    """

    if(year%4 == 0):
        return True
    return False


def is_perfect_square(num):
    """
    This function returns True if the number is perfect square i.e. it is a square of some integer.
    args:
        num (int)
    returns:
        flag (bool)
    """
    y = num**(0.5)
    
    if(y%1 == 0):
        return True
    else:
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
    sum = 0
    x = int(num/2)
    for i in range(1,x+1):
        if(num%i == 0):
            sum = sum+i
    if(sum == num):
        return True
    else:
        return False


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
    l1 = []
    l2 = []
    for i in range(0,3):
        l1.append(a[i])
    for i in range(3,6):
        l2.append(a[i])
    l = [l1,l2]
    z = np.array(l)
    return z


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
    b = np.array(l[::-3])
    
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
    l = string.split(" ")
    l.reverse()
    str = ''
    for i in l:
        str = str + i
        str = str + " "
    
    return str    


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

    dict = {}
    for i in string:
        if i in dict.keys():
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
        
    return dict


def remove_special_characters(string):
    """
    This function removes the special characters from the input string. Special characters are those which are not letters or numbers.
    args:
        sstring (str)
    returns:
        string (str)
    ex:
        str = 'Hello, World! 123$ th15 1s 4 t35t str1ng'
        ## then
        str = 'Hello World 123 th15 1s 4 t35t str1ng'
    """
    str = ''
    for i in string:
        if(64<ord(i)<91 or 96<ord(i)<123 or 47<ord(i)<58 or i ==' '):
            str = str + i
         
    
    return str


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
    l = []
    t = ()
    for i in input_tuple:
        l.append(i)
    for i in range(0,len(l)-1):
        if(l[i][1] > l[i+1][1]):
            l[i],l[i+1] = l[i+1],l[i]
    print(l)   
    for i in l:
        t =  t + (i,)     
    return t


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

    str = ''
    l = string.split(" ")
    for i in l:
        if(i.isalnum()):
            str = str+i
        else:
            continue
      
    return str


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
    char = 0
    nukber =0
    special = 0
    for i in string:
        if(64<ord(i)<91 or 96<ord(i)<123):
            char = char+1
        elif(47<ord(i)<59):
            number = number+1
        else:
            special = special +1
    dict = {'Charchters':char,'Numbers':number,'Symbols':special}
    
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

    str = ''
    for i in string():
        if(64<ord(i)<91 or 96<ord(i)<123 or 47<ord(i)<58 or i ==' '):
            str = str + string[i]
            
        else:
            str = str + '#'
            
    return str
