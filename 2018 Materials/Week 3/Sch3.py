import numpy as np
from scipy.special import lpmv
# from scipy.special import binom
# import scipy.constants as c
# import math
# from scipy.special import assoc_laguerre as al

def angular_wave_func(m,l,theta,phi):
    p1 = (2*l+1)/(4*c.pi)
    p2 = np.math.factorial(l - abs(m))/np.math.factorial(l+abs(m))
    p3 = (math.e)**(((-1)**0.5)*m*phi)
    alf = lpmv(m, l, np.cos(theta))
    print (alf)
    cal = alf*(((p1*p2)**0.5)*p3)
    if m >0:
        return round(cal, 5)
    elif m <=0:
        return round(cal, 5)
    else:
        pass

import math
import cmath
import numpy as np

def angular_wave_func(m,l,theta,phi):
    if l==0:
        output=(1/(4*math.pi))**0.5
    elif l==1:
        if m==1:
            output=np.sqrt(3/(8*math.pi))*np.sin(theta)*np.exp(-1j*(phi))
        elif m==0:
            output=output=(3/(4*math.pi))**0.5*math.cos(theta)
        elif m==-1:
            output=math.sqrt(3/(8*math.pi))*math.sin(theta)*cmath.exp(-phi*1j)
    elif l==2:
        if m==2:
            output=math.sqrt(15/(32*math.pi))*(math.sin(theta))**2*(cmath.exp(2j*phi))
        elif m==1:
            output=-(math.sqrt(15/(8*math.pi))*math.sin(theta)*math.cos(theta)*cmath.exp(phi*1j))
        elif m==0:
            output=output=(5/(16*math.pi))**0.5*(3*(math.cos(theta))**2-1)
        elif m==-2:
            output=math.sqrt(15/(32*math.pi))*(math.sin(theta))**2*(cmath.exp(-2j*phi))
        elif m==-1:
            output=math.sqrt(15/(8*math.pi))*math.sin(theta)*math.cos(theta)*cmath.exp(phi*-1j) 
    elif l==3:
        if m==3:
            output=-(math.sqrt(35/(64*math.pi))*(math.sin(theta))**3*cmath.exp(3j*phi))
        elif m==2:
            output=math.sqrt(105/(32*math.pi))*math.cos(theta)*(math.sin(theta))**2*cmath.exp(2j*phi)
        elif m==1:
            output=-(math.sqrt(21/(64*math.pi))*math.sin(theta)*(5*(math.cos(theta))**2-1)*cmath.exp(1j*phi))
        elif m==0:
            output=math.sqrt(7/(16*math.pi))*(5*(math.cos(theta))**3-3*math.cos(theta))
        elif m==-1:
            output=(math.sqrt(21/(64*math.pi))*math.sin(theta)*(5*(math.cos(theta))**2-1)*cmath.exp(-1j*phi))
        elif m==-2:
            output=math.sqrt(105/(32*math.pi))*math.cos(theta)*(math.sin(theta))**2*cmath.exp(-2j*phi)
        elif m==-3:
            output=output=(math.sqrt(35/(64*math.pi))*(math.sin(theta))**3*cmath.exp(-3j*phi))
    return np.round(output,5)



# print('angular_wave_func (0,0,0,0)')
# ans= angular_wave_func (0,0,0,0)
# print(ans)
# print('angular_wave_func (0,1,c.pi ,0)')
# ans= angular_wave_func (0,1,c.pi ,0)
# print(ans)
# print('angular_wave_func (1,1,c.pi/2,c.pi)')
# ans= angular_wave_func (1,1,c.pi/2,c.pi)
# print(ans)
# print('angular_wave_func (0,2,c.pi ,0)')
# ans= angular_wave_func (0,2,c.pi,0)
# print(ans)

# def radial_wave_func(n,l,r):
#     a=c.physical_constants['Bohr radius'][0]
#     coef = 2/(n*a)
#     rcoef = (2*r)/(n*a)

#     p = 2*l+1
#     q=n+l
#     q_p = n-l-1

#     p1 = coef**3
#     p2 =  np.math.factorial(q_p)/(2*n*(np.math.factorial(n+l)))
#     p3 = (math.e**(-rcoef/2))*((rcoef)**l)
#     cal = ((p1*p2)**0.5)*p3*al(rcoef, q_p, p)
#     normal_cal = cal/(a**-1.5)
#     return round(normal_cal, 5)

# def calf(p, q_p, x):
#     if p == 0:
#         return 1
#     elif p == 3 and q_p == 0:
#         return 6
#     else:
#         return 64

# def calf(n, k, x):
#     sum = 0
#     for m in range(0,n+1):
#         sum+= (-1)**m * np.math.factorial(n+k) / np.math.factorial(n-m) / np.math.factorial(k+m) / np.math.factorial(m) * x**m
#     final = sum
#     return final

import scipy.constants as c
import numpy as np 

def radial_wave_func(n,l,r):
    a=c.physical_constants['Bohr radius'][0]
    if n==1:
        output=(2/(a**3)**0.5)*np.exp(-r/a)
    elif n==2:
        if l==1:
            output=(1/(24**0.5))*(a**(-3/2))*(r/a)*np.exp(-r/(2*a))
        elif l==0:
            output=(1/(2**0.5))*(a**(-3/2))*(1-(r/(2*a)))*np.exp(-r/(2*a))
    elif n==3:
        if l==0:
            output=(2/(81*(3)**0.5))*(a**(-3/2))*(27-18*(r/a)+2*(r/a)**2)*np.exp(-r/(3*a))
        elif l==1:
            output=(8/(27*(6**0.5)))*(a**(-3/2))*(1-r/(6*a))*(r/a)*np.exp(-r/(3*a))
        elif l==2:
            output=(4/(81*(30)**0.5))*(a**(-3/2))*(r/a)**2*np.exp(-r/(3*a))
    elif n==4:
        if l==0:
            output=0.25*(a**(-3/2))*(1-(3/4)*(r/a)+(1/8)*(r/a)**2-(1/192)*(r/a)**3)*np.exp(-r/(4*a))
        elif l==1:
            output=((5)**0.5/(16*(3**0.5)))*(a**(-3/2))*(r/a)*(1-0.25*(r/a)+(1/80)*(r/a)**2)*np.exp(-r/(4*a))
        elif l==2:
            output=(1/(64*(5**0.5)))*(a**(-3/2))*(r/a)**2*(1-(1/12)*(r/a))*np.exp(-r/(4*a))
        elif l==3:
            output=(1/(768*(35**0.5)))*(a**(-3/2))*(r/a)**3*np.exp(-r/(4*a))
    output1=(output)/(a**(-1.5))
    return round(output1,5)

b = c.physical_constants['Bohr radius'][0]
print('radial_wave_func (1,0,a)')
ans= radial_wave_func (1,0,b)
print(ans)
print('radial_wave_func (2,1,a)')
ans= radial_wave_func (2,1,b)
print(ans)
print('radial_wave_func (2,1,2*a)')
ans= radial_wave_func (2,1,2*b)
print(ans)
print('radial_wave_func (3,1,2*a)')
ans= radial_wave_func (3,1,2*b)
print(ans)

# radial_wave_func (1,0,a) #p=1, q-p= 0
# 0.73576
# radial_wave_func (2,1,a) #p=3, q-p = 0
# 0.12381
# radial_wave_func (2,1,2*a) #p=3, q-p = 0
# 0.15019
# radial_wave_func (3,1,2*a) #p=3, q-p = 1
# 0.08281