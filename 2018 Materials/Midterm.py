# f = [1,2,3]
# g= f[:]
# g[0]=4
# print(g,f)

# import1 = int(input("Enter a number:"))  
# if import1==2:      
#     print("Yes")  
# else:
#     print("No")

# my_string = "Computing"  
# for character in my_string:
#     print(character)
#     if character == "u":
#         print("Found 'u' :)")   
#         #break  

# def my_function(n): 
#     return_value = None 
#     if n == 0 or n == 1: 
#         return_value = False 
#     i=2 
#     while i < n**0.5: 
#         if n%i==0: 
#             return_value = False 
#             break 
#         i+=1 
#         return_value = True 
#     return return_value

# print(my_function(37))


#Q3
# import math
# def area_square(s):
#     return float(s**2)

# def vol_frustum(top_area, bottom_area, height):
#     return float(height/3*(top_area+bottom_area+math.sqrt(top_area*bottom_area)))

# def get_volume(s1, s2, height):
#     top_area = area_square(s1)
#     bottom_area = area_square(s2)
#     final = float(height/3*(top_area+bottom_area+math.sqrt(top_area*bottom_area)))
#     return round(final,3)

# print(area_square(2))
# print(area_square(3))
# print(vol_frustum(1,4,2))
# print(vol_frustum(2,2,2))
# print(get_volume(1,2,2))
# print(get_volume(1.5,3.3,5.0))
# print(get_volume(3.6,6.4,4.0))

#Q4
def determinant(M):
    for sublist in M:
        if len(sublist) != len(M):
            return None
    if len(M) == 1:
        return M[0][0]
    elif len(M) ==2:
        det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
        return det
    elif len(M) == 3:
        det1 = M[0][0]* (M[1][1]*M[2][2] - M[1][2]*M[2][1])
        det2 = M[0][1]* (M[1][2]*M[2][0] - M[1][0]*M[2][2])
        det3 = M[0][2]* (M[1][0]*M[2][1] - M[1][1]*M[2][0])
        return det1+det2+det3

# print(determinant([[100]]))
# print(determinant([[-5,-4],[-2,-3]]))
# print(determinant([[2,-3,1],[2,0, -1], [1,4,5]]))
# print(determinant([[0,3,5],[5,5,2], [3,4,3]]))
# print(determinant([[23], [-4,4]]))

#Q5
def nroot(n,t,num):
    return round(num**(1/n), 3)


def nroot_complex(n,t,num):
    cal = nroot(n, t, abs(num))
    if n % 4==0:
        return cal*-1
    elif n%2 == 0:
        return cal*1j
    else:
        return cal    

# print(nroot(2,5,-4))




#Q6
def read_stations(f):
    d = {}
    # for num, line in enumerate(f):
    #     if line[0] == '=':
    #         key = line[1:-2]
    #         d[key] = None
    for line in f:
        print(line)
    return d

import pickle

def get_stationline(mrt):
    d = {}
    for k, v in mrt.items():
        l=[]
        l.append()
        d[v] = k
    return d

def get_interchange(stationline):
    d= stationline
    for k,v in d.items():
        if len(v) <2:
            del d[k]
    return d


f = open('file.txt', 'r')
print(read_stations(f))


#Q7
def decompose(n):
    coins = [1,2,5,10,20,100,200]

#1,2,5,10,20,100,200    