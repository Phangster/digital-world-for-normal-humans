import numpy as np
import scipy.constants as c
import math
import cmath
#np.set_printoptions(suppress=False,formatter={'float_kind':'{:f}'.format})

#Week 2 ============================================
def spherical_to_cartesian(r, theta, phi):
    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)
    # x = round(x, 5)
    # y = round(y, 5)
    # z = round(z, 5)
    return x,y,z

def cartesian_to_spherical(x, y, z):
    r = (x**2+y**2+z**2)**0.5
    theta = np.arccos(z/r)
    phi = np.arccos(x/(x**2+y**2)**0.5)
    # r = round(r, 5)
    # theta = round(theta, 5)
    # phi = round(phi, 5)
    return r, theta, phi

def absolute (complex):
    real = complex.real
    imaginary = complex.imag
    absolute = (real**2+imaginary**2)**0.5
    return absolute

#Week 3 ============================================
def angular_wave_func(m,l,theta,phi):
    if l==0:
        output=(1/(4*math.pi))**0.5
    elif l==1:
        if m==1:
            output=-np.sqrt(3/(8*math.pi))*np.sin(theta)*np.exp(1j*(phi))
        elif m==0:
            output=(3/(4*math.pi))**0.5*np.cos(theta)
        elif m==-1:
            output=np.sqrt(3/(8*math.pi))*np.sin(theta)*np.exp(-phi*1j)
    elif l==2:
        if m==2:
            output=np.sqrt(15/(32*math.pi))*(np.sin(theta))**2*(np.exp(2j*phi))
        elif m==1:
            output=-(np.sqrt(15/(8*math.pi))*np.sin(theta)*np.cos(theta)*np.exp(phi*1j))
        elif m==0:
            output=(5/(16*math.pi))**0.5*(3*(np.cos(theta))**2-1)
        elif m==-2:
            output=np.sqrt(15/(32*math.pi))*(np.sin(theta))**2*(np.exp(-2j*phi))
        elif m==-1:
            output=np.sqrt(15/(8*math.pi))*np.sin(theta)*np.cos(theta)*np.exp(phi*-1j) 
    elif l==3:
        if m==3:
            output=-(np.sqrt(35/(64*math.pi))*(np.sin(theta))**3*np.exp(3j*phi))
        elif m==2:
            output=np.sqrt(105/(32*math.pi))*np.cos(theta)*(np.sin(theta))**2*np.exp(2j*phi)
        elif m==1:
            output=-(np.sqrt(21/(64*math.pi))*np.sin(theta)*(5*(np.cos(theta))**2-1)*np.exp(1j*phi))
        elif m==0:
            output=np.sqrt(7/(16*math.pi))*(5*(np.cos(theta))**3-3*np.cos(theta))
        elif m==-1:
            output=(np.sqrt(21/(64*math.pi))*np.sin(theta)*(5*(np.cos(theta))**2-1)*np.exp(-1j*phi))
        elif m==-2:
            output=np.sqrt(105/(32*math.pi))*np.cos(theta)*(np.sin(theta))**2*np.exp(-2j*phi)
        elif m==-3:
            output=(np.sqrt(35/(64*math.pi))*(np.sin(theta))**3*np.exp(-3j*phi))
    return output


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
    return output1


#Week 4==================================================================
def linspace(start, stop, *args, **kwargs):
    incriment = (stop - start)
    if 'num' in kwargs:
        incriment /= kwargs['num']-1
    elif args == ():
        incriment/=49
    elif type(args[0]) == int:
        incriment/= args[0]-1
    else:
        incriment/=49

    l = []
    start = start
    while start<stop:
        l.append(round(start, 5))
        start +=incriment
    if l[-1] != stop:
        l.append(stop)
    return l

def meshgrid(x, y, z):
    xlen = len(x)
    ylen = len(y)
    zlen = len(z)
    xlist = [[[x[j] for i in range(zlen)] for j in range(xlen)] for k in range(ylen)]
    ylist = [[[y[k] for i in range(zlen)] for j in range(xlen)] for k in range(ylen)]
    zlist = [[[z[i] for i in range(zlen)] for j in range(xlen)] for k in range(ylen)]
    return xlist, ylist, zlist

#Week 5 ============================================
def real_angular_wf(m, l, theta, phi):
    #print('input variables are:', m, l)
    if m < 0:
        final = 1j/(2**0.5)*(angular_wave_func(m,l,theta,phi) - (-1)**m * angular_wave_func(-m,l,theta,phi))
        #final = (2**0.5)*((-1)**m)*(angular_wave_func(m,l,theta,phi).real)
        return final
    elif m == 0:
        final = angular_wave_func(0, l, theta, phi)
        return final
    elif m > 0:
        final = 1/(2**0.5)*(angular_wave_func(-m,l,theta,phi) + (-1)**m * angular_wave_func(m,l,theta,phi))
        #final = (2**0.5)*((-1)**m)*(angular_wave_func(m,l,theta,phi).imag)
        return final

def hydrogen_wave_func(n,l, m, roa, Nx, Ny, Nz):
    xx,yy,zz=np.mgrid[-1*roa:roa:(Nx*1j),-1*roa:roa:(Ny*1j),-1*roa:roa:(Nz*1j)] #get the mgrid of Nx, Ny, Nz
    spherical_coordinates = cartesian_to_spherical(xx,yy,zz) #get spherical coordinates
    clean_spherical_coordinates = np.nan_to_num(spherical_coordinates) #removes Nan values
    r = clean_spherical_coordinates[0] 
    theta = clean_spherical_coordinates[1]
    phi = clean_spherical_coordinates[2]
    #print(clean_spherical_coordinates)
    rawf = np.absolute(real_angular_wf(m, l, theta, phi))
    a=c.physical_constants['Bohr radius'][0]
    rwf = np.absolute(radial_wave_func(n,l,r*a))
    mag = (rawf*rwf)**2 #gets the final density function
    return xx, yy, zz, np.round(mag,5)


print('Test 1===========================================================')
x,y,z,mag=hydrogen_wave_func(2,1,1,8,3,3,3)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)

print('Test 2===========================================================')
x,y,z,mag=hydrogen_wave_func(2,1,1,5,3,4,2)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)

print('Test 3===========================================================')
x,y,z,mag=hydrogen_wave_func(2,0,0,3,5,4,3)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)

print('Submission 1===========================================================')
x,y,z,mag=hydrogen_wave_func(2,1,1,8,4, 4, 4)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)

print('Submission 2===========================================================')
x,y,z,mag=hydrogen_wave_func(2,1,1,8,4, 4, 4)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)

print('Submission 3===========================================================')
x,y,z,mag=hydrogen_wave_func(2,1,1,8,4, 4, 4)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)

print('Submission 4===========================================================')
x,y,z,mag=hydrogen_wave_func(2,1,1,8,4, 4, 4)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)

'''
Test case 1: hydrogen_wave_func(2,1,1,8,4, 4, 4)                                                                                                                               
Test case 1: hydrogen_wave_func(2,1,1,8,4, 4, 4)                                                                                                                               
False                                                                                                                                                                          
Test case 2: hydrogen_wave_func(2,1,1,5,3,4,2)                                                                                                                                 
Test case 2: hydrogen_wave_func(2,1,1,5,3,4,2)                                                                                                                                 
False                                                                                                                                                                          
Test case 3: hydrogen_wave_func(2,0,0,3,5,4,3)                                                                                                                                 
Test case 3: hydrogen_wave_func(2,0,0,3,5,4,3)                                                                                                                                 
True                                                                                                                                                                           
Pass:  True                                                                                                                                                                    
Test case 3: hydrogen_wave_func(3,1,0,10,6,6,6)                                                                                                                                
Test case 3: hydrogen_wave_func(3,1,0,10,6,6,6)                                                                                                                                
True                                                                                                                                                                           
Pass:  True                                                                                                                                                                    
Score: [2/4]   '''

