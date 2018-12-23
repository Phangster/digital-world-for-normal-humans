# # # # Question 1
# # # import random

# # # craps=set([2,3,12])
# # # naturals=set([7,11])

# # # def roll_two_dices():
# # #     return (random.randint(1,6),random.randint(1,6))

# # # def print_lose():
# # #     print('You lose') 

# # # def print_win():
# # #     print('You win') 

# # # def print_point(p):
# # #     print('Your points are '+ str(p)) 

# # # def is_craps(n):
# # #     if n in craps:
# # #         return True
# # #     else:
# # #         return False

# # # def is_naturals(n):
# # #     if n in naturals:
# # #         return True
# # #     else:
# # #         return False

# # # def play_craps():
# # #     point=-1
# # #     while True:
# # #         n1,n2=roll_two_dices()
# # #         sumn=n1+n2
# # #         print ('You rolled %d + %d = %d'%(n1,n2,sumn))   
# # #         if point==-1:              
# # #             if is_craps(sumn):  
# # #                 print_lose()     
# # #                 return 0
# # #             elif is_naturals(sumn):   
# # #                 print_win()     
# # #                 return 1
# # #             point=sumn
# # #             print_point(point)
# # #         else:
# # #             if sumn==7:
# # #                 print_lose()
# # #                 return 0
# # #             elif sumn==point:
# # #                 print_win()
# # #                 return 1   



# # #Question 2

def leap_year(year):
    if year%4 != 0:
        return False
    elif year%100 !=0:
        return True
    elif year%400 !=0:
        return False
    else:
        return True
 
def day_of_week_jan1(year):
    A = year
    return R(1+5*R(A-1, 4)+4*R(A-1, 100) + 6*R(A-1, 400), 7) 
def R(y, x):
    return y%x


def num_days_in_month(month_num, leap_year):
    if month_num in [1,3,5,7,8,10,12]:
        return 31
    elif month_num in [4,6,9,11]:
        return 30
    elif month_num in [2]:
        if leap_year ==True:
            return 29
        else: 
            return 28

# print(num_days_in_month(1,False))
# print(num_days_in_month(2, False))
# print(num_days_in_month(2, True))
# print(num_days_in_month(3, False))
# print(num_days_in_month(4, False))

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    final = [months[month_num-1]]
    days_string = ''
    for i in range(first_day_of_month):
        days_string += '   '
    for  i in range(1, num_days_in_month+1):
        if i < 10:
            days_string += '  '
            days_string += str(i)
        else:
            days_string += ' '
            days_string += str(i)

    final.append(days_string[0:21])
    final.append(days_string[21:42])
    final.append(days_string[42:63])
    final.append(days_string[63:84])
    if len(days_string) > 84:
        final.append(days_string[84:105])
    if len(days_string) > 105:
        final.append(days_string[105:])
    return final


def  print_cal_month(list_of_str):
    ret_val=''
    for l in  list_of_str:
        ret_val += l.replace(' ','*')
        ret_val +='\n'
    return  ret_val

# ans = construct_cal_month (1,2,31)
# print(print_cal_month(ans))
 
def len_last_week_cal(list):
    length = len(list[-1][-1]) //3
    if length <7:
        return length
    elif length == 7:
        return 0

def construct_cal_year(year):
    final = [year]
    final.append(construct_cal_month(1, day_of_week_jan1(year), num_days_in_month(1, leap_year(year))))
    for i in range (2,13):
        len_last_week = len_last_week_cal(final)
        final.append(construct_cal_month(i, len_last_week, num_days_in_month(i, leap_year(year))))
    #print (final)
    return final

print(construct_cal_year(2017))

def display_calendar(year):
    final = ''
    for item in construct_cal_year(year)[1:]:
        final += item[0]
        final += '\n'
        final += '  S  M  T  W  T  F  S'
        final += '\n'
        for thing in item[1:]:
            final += str(thing)
            final +='\n'
        final +='\n'
    return final[:-2]

# # def  print_space_display_calendar(calendar):
# #     temp=calendar.replace(' ', '*')
# #     return  temp.replace('\n','+\n')

# # ans=display_calendar (2015)
# # print('START')
# # print(print_space_display_calendar(ans))
# # print('END')

# #Question 3
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

#HW1
def extract_values(values):
    numbers = values.split()
    return int(numbers[0]), int(numbers[-1])


def calc_ratios(values):
    if values[-1] == 0:
        return None
    else:
        return values[0]/values[-1]

def get_integer_ratio():
    data=input('Enter integer pair (hit Enter to quit)')  
    while data !='':
        values=extract_values(data)
        ratio=calc_ratios(values)
        print('The ratio of the two integers are: {:.2f}'.format(ratio))
        data=input('Enter integer pair (hit Enter to quit)')



