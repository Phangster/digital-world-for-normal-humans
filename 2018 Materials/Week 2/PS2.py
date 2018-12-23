#Cohort problems
#Question 1 ---------------------------------------------------------------------------------------------
def fahrenheit_to_celsius(fahrenheit):
  _celsius = (fahrenheit - 32)*(5/9)
  return _celsius

print ( fahrenheit_to_celsius (32) )
print ( fahrenheit_to_celsius ( -40))
print ( fahrenheit_to_celsius (212) )

#Questions 2---------------------------------------------------------------------------------------------
def position_velocity(v, t):
  y = round(v*t - 0.5*9.81*(t**2), 2)
  y_prime = round(v - 9.81*t, 2)
  _output = (y, y_prime)
  return _output

print(position_velocity(5.0, 10.0))
print(position_velocity(5.0, 0))
print(position_velocity(0, 5.0))

#Questions 3---------------------------------------------------------------------------------------------
def minutes_to_years_days(mins):
  year = int(mins/60/24/365)
  days = int(mins/60/24 % 365)
  _output = (year, days)
  return _output
  
print ( minutes_to_years_days (1000000000) )
print ( minutes_to_years_days (2000000000) )

#Question 4 ------------------------------------------------------------------------------------------------
class Coordinate:
    x = 0
    y = 0
  
def area_of_triangle(p1, p2, p3):
  s1 = length(p1, p2)
  s2 = length(p2, p3)
  s3 = length(p1, p3)
  s = (s1+s2+s3)/2
  area = round((s*(s-s1)*(s-s2)*(s-s3))**0.5, 2)
  return area

def length(p1, p2):
  x = abs(p1.x - p2.x)
  y = abs(p1.y - p2.y)
  length = (x**2+y**2)**0.5
  return length

print (" Test Case 1")
p1= Coordinate ()
p1.x =1.5
p1.y= -3.4
p2= Coordinate ()
p2.x =4.6
p2.y=5
p3= Coordinate ()
p3.x =9.5
p3.y= -3.4
ans= area_of_triangle (p1 ,p2 ,p3)
print (ans)

print (" Test Case 2")
p1= Coordinate ()
p1.x =2.0
p1.y= -3.4
p2= Coordinate ()
p2.x =4.6
p2.y=5
p3= Coordinate ()
p3.x =9.5
p3.y= -1.4
ans= area_of_triangle (p1 ,p2 ,p3)
print (ans)

print (" Test Case 3")
p1= Coordinate ()
p1.x =1.5
p1.y =3.4
p2= Coordinate ()
p2.x =4.6
p2.y=5
p3= Coordinate ()
p3.x= -1.5
p3.y =3.4
ans= area_of_triangle (p1 ,p2 ,p3)
print (ans)

print (" Test Case 4")
p1= Coordinate ()
p1.x= -1.5
p1.y =3.4
p2= Coordinate ()
p2.x =4.6
p2.y=5
p3= Coordinate ()
p3.x =4.3
p3.y= -3.4
ans= area_of_triangle (p1 ,p2 ,p3)
print (ans)


#Question 5 ----------------------------------------------------------------------------------------------

def compound_value_sixth_month(principle, interest):
  amount = 0
  m_rate = interest/12
  for i in range(6):
    amount+=principle
    amount = amount*(1+m_rate)
  return round(amount, 2)

print ( compound_value_sixth_month (100 ,0.05) )
print ( compound_value_sixth_month (100 ,0.03) )
print ( compound_value_sixth_month (200 ,0.05) )
print ( compound_value_sixth_month (200 ,0.03) )

#Homework
#Question 1--------------------------------------------------------------------------------
def celsius_to_fahrenheit(fahrenheit):
  _celsius = fahrenheit*(9/5) +32
  return _celsius

print ( celsius_to_fahrenheit (0))
print ( celsius_to_fahrenheit ( -40))
print ( celsius_to_fahrenheit (100) )

#Question 2--------------------------------------------------------------------------------
import math

def area_vol_cylinder(r, l):
  area = math.pi*r**2
  vol = area*l
  output = (round(area, 2), round(vol, 2))
  return output

print ( area_vol_cylinder (1.0 ,2.0) )
print ( area_vol_cylinder (2.0 ,2.3) )
print ( area_vol_cylinder (1.5 ,4) )
print ( area_vol_cylinder (2.2 ,5.0) )


#Question 3--------------------------------------------------------------------------------
def wind_chill_temp(t, v):
  twc = 35.74 + 0.6215*t - 35.75*v**0.16 + 0.4275*t*v**0.16
  return twc

print ( wind_chill_temp (5.3 ,6) )
print ( wind_chill_temp (2.2 ,4) )

#Question 4--------------------------------------------------------------------------------
def bmi(w_p, h_i):
  w_kg = 0.45359237*w_p
  h_m = 0.0254*h_i
  bmi = (w_kg)/(h_m**2)
  return bmi

print ( bmi (120 ,60) )
print ( bmi (100 ,50) )

#Question 5--------------------------------------------------------------------------------
def investment_val(p , r, y):
  total = p*(1+r/1200)**(y*12)
  return round(total , 2)

print ( investment_val (1000 ,4.25 ,1) )
print ( investment_val (1500 ,3.25 ,2) )

#Bonus: Newton's algorithm--------------------------------------------------------------------------------------
print("""


""")
def newtonSqrt(n):
  if n**0.5 == int(n**0.5):
    print(n**0.5)
  
  else:
    return "invalid input"

print(newtonSqrt(100))

