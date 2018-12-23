#Q3
def maxOccurrences(inp):
    inp_list = [int(i) for i in inp.split(' ')]
    d = {}
    for k in inp_list:
        d[k] = d.get(k, 0) + 1
    max_val = max(d.values())
    max_key = [k for k,v in d.items() if v == max_val]
    return max_key, max_val


# print ('test 1')
# inp='2 3 40 3 5 4 -3 3 3 2 0'
# print (maxOccurrences(inp))

# print ('test 2')
# inp='9 30 3 9 3 2 4'
# print (maxOccurrences(inp))

#Q4
from libdw import sm

class RingCounter(sm.SM):
    start_state = '000'
    def get_next_values(self, state, inp):
        count = int(state, base = 2)
        if inp == 1:
            nextstate, output = '000','000'
        elif inp == 0 :
            count += 1
            bin_count = f'{count%7:03b}'#.replace(' ','0')
            nextstate, output = bin_count, bin_count

        return nextstate, output

print ('test 1')
r=RingCounter()
print (r.transduce([0,0,0,0,0,0,0,0,0]))

print ('test 2')
r=RingCounter()
print (r.transduce([0,0,0,1,0,0,0,0,0]))

print ('test 3')
r=RingCounter()
print (r.transduce([0,0,0,1,0,0,1,0,0]))

#Q5

class Avatar():
    def __init__(self, name, hp = 100, position = (1,1)):
        self.name = name
        self.hp = hp
        self.position = position

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getHP(self):
        return self.hp
    
    def setHP(self, hp):
        self.hp = hp

    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position

    def heal(self, amount = 1):
        if amount > 0:
            self.hp += amount
        else:
            pass

    def attacked(self, amount = -1):
        if amount < 0:
            self.hp += amount
        else:
            pass

# print ('test 1: __init__')
# a=Avatar('John')
# print (a.name, a.hp, a.position)

# print ('test 2: __init__')
# a=Avatar('Jane',150,(10,10))
# print (a.name, a.hp, a.position)

# print ('test 3: getName(), setName()')
# a=Avatar('John')
# a.setName('Jude')
# print (a.getName())

# print ('test 4: getPosition(), setPosition()')
# a=Avatar('John')
# a.setPosition((1,3))
# print (a.getPosition())

# print ('test 5: getHP(), setHP()')
# a=Avatar('John')
# a.setHP(200)
# print (a.getHP())

# print ('test 6: heal()')
# a=Avatar('John')
# a.heal(5)
# print (a.getHP())

# print ('test 7: attacked()')
# a=Avatar('John')
# a.attacked(20)
# print (a.getHP())

# print ('test 8: heal()')
# a=Avatar('John')
# a.heal()
# print (a.getHP())

# print ('test 9: attacked()')
# a=Avatar('John')
# a.attacked()
# print (a.getHP())

# print ('test 10: heal(), attacked() ')
# a=Avatar('John')
# a.attacked(2)
# a.heal(-2)
# print (a.getHP() )

#Q6

class Map():
    def __init__(self, world):
        self.world = world
    
    def whatIsAt(self, inp):
        obj = self.world.get(inp, 'Empty')
        try:
            if obj == 'x':
                return 'Exit'
            elif obj == 0:
                return 'Wall'
            elif obj > 0:
                return 'Food'
            elif obj < 0:
                return 'Enemy'
        except Exception as e:
            print(e)
            return obj

    def getEnemyAttack(self, tup):
        obj = self.world.get(tup, False)
        if obj < 0:
            return obj
        else:
            return False

    def getFoodEnergy(self, tup):
        obj = self.world.get(tup, False)
        if obj > 0:
            return obj
        else:
            return False

    def removeEnemy(self, tup):
        obj = self.world.get(tup, False)
        if obj<0:
            del self.world[tup]
            return True
        else:
            return False

    def eatFood(self, tup):
        obj = self.world.get(tup, False)
        if obj>0:
            del self.world[tup]
            return True
        else:
            return False
        
    def getExitPosition(self):
        d_rev = {v:k for k,v in self.world.items()}
        return d_rev.get('x', None)


# world={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0, (5,0): 0,
# (0,1):0, (1,1): 2, (2,1):-3, (5,1): 0, (0,2):0, (5,2): 0, (0,3):0,
# (5,3): 0, (0,4):0, (5,4): 0, (0,5):0, (1,5):0 , (2,5):0, (3,5): 0,
# (4,5):'x', (5,5): 0}

# print ('test 1: object instantiation'  )                                                          
# m=Map(world)
# print (m.world)

# print ('test 2: whatIsAt')
# print (m.whatIsAt((1,0)))

# print ('test 3: whatIsAt')
# print (m.whatIsAt((2,1)))

# print ('test 4: whatIsAt')
# print (m.whatIsAt((1,1)))

# print ('test 5: getFoodEnergy')
# w1=m.getFoodEnergy((1,1))
# w2=m.getFoodEnergy((3,3))
# print (w1,w2)

# print ('test 6: getEnemyAttack')
# w1=m.getEnemyAttack((2,1))
# w2=m.getEnemyAttack((3,3))
# print (w1,w2)

# print ('test 7: removeEnemy')
# w1=m.getEnemyAttack((2,1))
# w2=m.removeEnemy((2,1))
# w3=m.getEnemyAttack((2,1))
# print (w1,w2,w3)

# print ('test 8: whatIsAt')
# print (m.whatIsAt((1,4)))

# print ('test 9: getFoodEnergy')
# print (m.getFoodEnergy((1,4)))

# print ('test 10: getEnemyAttack')
# print (m.getEnemyAttack((1,4)))

# print ('test 11: whatIsAt')
# print (m.whatIsAt((4,5)))

# print ('test 12: getExitPosition')
# print (m.getExitPosition())

# print ('test 13: eatFood')
# w1=m.whatIsAt((1,1))
# w2=m.eatFood((1,1))
# w3=m.whatIsAt((1,1))
# print (w1,w2,w3)

# print ('test 14: test aliasing')
# print (m.world == world)

#Q7
class DW2Game(sm.SM):
    '''I gave up for this one'''
    def __int__(self, Avatar, Map):
        self.state = (Avatar, Map)

    def getNextValues(self, state, inp):  
        pass

    def done(self, state):
        if state[1].getExitPosition() == state[0].getPosition:
            return True
        else:
            return False

# world2={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0,
# (5,0): 0, (0,1):0, (5,1): 0, (0,2):0, (1,2): -2, (5,2): 0,
# (0,3):0, (2,3): 3, (5,3): 0, (0,4):0, (5,4): 0, (0,5):0,
# (1,5):0, (2,5):0, (3,5): 0, (4,5):'x', (5,5): 0,}

# print ('test 1')
# inp=[('move','down'),('attack','down'),('move','down'),(
# 'move','down'),\
# ('move','down'),('move','right'),('move','right'),('move','\
# right'),('move','down'),\
# ('move','down')]
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# print (g.transduce(inp))

