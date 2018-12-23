#Q3
def complete_ISBN(inp):
    count = 0
    for i in range(9):
        count += int(inp[i]) * (i+1)
    checksum = count % 11
    if checksum == 10:
        return inp + "X"
    else: 
        return inp + str(checksum)

# print(complete_ISBN('013601267'))
# print(complete_ISBN('013031997'))
# print(complete_ISBN('020139829'))

#Q4
def get_products(inlist, test):
    d = {}
    for tup in inlist:
        product = 1
        for i in range(len(tup)):
            product *= tup[i]
        d[product] = []
    for tup in inlist:
        product = 1
        for i in range(len(tup)):
            product *= tup[i]
        d[product].append(tup)
    return d, d.get(test, None)

# inlist = [(3,5),(2,2),(2,2,3),(12,2),(7,3),(3,7,1)]
# print(get_products(inlist, 21))
# print(get_products(inlist, 11))


#Q5
#(1) 'new word' (2) 'consonant' (3) 'vowel' (4) 'error'

from libdw import sm
class SpellCheckSM(sm.SM):
    start_state = 'new word'
    consonants = ['k','g','s','t','d','n','h','b','m','r'] #k g s t d n h b m r
    vowels = ['a','e','i','o','u'] #a e i o u
    def get_next_values(self, state, inp):
        if state == 'new word':
            if inp in self.consonants: #A1
                nextstate, output = 'consonant', ''
            elif inp not in self.consonants and inp != ' ': #E8
                nextstate, output = 'error', ''
            elif inp == ' ' : #E10
                nextstate, output = state, ''

        elif state == 'consonant':
            if inp == ' ': #E4
                nextstate, output = 'new word', 'error'
            elif inp not in self.vowels and inp != ' ': #E5
                nextstate, output = 'error', ''
            elif inp in self.vowels: #A2
                nextstate, output = 'vowel', ''
        
        elif state == 'vowel':
            if inp == ' ': #A3
                nextstate, output = 'new word', 'ok'
            elif inp != ' ': #E6
                nextstate, output = 'error', ''

        elif state == 'error':
            if inp == ' ': #E7
                nextstate, output = 'new word', 'error'
            elif inp != ' ': #E9
                nextstate, output = 'error', ''
        return nextstate, output

# a = SpellCheckSM()
# print('test A')
# line = 'k si tu ne mai me pas je '
# print( a.transduce(line, verbose = True))

# print('test B')
# line = 'hi ka ru no de '
# print (a.transduce(line))

# print('test C')
# line = 'mu '
# a.transduce(line,verbose=True)

#Q6
class Parallelogram:
    def __init__(self, side1, side2, diag):
        self.side1 = side1
        self.side2 = side2
        self.diag = diag

    def __str__(self):
        return '{:.2f}'.format(self.diag)

    def set_diagonal(self, i):
        if i >= 0:
            self.diag = i
        else:
            self.diag = 0
        
    def get_diagonal(self):
        return self.diag

    diagonal = property(get_diagonal,set_diagonal)

    def __call__(self):
        return self.side1 + self.side2 > self.diag

    def calc_area(self):
        s = (self.side1 + self.side2 + self.diag)/2
        return  round(2*(s*(s-self.side1)*(s-self.side2)*(s-self.diag))**0.5, 2)

# para = Parallelogram(2,3,4)
# print (para)

# para = Parallelogram(2,3,4)
# para.diagonal = 3
# print (para)

# para = Parallelogram(2,3,4)
# para.diagonal = -1
# print (para)

# para = Parallelogram(3,4,5)
# print (para())

# para = Parallelogram(3,4,8)
# print (para())


class Rhombus(Parallelogram):
    def __call__(self):
        return self.side1 + self.side2 > self.diag and  self.side1 == self.side2

class Rectangle(Parallelogram):
    def __call__(self):
        return self.side1**2 + self.side2**2 == self.diag**2

    def calc_area(self):
        return round(self.side1 * self.side2, 2)

class Square(Rectangle):
    def __call__(self):
        return int(self.side1**2 + self.side2**2) == int(self.diag**2)
    def calc_area(self):
        return round(self.side1**2,2)

# rect = Rectangle(3,4,6)
# print (rect())

# rhom = Rhombus(3,3,2)
# print (rhom())

# squr = Square(2,2,8**0.5)
# print (squr())


# para = Parallelogram(3,4,2)
# print (para.calc_area())

# para = Parallelogram(5,7,9)
# print (para.calc_area())

# rect = Rectangle(3,4,5)
# print (rect.calc_area())

# rhom = Rhombus(3,3,4)
# print (rhom.calc_area())

# squr= Square(2,2,2.83)
# print (squr.calc_area())

class MyTask(object):
    def __init__(self, deadline, duration):
        self.deadline = deadline
        self.duration = duration
    def __str__(self):
        return 'T(%d,%d)' %(self.deadline, self.duration)

def procrastination(assignment):
    latest = 0
    for task in assignment:
        if task.deadline > latest:
            latest = task.deadline
    print(latest)


assignments = [ MyTask(9,1), MyTask(9,2), MyTask(7,1) ]
print (procrastination(assignments))
assignments1 = [ MyTask(3,2), MyTask(3,2) ]
print (procrastination(assignments1))
assignments2 = [ MyTask(9,1), MyTask(9,2), MyTask(4,3) ]
print (procrastination(assignments2))
assignments3 = [MyTask(14,10), MyTask(33,2), MyTask(5,3),
MyTask(14,1), MyTask(10,2)]
print (procrastination(assignments3))