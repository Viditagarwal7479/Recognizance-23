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
    n=len(string)
    t= True
    for i in range(int(n/2)):
        if str[i]!=str[n-1-i] :
            t=False
    return t
    


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
    else :
        return (num**0.5)

    
    


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
    arr.sort(reverse=True)
    ar1=[]
    for i in arr:
        if i not in ar1:
            ar1.append(i)
   
    
    return ar1[0],ar1[1]

print(Maximum([1,2,3,4,4]))



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
    ar1=[]
    for i in arr:
        if i%2==0:
            ar1.append(i)
    for i in arr:
        if i%2==1:
            ar1.append(i)
    return ar1
        
    
    
    
    
    
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

    import numpy as np
    A,B,C=np.array(A),np.array(B),np.array(C)
    D=np.array([A,B])
    D_x=np.array([C,B])
    D_y=np.array([A,C])
    D=D.transpose()
    D_x=D_x.transpose()
    D_y=D_y.transpose()
    x=np.linalg.det(D_x)/np.linalg.det(D)
    y=np.linalg.det(D_y)/np.linalg.det(D)
    
    return x, y


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

   
    return string.swapcase()


def is_prime(num):
    """
    This function returns True if the number is prime
    args:
        num (int)
    returns:
        flag (bool)
    """
    flag=True
    for i in range(2,int(num/2)):
        if num%i==0:
            flag=False
            break

    
    return flag
print(is_prime(43))


def is_leap_year(year):
    """
    This function returns True if the year is leap year
    args:
        year (int)
    returns:
        flag (bool)
    """
    if year%4==0:
        return True
    else:
         return None

    
   


def is_perfect_square(num):
    """
    This function returns True if the number is perfect square i.e. it is a square of some integer.
    args:
        num (int)
    returns:
        flag (bool)
    """

    flag=False
    t=num**0.5
    p=int(t)
    q=t-p
    if q==0:
        flag=True
    return flag



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

    div=[]
    for i in range(1,num):
        if num%i==0:
            div.append(i)
     sum=0
    for i in range(len(div)):
        sum+=div[i]
    if sum!=num:
        return False
    else :
        return True
   


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
    x=a[:3]
    y=a[3:]
    z=np.array([x,y])
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

    # Code Here
    return a[::-3]


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

    temp=(string.split())
    reverse=""
    for i in temp[::-1]:
        reverse+=i+' '
    
    return reverse



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
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
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

    
    str=''
    for i in string:
        if (i.isalpha() or i.isdigit()):
            str+=i
    return str

def sort_tuple_of_tuples(input_tuple):
    """
    This function sorts the input tuple of tuples by the second item.
    args:
        input_tuple (tuple)
    returns:
        input_tuple (tuple)
    ex: (('a', 55), ('z', 1), ('f', 37), ('w', 19))
        input_tuple:
        ## then
        input_tuple: (('z', 1), ('w', 19), ('f', 37), ('a', 55))
    """
    t=[*input_tuple]
   
    for i in range(len(t)):
        for j in range(i-1):
            if t[j][1]>t[j+1][1]:
                t[j],t[j+1]=t[j+1],t[j]
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

    ls=string.split()
    str=''
    num='0123456789'
    print(ls)
    for i in ls:
        for j in i:
            if j in num:
                str+=i+' '
                break
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
    ch=0;num=0;sym=0
    for i in string:
        if i.isalpha():
            ch+=1
        elif i.isdigit():
            num+=1
        elif i==' ':
            continue
        else:
            sym+=1
            
    dict={'Chracters':ch,'Numbers':num,'Symbols':sym}       
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

    
    str=''
    
    for i in range(len(string)):
        if ( string[i].isalpha()or string[i].isdigit()):
            str+=string[i]
        else:
            str+='#'
    return str

