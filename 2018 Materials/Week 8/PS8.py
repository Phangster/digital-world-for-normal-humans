#Q1
class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def magnitude(self):
        return (self.x**2+self.y**2)**0.5

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 


# a = Coordinate(3,4)

# print(a.x)
# print(a.y)
# print(a.magnitude())
# a.translate(3, 4)
# print(a.x,a.y)

# b = Coordinate(x=3, y=4)

# print(a==b)


#Q2
class Celsius:
    def __init__(self, temperature=0):
        if temperature < -273:
            self._temperature = -273
        else:
            self._temperature = temperature
    def to_fahrenheit(self):
        return self._temperature * (9/5) +32
    def get_temperature(self):
        return self._temperature
    def set_temperature(self, value):
        if value < -273:
            self._temperature = -273
        else:
            self._temperature = value
    
    temperature = property(get_temperature, set_temperature)

c = Celsius(100)
c.temperature = -5000
print(c.temperature)
# print(c.get_temperature())

# c.temperature = -300
# print(c.get_temperature())

#Q3
import time
class StopWatch:
    def __init__ (self):
        self.start_time = time.time()
        self.end_time = end_time

    def start(self):
        self.start_time = time.time()
        self.end_time = -1

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        if self.end_time == -1:
            return None
        else: 
            return float(self.end_time - self.start_time)


#Q4
class Line:
    def __init__(self, c0=0, c1=0):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        return float(self.c0 + self.c1*x)

    def table(self,L , R, n):   
        string = ''
        incriment = (R-L)/(n-1)
        if L == R:
            n = 1
        l = [L+incriment*i for i in range(n)]
        for i in l:
            string += '{0:10.2f}{1:10.2f}'.format(i, self.c0 + self.c1*i)
            string += '\n'
        if n == 0:
            return "Error in printing table"
        return string

# a = Line(1,2)
# print(a(2))
# print(a.table(1,5,4))

# a = Line(-1,2)
# print(a(2))
# print(a.table(-1,5,10))

# a = Line(3,4)
# print(a(2))
# print(a.table(1,5,15))

# a = Line(3,4)
# print(a(2))
# print(a.table(1,1,15))

# a = Line(3,4)
# print(a(2))
# print(a.table(1,5,0))
'''
    Test case 1 : c0 = 1, c1 = 2, x = 2, L = 1, R = 5, N = 4                                                                                                                       
    ans =  (5.0, '      1.00      3.00\n      2.33      5.67\n      3.67      8.33\n      5.00     11.00\n')                                                                       
    Test case 1 : c0 = 1, c1 = 2, x = 2, L = 1, R = 5, N = 4                                                                                                                       
    ans =  (5, '1.00      3.00\n2.33      5.67\n3.67      8.33\n5.00     11.00\n')                                                                                                 
    Test case 2 : c0 = -1, c1 = 2, x = 2, L = -1, R = 5, N = 10                                                                                                                    
    Test case 2 : c0 = -1, c1 = 2, x = 2, L = -1, R = 5, N = 10                                                                                                                    
    Test case 3 : c0 = 3, c1 = 4, x = 2, L = 1, R = 5, N = 15                                                                                                                      
    Test case 3 : c0 = 3, c1 = 4, x = 2, L = 1, R = 5, N = 15                                                                                                                      
    Test case 4 : c0 = 3, c1 = 4, x = 2, L = 1, R = 1, N = 15                                                                                                                      
    Test case 4 : c0 = 3, c1 = 4, x = 2, L = 1, R = 1, N = 15                                                                                                                      
    Test case 5 : c0 = 3, c1 = 4, x = 2, L = 1, R = 5, N = 0                                                                                                                       
    Test case 5 : c0 = 3, c1 = 4, x = 2, L = 1, R = 5, N = 0                                                                                                                       
    Score: [0/5]               
'''

#HW1
class Time:
    def __init__(self, h=0, m=0, s=0):
        self._hours = h
        self._minutes = m
        self._seconds = s
    
    def set_seconds(self, seconds):
        if seconds >=86400:
            seconds = seconds % 86400
        hours = seconds // 3600
        remaining_minutes = seconds % 3600
        minutes = remaining_minutes // 60 
        seconds = remaining_minutes % 60
        print('{}:{}:{}'.format(hours, minutes, seconds))
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
    
    def get_seconds(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds
    
    elapsed_time = property(get_seconds, set_seconds)

    def __str__(self):
        return "Time:{:2d}:{:2d}:{:2d}".format(self._hours, self._minutes, self._seconds)

# a=Time()
# a.set_seconds(555550)
# print(a)

#HW2
class Account:    
    def __init__(self, owner, account_number, amount):
        self._owner = owner
        self._account_number = account_number
        self._balance = amount

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def __str__(self):
        return "{}, {}, balance: {}".format(self._owner,self._account_number,self._balance)

#HW3
class Diff:
    def __init__(self ,f , h = 1e-4):
        self.f = f
        self.h = h

    def __call__(self, x):
        return ( self.f(x+self.h) - self.f(x) ) / self.h


#HW4
class Polynomial:
    def __init__(self, l= []):
        self.coeff = l

    def __add__(self, p2):
        l1 = [l for l in self.coeff]
        l2 = [l for l in p2.coeff]
        # print (l1, l2)
        while len(l2) > len(l1):
            l1.append(0)
        while len(l1) > len(l2):
            l2.append(0)
        return Polynomial([sum(t) for t in list(zip(l1, l2))])

    def __sub__(self, p2):
        l1 = [l for l in self.coeff]
        l2 = [l for l in p2.coeff]
        # print (l1, l2)
        while len(l2) > len(l1):
            l1.append(0)
        while len(l1) > len(l2):
            l2.append(0)
        return Polynomial([t[0] - t[1] for t in list(zip(l1, l2))])
    
    def __call__(self, x):
        return [l for l in self.coeff], sum([coeff*x**num for num, coeff in enumerate(self.coeff)])
        

    def __mul__(self, p2):
        print(self.coeff)
        print(p2.coeff)
        lsuper = [0 for i in range(len(self.coeff + p2.coeff) -1)]
        for i in range(len(self.coeff)):
            for j in range(len(p2.coeff)):
                lsuper[i+j] += self.coeff[i] * p2.coeff[j]
        return Polynomial(lsuper)

    def differentiate(self):
        self.coeff = [num*coeff for num, coeff in enumerate(self.coeff)][1:]

    def derivative(self):
        return Polynomial([num*coeff for num, coeff in enumerate(self.coeff)][1:])

# p1 = Polynomial([1, -1])
# print(p1.coeff)
# p2 = Polynomial ([0, 1, 0, 0, -6, -1])
# print(p2.coeff)

# # p3 = p1 + p2
# # print(p3.coeff)

# p4 = p1*p2
# print(p4.coeff)

# p5 = p2.derivative ()
# print(p5.coeff)

# p = Polynomial ([1, -1])
# q = Polynomial ([0, 1, 0, 0, -6, -1])
# r=p-q
# print(r.coeff)
# print(r(3))

'''
    Polynomials [2, 1, -1] and [3, 1, 0, 0, -6, -1] are added                                                                                                                      
    Pass:  True                                                                                                                                                                    
    Polynomial [3, 1, 0, 0, -6, -1] is subtracted from                                                                                                                             
                       polynomial [2, 1, -1] and resultant evaluated with x = 3                                                                                                    
    Note: A tuple with coeff list and evaluated value is checked.                                                                                                                  
    Pass:  False                                                                                                                                                                   
    Polynomials [1, 2, 3, 4] and [1, 2, 3, 4] are multiplied                                                                                                                       
    [1, 2, 3, 4]                                                                                                                                                                   
    [1, 2, 3, 4]                                                                                                                                                                   
    Pass:  True                                                                                                                                                                    
    Polynomial [1, 3, 5, 7, 9] is differentiated                                                                                                                                   
    Pass:  True                                                                                                                                                                    
    Copy of polynomial [2, 4, 6, 8, 10] is differentiated                                                                                                                          
    Pass:  True                                                                                                                                                                    
    Score: [4/5]      
'''