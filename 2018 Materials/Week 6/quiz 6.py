#from quizA_others import sum_of_odd_place, prefix_matched, get_prefix # <-- do not change this line

# TASK: implement the functions 'is_valid', 'sum_of_double_even_places',
#   'get_digit', and 'get_size'.

# HINT: the functions 'sum_of_odd_place' and 'prefix_matched' are
#   already implemented/imported and should be used in your solution.
#   Their behaviour is described in the Quiz A test paper.

def is_valid(number):
    sum1 = sum_of_double_even_place(number)
    sum2 = sum_of_odd_place(number)
    sum3 = sum1+sum2
    if sum3%10==0:
       return True
    else:
        return False

def sum_of_double_even_place(number):
    num = str(number)
    l1 = []
    l2 = []
    sum1 = 0
    for n in num[::2]: #skips numbers
       l1.append(2*int(n)) #doubles the number and appends to list 1
    for i in l1:
        l2.append(get_digit(i)) #calls the other function to return sum of 2 digit numbers
    print(l1)
    print(l2)
    for j in l2: #for loop to sum numbers in list
        sum1+=j
    return sum1

def get_digit(number): #function to return single numbers and sum double digit number
    if len(str(number))==1:
       return number
    else:
        string = str(number)
        return int(string[0]) + int(string[1])

def get_size(d): 
    return len(str(d)) #turns d to a string and gets the length

print(is_valid(371826291433349))
# print(get_digit(5))
# print(get_size(15))