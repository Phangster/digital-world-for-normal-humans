import numpy as np
import scipy.constants as c
a=c.physical_constants['Bohr radius'][0]
from math import sqrt
from math import sin
from math import cos

def spherical_to_cartesian(r, theta, phi):
    x = round(r*(sin(theta))*cos(phi), 5)
    y = round(r*(sin(theta))*sin(phi), 5)
    z = round(r*cos(theta), 5)
    return(x,y,z)

def cartesian_to_spherical(x,y,z):
    r = sqrt(x**2 + y**2 + z**2)
    r = np.round(r, 5)      
    theta = np.arctan((np.sqrt(x**2 + y**2))/z)
    theta = np.round(theta, 5)
    phi = np.arctan(y/x) if x != 0 else (np.pi/2)
    phi = np.round(phi, 5)
    return(r, theta, phi)

def absolute(cnumber):
    cnumber = cnumber.real + cnumber.imag*1j
    magnitude = sqrt(cnumber.real**2+cnumber.imag**2)
    return(magnitude)

import math as c
def angular_wave_func(m, l, theta, phi):
    if l == 0 and m == 0:
        wave_func = np.sqrt(1/(4*np.pi))
        return np.round(wave_func, 5)
    elif l == 1:
        if m == 0:
            wave_func = (np.sqrt(3/(4*np.pi)))*np.cos(theta)
            return np.round(wave_func, 5)
        elif m == 1:
            wave_func = -np.sqrt(3/(8*np.pi))*np.sin(theta)*np.exp(phi*1j)
            return np.round(wave_func, 5)
        elif m == -1:
            wave_func = (np.sqrt(3/(8*np.pi)))*np.sin(theta)*np.exp(phi*-1j)
            return np.round(wave_func, 5)
    elif l == 2:
        if m == 2:
            wave_func = (np.sqrt(15/(32*np.pi)))*((np.sin(theta))**2)*np.exp(2*phi*1j)
            return np.round(wave_func, 5)
        elif m == 1:
            wave_func = -(np.sqrt(15/(8*np.pi)))*(np.cos(theta))*(np.sin(theta))*np.exp(phi*1j)
            return np.round(wave_func, 5)
        elif m == 0:
            wave_func = (np.sqrt(5/(16*np.pi)))*((3*(np.cos(theta))**2) - 1)
            return np.round(wave_func, 5)
        elif m == -1:
            wave_func = np.sqrt(15/(8*np.pi))*(np.cos(theta))*(np.sin(theta))*np.exp(-phi*1j)
            return np.round(wave_func, 5)
        elif m == -2:
            wave_func = (np.sqrt(15/(32*np.pi)))*((np.sin(theta))**2)*np.exp(-2*phi*1j)
            return np.round(wave_func, 5) 
    elif l == 3:
        if m == 3:
            wave_func = -(np.sqrt(35/(64*np.pi)))*((np.sin(theta))**3)*np.exp(phi*3j)
            return np.round(wave_func, 5)
        elif m == 2:
            wave_func = (np.sqrt(105/(32*np.pi)))*(np.cos(theta))*((np.sin(theta))**2)*np.exp(phi*2j)
            return np.round(wave_func, 5) 
        elif m == 1:
            wave_func = -(np.sqrt(21/(64*np.pi)))*(np.sin(theta))*((5*(np.cos(theta))**2) - 1)*(np.exp(phi*1j))
            return np.round(wave_func, 5) 
        elif m == 0:
            wave_func = (np.sqrt(7/(16*np.pi)))*((5*(np.cos(theta))**3) - 3*(np.cos(theta)))
            return np.round(wave_func, 5)
        elif m == -1:
            wave_func = (np.sqrt(21/(64*np.pi)))*(np.sin(theta))*((5*(np.cos(theta))**2) - 1)*(np.exp(phi*-1j))
            return np.round(wave_func, 5)
        elif m == -2:
            wave_func = (np.sqrt(105/(32*np.pi)))*(np.cos(theta))*((np.sin(theta))**2)*np.exp(-phi*2j)
            return np.round(wave_func, 5)
        elif m == -3:
            wave_func = (np.sqrt(35/(64*np.pi)))*((np.sin(theta))**3)*np.exp(-phi*3j)
            return np.round(wave_func, 5)
    else:
        return None


def radial_wave_func(n,l,r):
    b = a**(-3/2)
    if n == 1 and l == 0:
        wave_func = 2*b*np.exp(-r/a)
    elif n == 2:
        if l == 0:
            wave_func = (1/np.sqrt(2))*b*(1-(r/(2*a)))*np.exp(-(r/(2*a)))
        elif l == 1:
            wave_func = (1/np.sqrt(24))*b*(r/a)*np.exp(-r/(2*a))
    elif n == 3:
        if l == 0:
            wave_func = (2/(81*np.sqrt(3)))*b*(27 - 18*(r/a) + 2*(r/a)**2)*np.exp(-r/(3*a))
        elif l == 1:
            wave_func = (8/(27*np.sqrt(6)))*b*(1 - (r/(6*a)))*(r/a)*np.exp(-r/(3*a))
        elif l == 2:
            wave_func = (4/(81*np.sqrt(30)))*b*(r/a)**2*np.exp(-r/(3*a))
    elif n == 4:
        if l == 0:
            wave_func = 0.25*b*(1 - 0.75*(r/a) + (0.125*(r/a)**2) - (1/192)*(r/a)**3)*np.exp(-r/(4*a))
        elif l == 1:
            wave_func = (np.sqrt(5)/(16*np.sqrt(3)))*b*(r/a)*(1 - 0.25*(r/a) + (1/80)*(r/a)**2)*np.exp(-r/(4*a))
        elif l == 2:
            wave_func = (1/(64*np.sqrt(5)))*b*(r/a)**2*(1 - (1/12)*(r/a))*np.exp(-r/(4*a))
        elif l == 3:
            wave_func = (1/(768*np.sqrt(35)))*b*(r/a)**3*np.exp(-r/(4*a)) 
    wave_func = wave_func/b
    return np.round(wave_func, 5)

def linspace(start, stop, num = 50):
    lst = []
    i = start
    while i >= start and i <= stop:
        lst.append (round(i, 5))
        i += (stop - start)/(num - 1)
    return lst

def x_array():
    lst_2 = []
    for i in range(len(y)):
        lst_1 = []
        for j in range(len(x)):
            lst = []
            for k in range(len(z)):
                lst.append (float(x[j]))
            lst_1.append(lst)
        lst_2.append(lst_1)
    return lst_2
        
def y_array():
    lst_2 = []
    for i in range(len(y)):
        lst_1 = []
        for j in range(len(x)):
            lst = []
            for k in range(len(z)):
                lst.append (float(y[i]))
            lst_1.append(lst)
        lst_2.append(lst_1)
    return lst_2

def z_array():
    lst_2 = []
    for i in range(len(y)):
        lst_1 = []
        for j in range(len(x)):
            lst = []
            for k in range(len(z)):
                lst.append (float(z[k]))
            lst_1.append(lst)
        lst_2.append(lst_1)
    return lst_2         

def meshgrid(x_1,y_1,z_1):
    global x
    x = x_1
    global y
    y = y_1
    global z
    z = z_1
    return y_array(), x_array(), z_array()

cartesian_to_spherical_vector = np.vectorize(cartesian_to_spherical)
absolute_vector = np.vectorize(absolute)
angular_vector = np.vectorize(angular_wave_func)
radial_wave_func_vector = np.vectorize(radial_wave_func)

def hydrogen_wave_func(n,l, m, roa, Nx, Ny, Nz):
    x = linspace(-roa, roa, Nx)
    y = linspace(-roa, roa, Ny)
    z = linspace(-roa, roa, Nz)
    x,y,z = np.array(meshgrid(y,x,z))
    r,theta,phi = cartesian_to_spherical_vector(x,y,z)
    r = r*a
    radial_solution = radial_wave_func_vector(n,l,r)
    if m < 0:
        angular_soln = (1j/sqrt(2))*(angular_vector(m,l,theta,phi) - ((-1)**m)*angular_vector(-m,l,theta,phi))
    elif m == 0:
        angular_soln = angular_vector(0,l,theta,phi)
    else:
        angular_soln = (1/sqrt(2))*(angular_vector(-m,l,theta,phi) + ((-1)**m)*angular_vector(m,l,theta,phi))
    mag = absolute_vector(angular_soln*radial_solution)**2
    return x,y,z, np.round(mag, 5)
