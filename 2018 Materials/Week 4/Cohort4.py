#HW1
# def compound_value_months(principle, interest, months):
#   amount = 0
#   m_rate = interest/12
#   for i in range(months):
#     amount+=principle
#     amount = amount*(1+m_rate)
#   return round(amount, 2)

# ans= compound_value_months (100 ,0.03 ,7)
# print ( ans)

#HW2
# def find_average(lists):
#     total = 0
#     item_count = 0
#     for l in lists:
#         item_count += len(l)
#         for item in l:
#             total+=item
#     total_ave = total/item_count

#     final_list = []
#     for l in lists:
#         if len(l) == 0:
#             final_list.append(0)
#         else:
#             final_list.append(sum(l)/len(l))
#     return final_list, total_ave

# ans= find_average ([[3 ,4] ,[5 ,6 ,7] ,[ -1 ,2 ,8]])
# print ( ans)

HW3
def transpose_matrix(m):    
    final = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return final


# a = [[1,2,3], [4,-5,6]]
# print (transpose_matrix(a))

# a = [[1,2], [10,5], [0,0]] 
# print (transpose_matrix(a))


#HW4
# phonebook =[{'name':'Andrew', 'mobile_phone':9477865 , 
# 'office_phone':6612345 , 'email':'andrew@sutd.edu.sg'},
# {'name':'Bobby','mobile_phone':8123498 , 'office_phone':6654321 , 'email': 'bobby@sutd .edu.sg'}]

# def get_details(name, key, lst):
#     for dic in lst:
#         if name != dic['name']:
#             pass
#         elif name == dic['name']:
#             return dic[key]
#         else:
#             return None

# print ( get_details ('Andrew', 'mobile_phone', phonebook ))
# print ( get_details ('Andrew ', 'email', phonebook ))


#HW5
# def get_base_counts(string):
#     dna = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
#     for char in string:
#         # if char != 'A' or 'C' or 'T' or 'G':
#         #     return 'The input DNA string is invalid'
#         # else:
#         if char == 'A':
#             print(dna)
#             dna['A']+=1
#         elif char == 'T':
#             dna['T']+=1
#         elif char == 'C':
#             dna['C']+=1
#         elif char == 'G':
#             dna['G']+=1
#         else:
#             return 'The input DNA string is invalid'
#     return dna

# print(get_base_counts("A"))



#HW1
# def f_to_c(f):
#     return round((f-32)*5/9, 1)

# def f_to_c_approx(f):
#     return round((f-30)/2, 1)

# F = [0,10,20,30,40,50,60,70,80,90,100]

# def get_conversion_table_a():
#     l2 = []
#     for i in F:
#         l2.append([i, f_to_c(i), f_to_c_approx(i)])
#     return l2
 
# def get_conversion_table_b():
#     l1 = []
#     l2 = []
#     l3 = []
#     for i in F:
#         l1.append(i)
#         l2.append(f_to_c(i))
#         l3.append(f_to_c_approx(i))
#     return [l1, l2, l3]


HW2
def max_list(inlist):
    l = []
    for i in inlist:
        l.append(max(i))
    return l

def max_list(inlist):
    return [max(i) for i in inlist]
    
#HW3
# def multiplication_table(n):
#     if n<=0:
#         return None
#     else:
#         l=[]
#         for j in range(n):
#             l.append([(j+1)*(i+1) for i in range(n)])
#         return l

# print(multiplication_table(4))

#HW4
# import sys

# def most_frequent(lst):
#     l1 = list(set(lst)) #removes repeat values
#     d1 = {el:0 for el in l1} #creates a blank dictionary using l1 as keys
#     for item in lst:
#         d1[item] +=1 #adds count to dictionary for item in input list
#     #print (d1)
#     max_value = max(d1.values()) #find the max value from dictionary
#     max_keys = [k for k, v in d1.items() if v == max_value] #adds keys to list if max value attained
#     return max_keys

# print(most_frequent([2,3,40,3,5,4,-3,3,3,2,0]))

#HW5
# def diff(p):
#     d1 = {(k-1):k*v for (k,v) in p.items() if k>0}
#     return d1

# p={0:-3, 3:2, 5:-1}
# print(diff(p))

