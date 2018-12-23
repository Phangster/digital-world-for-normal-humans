print "Q1:"

#import string
#import numbers

def maxOccurrences(inp):
    diction = {}
    newlist = []
    result = []
    inp = inp.split()
    for i in inp:
        newlist.append(int(i))
    for i in set(newlist):
        count = 0
        for j in newlist:
            if j == i:
                count += 1
        diction[i] = count
    maxvalue = max(diction.values())
    for i in diction:
        if diction[i] == maxvalue:
            result.append(i)
    finalresult = [0, 0]
    finalresult[0] = sorted(result)
    finalresult[1] = maxvalue
    return tuple(finalresult)


inp = '9 30 3 9 3 2 4'
result = maxOccurrences(inp)
print result

print "\n"
##############################################################################################
##############################################################################################

print "Q2:"
import libdw.sm as sm

class RingCounter(sm.SM):
    startState=0
    def getNextValues(self,state,inps):
        if inps==0:
            if state<7:
                state+=1
                return state,format(state,'03b')
            else:
                state=0
                return state,format(state,'03b')
        else:
            state=0
            return state,format(state,'03b')

print 'test 1'
r=RingCounter()
print r.transduce([0,0,0,0,0,0,0,0,0])

print "\n"
##############################################################################################
##############################################################################################
print "Q3:"

class Avatar(object):
    def __init__(self, name,hp=100,position=(1,1)):
        self.name=name
        self.hp=hp
        self.position=position

    def getName(self):
        return self._name
    def setName(self, value):
        self._name=value
    def getHP(self):
        return self.hp
    def setHP(self, value):
        self.hp=value
    def getPosition(self):
        return self._position
    def setPosition(self, value):
        self._position=value
    def heal(self,input=1):
        if input >=0:
            self.hp+=input
            return self.hp
    def attacked(self,input=-1):
        if input<0:
            self.hp+=input
            return self.hp

print 'test 4: getPosition(), setPosition()'
a=Avatar('John')
a.setPosition((1,3))
print a.getPosition()
print 'test 5: getHP(), setHP()'
a=Avatar('John')
a.setHP(200)
print a.getHP()
print 'test 6: heal()'
a=Avatar('John')
a.heal(5)
print a.getHP()
print 'test 7: attacked()'
a=Avatar('John')
a.attacked(20)
print a.getHP()
print 'test 8: heal()'
a=Avatar('John')
a.heal()
print a.getHP()
print 'test 9: attacked()'
a=Avatar('John')
a.attacked()
print a.getHP()
print 'test 10: heal(), attacked() '
a=Avatar('John')
a.attacked(2)
a.heal(-2)
print a.getHP()

print "\n"
##############################################################################################
##############################################################################################
print "Q5:"

class Map(object):
    """docstring for Map."""
    def __init__(self, world):
        super(Map, self).__init__()
        self.world=world
    def whatIsAt(self,location):
        for i in self.world:
            if i==location:
                if self.world[i]=='x':
                    return 'Exit'
                elif self.world[i]==0:
                    return 'Wall'
                elif self.world[i]>0:
                    return 'Food'
                elif self.world[i]<0:
                    return 'Enemy'
        return 'Empty'
    def getEnemyAttack(self,location):
        result=self.whatIsAt(location)
        if result=='Enemy':
            return self.world[location]
        else:
            return False
    def getFoodEnergy(self,location):
        result=self.whatIsAt(location)
        if result=='Food':
            return self.world[location]
        else:
            return False
    def removeEnemy(self,location):
        result=self.whatIsAt(location)
        if result=='Enemy':
            del self.world[location]
            return True
        else:
            return False
    def eatFood(self,location):
        result=self.whatIsAt(location)
        if result=='Food':
            del self.world[location]
            return True
        else:
            return False
    def getExitPosition(self):
        for i in self.world:
            if self.world[i]=='x':
                return i
        else:
            return None

world={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0, (5,0): 0,
(0,1):0, (1,1): 2, (2,1):-3, (5,1): 0, (0,2):0, (5,2): 0, (0,3):0,
(5,3): 0, (0,4):0, (5,4): 0, (0,5):0, (1,5):0 , (2,5):0, (3,5): 0,
(4,5):'x', (5,5): 0}
print 'test 1: object instantiation'
m=Map(world)
print m.world
print 'test 8: whatIsAt'
print m.whatIsAt((1,4))
print 'test 9: getFoodEnergy'
print m.getFoodEnergy((1,4))
print 'test 10: getEnemyAttack'
print m.getEnemyAttack((1,4))
print 'test 11: whatIsAt'
print m.whatIsAt((4,5))
print 'test 12: getExitPosition'
print m.getExitPosition()
print 'test 13: eatFood'
w1=m.whatIsAt((1,1))
w2=m.eatFood((1,1))
w3=m.whatIsAt((1,1))
print (w1,w2,w3)
print 'test 14: test aliasing'
print m.world == world

print "\n"
##############################################################################################
##############################################################################################

print "Q7"


import libdw.sm as sm

class Avatar(object):
    def __init__(self, name,hp=100,position=(1,1)):
        self.name=name
        self.hp=hp
        self.position=position

    def getName(self):
        return self.name
    def setName(self, value):
        self.name=value
    def getHP(self):
        return self.hp
    def setHP(self, value):
        self.hp=value
    def getPosition(self):
        return self.position
    def setPosition(self, value):
        self.position=value
    def heal(self,input=1):
        if input >=0:
            self.hp+=input
            return self.hp
    def attacked(self,input=-1):
        if input<0:
            self.hp+=input
            return self.hp

class Map(object):
    """docstring for Map."""
    def __init__(self, world):
        super(Map, self).__init__()
        self.world=world
    def whatIsAt(self,location):
        for i in self.world:
            if i==location:
                if self.world[i]=='x':
                    return 'Exit'
                elif self.world[i]==0:
                    return 'Wall'
                elif self.world[i]>0:
                    return 'Food'
                elif self.world[i]<0:
                    return 'Enemy'
        return 'Empty'

    def search(self,key):
        resultlist=[]
        for i in self.world:
            if self.world[i]==key:
                resultlist.append[i]
        return resultlist

    def getEnemyAttack(self,location):
        result=self.whatIsAt(location)
        if result=='Enemy':
            return self.world[location]
        else:
            return False
    def getFoodEnergy(self,location):
        result=self.whatIsAt(location)
        if result=='Food':
            return self.world[location]
        else:
            return False
    def removeEnemy(self,location):
        result=self.whatIsAt(location)
        if result=='Enemy':
            del self.world[location]
            return True
        else:
            return False
    def eatFood(self,location):
        result=self.whatIsAt(location)
        if result=='Food':
            del self.world[location]
            return True
        else:
            return False
    def getExitPosition(self):
        for i in self.world:
            if self.world[i]=='x':
                return i
        else:
            return None



class DW2Game(sm.SM):
    """docstring for DW2Game."""
    def __init__(self,Avatar,Map):
        self.startState=(Avatar,Map)
    def getNextValues(self,nowstate,inps):
        if inps[0]=='move':
            newposition=self.movement(inps[1],nowstate[0])
            self.MoveAction(newposition,nowstate[0],nowstate[1])
            return(nowstate,(nowstate[0].getName(),nowstate[0].getPosition(),nowstate[0].getHP()))
        elif inps[0]=='attack':
            newposition=self.movement(inps[1],nowstate[0])
            self.AttackAction(newposition,nowstate[0],nowstate[1])
            return(nowstate,(nowstate[0].getName(),nowstate[0].getPosition(),nowstate[0].getHP()))


    def done(self,state):
        (Avatar,Map)=state
        location=Avatar.getPosition()
        item=Map.whatIsAt(location)
        if item=='Exit':
            return True
        else:
            return False

    def MoveAction(self,location,Avatar,Map):
        item=Map.whatIsAt(location)
        if item =='Wall':
            pass
        elif item=='Enemy':
            newHP=Avatar.getHP()+Map.getEnemyAttack(location)
            Avatar.setHP(newHP)
        elif item=='Empty'or item=='Exit':
            Avatar.setPosition(location)
        elif item=='Food':
            newHP=Avatar.getHP()+Map.getFoodEnergy(location)
            Avatar.setHP(newHP)
            Map.eatFood(location)
            Avatar.setPosition(location)



    def AttackAction(self,location,Avatar,Map):
        item=Map.whatIsAt(location)
        if item =='Wall':
            pass
        elif item=='Enemy':
            Map.removeEnemy(location)
        elif item=='Empty':
            pass
        elif item=='Food':
            pass


    def movement(self,command,Avatar):
        if command=='right':
            position=Avatar.getPosition()
            x=position[0]+1
            y=position[1]
            newposition=(x,y)
            return newposition
        elif command =='left':
            position=Avatar.getPosition()
            x=position[0]-1
            y=position[1]
            newposition=(x,y)
            return newposition
        elif command =='up':
            position=Avatar.getPosition()
            x=position[0]
            y=position[1]-1
            newposition=(x,y)
            return newposition
        elif command=='down':
            position=Avatar.getPosition()
            x=position[0]
            y=position[1]+1
            newposition=(x,y)
            return newposition









world2={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0,
(5,0): 0, (0,1):0, (5,1): 0, (0,2):0, (1,2): -2, (5,2): 0,
(0,3):0, (2,3): 3, (5,3): 0, (0,4):0, (5,4): 0, (0,5):0,
(1,5):0, (2,5):0, (3,5): 0, (4,5):'x', (5,5): 0,}
print 'test 5'
inp=[('move','right'),('move','right'),('move','right'),
('move','down'),('move','left'),('move','left'),('move','left'),
('attack','left'),('move','left'),('move','left'),('move','down'),
('move','right'),('move','right'),('move','right'),('move','down'),('move','down'),
('move','down')]
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
print g.transduce(inp)
print 'test 6'
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
g.start()
n,o=g.getNextValues(g.startState,('move','right'))
ans = g.state[0].getPosition() == n[0].getPosition()
print ans, g.state[0].getPosition(), n[0].getPosition()
