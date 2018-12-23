import math

def deg_to_rad(d):
    r= d/180*math.pi
    return round(r, 5)

def rad_to_deg(r):
    d= r/math.pi*180
    return round(d, 5)

print(deg_to_rad(180))
print(rad_to_deg(3.14))

def spherical_to_cartesian(r, theta, phi):
    x = r*math.sin(theta)*math.cos(phi)
    y = r*math.sin(theta)*math.sin(phi)
    z = r*math.cos(theta)
    x = round(x, 5)
    y = round(y, 5)
    z = round(z, 5)
    return x,y,z

print(spherical_to_cartesian(3, math.pi, 0))

def cartesian_to_spherical(x, y, z):
    r = (x**2+y**2+z**2)**0.5
    theta = math.acos(z/r)
    phi = math.acos(x/(x**2+y**2)**0.5)
    r = round(r, 5)
    theta = round(theta, 5)
    phi = round(phi, 5)
    return r, theta, phi

def absolute (complex):
    real = complex.real
    imaginary = complex.imag
    absolute = (real**2+imaginary**2)**0.5
    return absolute

print(absolute(1 + 2j))
