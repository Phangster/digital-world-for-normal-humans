import numpy as np
def compTrace(A):
    trace=np.trace(A)
    return trace


A = [[2.2, 2, 3.1], [4, 5, 6], [7, 8, 9]]
print compTrace(A)

###############################################################################
###############################################################################

def findKey(dInput, strInput):
    result=[]
    for i in dInput:
        if dInput[i]==strInput:
            result.append(i)
    result=sorted(result)
    return result

dInput = {1:'singapore', 20:'china', 4:'japan', 5:'china', 10:'japan'}
result=findKey(dInput,'korea')
print result
###############################################################################
###############################################################################
from math import *
class Square(object):
    """docstring for Square."""
    
    def __init__(self, x=0,y=0,sideLength=1.0):
        super(Square, self).__init__()
        self.x=x
        self.y=y
        self.sideLength=sideLength
        
    def getCenter(self):
        return(self.x,self.y)
        
    def getSideLength(self):
        return self.sideLength
        
    def getArea(self):
        return(self.sideLength**2)
        
    def getPerimeter(self):
        return self.sideLength*4
        
    def containPoint(self,px,py):
        if px <= self.x+self.sideLength/2 and px>=self.x-self.sideLength/2:
            if py <= self.y+self.sideLength/2 and py>=self.y-self.sideLength/2:
                return True
        return False
        
    def containSquare(self,insquare):
        insquarecenter=insquare.getCenter()
        insquarelength=insquare.getSideLength()
        
        if insquarecenter[0]-(insquarelength/2)>=self.x-(self.sideLength/2) \
and insquarecenter[0]+(insquarelength/2)<=self.x+(self.sideLength/2):
    
            if insquarecenter[1]-(insquarelength/2)>=self.y-(self.sideLength/2) \
and insquarecenter[1]+(insquarelength/2)<=self.y+(self.sideLength/2):
                return True
                
        return False


s = Square(x=1,y=1, sideLength=2.0)
# print s.getCenter()
# print s.getSideLength()
# print s.getArea()
# print s.getPerimeter()
# print s.containPoint(0,0)
# print s.containPoint(0,-0.5)
# print s.containPoint(1,1.5)
# print s.containSquare( Square(x=1.5, y = 1, sideLength = 1))
print s.containSquare( Square(x=1.5, y = 1, sideLength = 1.1))
# s2 = Square()
# print s2.getCenter()
# print s2.getSideLength()
# print s2.getPerimeter()
###############################################################################
###############################################################################
import libdw.sm as sm

class Elevator(sm.SM):
    
    startState='First'
    
    def getNextValues(self,state,inps):
        if state=='First':
            if inps=='Down':
                return state,state
            elif inps=='Up':
                state='Second'
                return state,state
                
        if state=='Second':
            if inps=='Down':
                state='First'
                return state,state
            elif inps=='Up':
                state='Third'
                return state,state
                
        if state=='Third':
            if inps=='Down':
                state='Second'
                return state,state
            elif inps=='Up':
                return state,state
                
e = Elevator()
print e.transduce( ['Up', 'Up', 'Up', 'Up', 'Down', 'Down', 'Down', 'Up'])

###############################################################################
###############################################################################

def countNumOpenLocker(k):
    locker=[0]*k
    for i in range(1,k+1):
        if i==1:
            locker[:]=[1]*k
        elif i==2:
            for i in range(k):
                if (i+1)%2==0:
                    locker[i]=0
        elif i==3:
            for i in range(k):
                if (i+1)%3==0:
                    if locker[i]==1:
                        locker[i]=0
                    else:
                        locker[i]=1
        elif i>3:
            n=i
            for i in range(k):
                if (i+1)%n==0:
                    if locker[i]==1:
                        locker[i]=0
                    else:
                        locker[i]=1
    count=0
    for i in range(k):
        if locker[i]==1:
            count+=1
    return count

print countNumOpenLocker(2000)
