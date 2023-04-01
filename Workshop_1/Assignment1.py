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

    y=x**2
    return y


# def word_is_palindrome(string):
#     """
#     This function returns True if the given string is
#     a Palindrome
#     args:
#         string (str)
#     returns:
#         flag (bool)
#     ex:
#         string = 'abcba'
#         ## then
#         flag = True
#     """

#     x=len(string)
#     y=0
#     for i in range(x):
#         if string[i]==string[x-i-1]:
#            y+=1
#     if y==x:
#         flag=True
#     else:
#         flag=False
#     return flag


# def sqrt_of_numbers(num):
#     """
#     This function returns the magnitude of the square root of the number
#     args:
#         num (int) Need not be positive
#     returns:
#         sqroot (float) rounded off upto 2 decimal places.
#     ex:
#         num = 27
#         ## then
#         sqroot = 5.20
#     """
#     if num < 0:
#         raise ValueError('Number must be positive')

#     # Code Here
#     return None


# def Maximum(arr):
#     """
#     This function returns first maximum and the second maximum
#     number in the array
#     args:
#         arr (list)
#     returns:
#         Max1, Max2 (int, int)
#     ex:
#         arr = [1, 2, 3, 4, 5]
#         ## then
#         Max1, Max2 = 5, 4
#     """
#     x=len(arr)
#     a=arr[0]
#     b=arr[0]
#     for i in range(1,x):
#         if a<arr[i]:
#             b=a
#             a=arr[i]
#     return a,b



# def even_sort(arr):
#     """
#     This function sorts the array giving higher preference to even numbers
#     args:
#         arr (list)
#     returns:
#         sort_arr (list)
#     ex:
#         arr = [15, 2, 6, 88, 7]
#         ## then
#         sort_arr = [2, 6, 88 ,7 ,15]
#         ## This is any even number is smaller than any odd number
#     """

#     x=len(arr)
#     p=[]
#     q=[]
#     for i in range(x):
#         for j in range(0,x-i-1):
#             if arr[j]>arr[j+1] :
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

#     for i in range(x):
#         if arr[i]%2==0 :
#             p.append(arr[i])
#         else:
#             q.append(arr[i])
#     y=len(p)
#     z=len(q)
#     sort_arr=[]
#     for i in range(y):
#         sort_arr.append(p[i])
#     for i in range(z):
#         sort_arr.append(q[i])
#     return sort_arr


# def eqn_solver(A, B, C):
#     """
#     This function solves a two variable system
#     i.e.,
#         A = [ 1, 2 ]
#         B = [ 3, 4 ]
#         C = [ 5, 6 ]
#         then it means
#         1x + 3y = 5
#         2x + 4y = 6
#         Hence you are required to find x, y for such a linear system
#     args:
#         A, B, C (list, list, list) representing coefficients in the equation
#     returns:
#         x, y (float, float)
#     """

#     # Code Here
#     return None, None


# def swap_case(string):
#     """
#     This function swaps the case of the string.
#     args:
#         string (str)
#     returns:
#         string (str)
#     ex:
#         string = 'Hello World'
#         ## then
#         string = 'hELLO wORLD'
#     """

    
#     return string.swapcase()


# def is_prime(num):
#     """
#     This function returns True if the number is prime
#     args:
#         num (int)
#     returns:
#         flag (bool)
#     """

#     b=0
#     for i in range(1,num):
#         if num%i == 0:
#             b+=1
#     if(b==1):
#         c=True
#     else:
#         c=False
#     return c
   


# def is_leap_year(year):
#     """
#     This function returns True if the year is leap year
#     args:
#         year (int)
#     returns:
#         flag (bool)
#     """

#     if year%100==0 and year%400==0:
#         a=True
#     elif year%100!=0 and year%4==0:
#         a=True
#     else:
#         a=False
#     return a


# def is_perfect_square(num):
#     """
#     This function returns True if the number is perfect square i.e. it is a square of some integer.
#     args:
#         num (int)
#     returns:
#         flag (bool)
#     """
#     b=0
#     for i in range(1,num):
#         if num==i**2:
#             b+=1
#     if b==1:
#         a=True
#     else:
#         a=False
#     return a
    


# def is_perfect_number(num):
#     """
#     This function returns True if the number is perfect number.
#     A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
#     For example 6 is a perfect number because 1+2+3 = 6
#     args:
#         num (int)
#     returns:
#         flag (bool)
#     ex:
#         num = 6
#         ## then
#         flag = True

#         num = 7
#         ## then
#         flag = False
#     """

#     a=0
#     for i in range(1,num):
#         if num%i==0:
#             a+=i
#     if(a==num):
#         b=True
#     else:
#         b=False
#     return b


# def resize_array(a):
#     """
#     This function resizes a 1D array to 2D array of size 2x3
#     args:
#         a (np.array) of size 1x6
#     returns:
#         b (np.array) of size 2x3
#     ex:
#         a = np.array([1, 2, 3, 4, 5, 6])
#         ## then
#         b = np.array([[1, 2, 3], [4, 5, 6]])
#     """

#     p=[]
#     q=[]
#     for i in range(len(a)):
#         if i<3 :
#             p.append(a[i])
#         elif i>=3 :
#             q.append(a[i])
#     c=[p,q]
#     return c


# def reverse_step_array(a):
#     """
#     This function returns the reversed array with step size of 3.
#     args:
#         a (np.array)
#     returns:
#         b (np.array)
#     ex:
#         a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
#         ## then
#         b = np.array([9, 6, 3])
#     """

#     n=len(a)
#     p=[]
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if a[j]<a[j+1] :
#                 a[j],a[j+1]=a[j+1],a[j]
#     for i in range(0,n,3):
#         p.append(a[i])
#     return p


# def reverse_words(string):
#     """
#     This function reverses the words in the string.
#     args:
#         string (str)
#     returns:
#         string (str)
#     ex:
#         string = 'Hello Again World'
#         ## then
#         string = 'World Again Hello'
#     """

#     p=string.split()
#     n=len(p)
#     q=""
#     for i in range(n):
#         q+=p[n-i-1] + ' '
#     return q


# def count_characters(string):
#     """
#     This function counts the frequency of characters(ignore spaces as characters) in the input string.
#     args:
#         string (str)
#     returns:
#         dict (dict)
#     ex:
#         string = 'Hello World'
#         ## then
#         dict = {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1}
#     """

#     string.strip()
#     n=len(string)
#     dict={}
#     for i in range(n):
#         a=0
#         for j in range(n):
#             if string[i]==string[j] and string[i] !=' ':
#                 a+=1
#         if string[i] !=' ' :
#             dict[string[i]]=a
#     return dict
    


# def remove_special_characters(string):
#     """
#     This function removes the special characters from the input string. Special characters are those which are not letters or numbers.
#     args:
#         string (str)
#     returns:
#         string (str)
#     ex:
#         str = 'Hello, World! 123$ th15 1s 4 t35t str1ng'
#         ## then
#         str = 'Hello World 123 th15 1s 4 t35t str1ng'
#     """

#     a=list(string)
#     n=len(a)
#     b=''
#     for i in range(n):
#         if a[i].isalnum() or a[i].isspace():
#             b+=a[i]
#     return b


# def sort_tuple_of_tuples(input_tuple):
#     """
#     This function sorts the input tuple of tuples by the second item.
#     args:
#         input_tuple (tuple)
#     returns:
#         input_tuple (tuple)
#     ex:
#         input_tuple: (('a', 55), ('z', 1), ('f', 37), ('w', 19))
#         ## then
#         input_tuple: (('z', 1), ('w', 19), ('f', 37), ('a', 55))
#     """

#     # Code Here
#     return None


# def alpha_numeric_words(string):
#     """
#     This function finds words with both alphabets and numbers from an input string.
#     args:
#         string (str)
#     returns:
#         string (str)
#     ex:
#         string: "Hey there33 how11 are you1"
#         ## then
#         string: "there33 how11 you1"
#     """

#     a=string.split()
#     n=len(a)
#     b=''
#     for i in range(n):
#         if not a[i].isalpha():
#             if a[i].isalnum():
#                 b+=a[i] + ' '
#     return b
    


# def count_them_all(string):
#     """
#     This function counts all letters, digits, and special symbols from an input string.
#     args:
#         string (str)
#     returns:
#         dict (dict)
#     ex:
#         string: "IdDk3837#$fsd%%"
#         ## then
#         dict: {'Characters': 7, 'Numbers': 4, 'Symbols': 4}
#     """

#     l=list(string)
#     a=0
#     b=0
#     c=0
#     dict={}
#     for i in range(len(l)):
#         if l[i].isalpha() :
#             a+=1
#             continue
#         elif l[i].isdigit() :
#             b+=1
#             continue
#         else :
#             c+=1
        
       
#     dict['Characters']=a
#     dict['Numbers']=b
#     dict['Symbols']=c
#     return dict
    


# def hash_supremacy(string):
#     """
#     This function replaces each special symbol with '#' in the input string.
#     args:
#         string (str)
#     returns:
#         string (str)
#     ex:
#         string: "&He was a^%$ great @guy"
#         ## then
#         string: "#He was a### great #guy"
#     """

#     l=list(string)
#     a=''
#     for i in range(len(l)):
#         if not(l[i].isalpha()) and not (l[i].isdigit()) and not(l[i].isspace()):
#             l[i]='#'
#     for i in range(len(l)):
#         a+=l[i]
#     return a
