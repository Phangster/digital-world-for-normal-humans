#C1
print("C2-----------------------------------------------")
def is_larger(x,y):
    if x>y:
        return True
    elif y>=x:
        return False
    else:
        pass

print ( is_larger (2 , -1))

#C2
print("C3-----------------------------------------------")
def letter_grade (n):
    if n>100 or n<0:
        return None
    elif n >=90:
        return "A"
    elif n >=80:
        return "B"
    elif n >=70:
        return "C"
    elif n >=60:
        return "D"
    else:
        return "E"

print ( letter_grade (80) )

#C3
print("C4-----------------------------------------------")
def list_sum(list):
    sum = 0.0
    for num in list:
        sum += num
    return sum

print(list_sum ([]))

print("C5-----------------------------------------------")
def minmax_in_list(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    if len(alist)>0:
        small = alist[0]
        big = alist[-1]
        return small, big
    else:
        return None, None

print(minmax_in_list ([1 ,2 ,3 ,4 ,5]))

print("C6-----------------------------------------------")
def is_palindrome(num):
    num = str(num)
    if num == str(num)[::-1]:
        return True
    else:
        return False

print(is_palindrome (1))

print("PS1-----------------------------------------------")
def check_value(n1, n2, n3, x):
    if x > n1 and x>n2 and x<n3:
        return True
    else: 
        return False

print(check_value (1 ,4 ,8 ,7))
print(check_value (1 ,4 ,5 ,7))

print("PS2-----------------------------------------------")
def temp_convert (unit, num):
    if unit == "F":
        f = num*float(9)/5 + 32
        return f
    elif unit == "C":
        c = (num-32)*float(5)/9
        return c
    else:
        return None


print("PS3-----------------------------------------------")
def get_even_list(list):
    new_list = []
    for item in list:
        if item % 2 ==0:
            new_list.append(item)
    return new_list

print(get_even_list ([11 ,22 ,31 ,41 ,52]))

print("PS4-----------------------------------------------")
def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

print(is_prime (13))

print("PS5-----------------------------------------------")

import math
def approx_ode(h,t0,y0,tn):
    if tn < h/2:
        return y0
    else:
        cal = approx_ode(h, t0, y0, tn-h)
        res = cal + h*f(tn-h, cal)
        return res

######### Ignore code below this line ######################################
def f(t, y):
    return 3.0+math.exp(-t)-0.5*y

print(approx_ode(0.1, 0, 1, 3))
print(approx_ode(0.1, 0, 1, 4))
print(approx_ode(0.1, 0, 1, 5))
