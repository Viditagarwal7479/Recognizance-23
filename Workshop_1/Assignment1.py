def square(x):
    return x**2


def word_is_palindrome(string):
    str2=""
    for i in string:
     str2=i+str2
    return (str2==string)


def sqrt_of_numbers(num):
    if num < 0:
        raise ValueError('Number must be positive')
    return num**(1/2)


def Maximum(arr):
    max1=arr[0]
    max2=arr[0]
    for i in arr :
      if(max1<i):
        max1=i
    for i in arr:
      if(i==max1):
        continue
      if(max2<i):
        max2=i
    return max1, max2


def even_sort(arr):
    
    even=[]
    odd=[]
    for i in arr:
        if(i%2==0):
         even.append(i)
        else
         odd.append(i)
    l1=len(even)
    l2=len(odd)
    for i in range(0,l1-1):
      t=0
      for j in range(i+1,l1):
        if(even[i]>even[j]):
            t=even[i]
            even[i]=even[j]
            even[j]=t
     for i in range(0,l2-1):
      t=0
      for j in range(i+1,l2):
        if(odd[i]>odd[j]):
            t=odd[i]
            odd[i]=odd[j]
            odd[j]=t    
     return even+odd


def eqn_solver(A, B, C):
    x=(B[0]*C[1]-B[1]*C[0])/(-A[0]*B[1]+A[1]*B[0])
    y=(C[0]*A[1]-C[1]*A[0])/(-A[0]*B[1]+A[1]*B[0])
    return x,y


def swap_case(string):
    str2=""
    for i in string:
        if(i.isupper()):
         str2+=i.lower()
        else :
         str2+=i.upper()
    return str2


def is_prime(num):
    f=0;
    flag=False
    for i in range(1,num+1):
        if(num%i==0):
          f+=1
    flag=(f==2) 
    return flag



def is_leap_year(year):
    flag=False
    if(year%100==0 and year%400==0):
     flag=True
    elif(year%4==0 and year%100!=0):
     flag=True
    return flag



def is_perfect_square(num):
    return (num**(0.5)==int(num**(0.5)))


def is_perfect_number(num):
    sum=0;
    for i in range(1,num+1):
        if(num%i==0):
         sum+=i
    return (sum==num)


def resize_array(a):
    ar=[[],[]]
    t=0
    for i in range(2):
        for j in range(3):
            ar[i].append(a[t++])
    return ar


def reverse_step_array(a):
    b=a[::-1]
    c=[]
    for i in b:
       if(i%3==0):  
          c.append(i)
   
    return c


def reverse_words(string):
    wrd=""
    s=""
    str2=""
    for i in string:
        if(i!=' '):
           wrd+=i
        else :
           str2=""
           for i in wrd:
              str2=i+str2   
           s+=(" "+str2)
        
    return s


def count_characters(string):
    dict1={}
    s="abcdefghijklmnopqrstuvwxyz"
    s2=string.lower()
    for i in s:
        f=0
        for j in s2:
            if(j==i):
              f+=1
        if(f!=0) :     
            dict1[i]=f
    return dict1


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
    return None


def sort_tuple_of_tuples(input_tuple):
    lst=list(input_tuple)
    l=len(lst)
    for i in range(0,l-1):
      t=0
      for j in range(i+1,l):
        if(lst[i][1]>lst[j][1]):
            t=lst[i][1]
            lst[i][1]=lst[j][1]
            lst[j][1]=t
    tup=tuple(lst)
    return tup


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
    return None


def count_them_all(string):
   dict1 ={'Characters':0,'Numbers':0,'Symbols':0}
   for i in string:
        if((i>='a' and i<='z')||(i>='A' and i<='Z')):
          dict1['Character']+=1
        elif(i>='0' and i<='9'):
          dict1['Number']+=1
        else :
          dict1['Symbol']+=1
   return dict1


def hash_supremacy(string):
   str2=""
   for i in string:
        if((i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9') or (i==' ')):
         str2+=i
        else:
         str2+="#"
    
   return str2
