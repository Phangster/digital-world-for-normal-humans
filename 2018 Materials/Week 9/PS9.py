from libdw import sm


#Cohort 1
# class CM(sm.SM):
#     start_state = 0

#     def get_next_state(self, state, inp):
#         print('state: {}, input {}'.format(state, inp))
#         if inp != 50 and inp != 100:
#             nextstate = state
#             output = (state, "--", inp)
#             print(output)
#             return nextstate, output
#         else:
#             nextstate = state + inp
#             if nextstate >= 100:
#                 diff = nextstate - 100
#                 nextstate = 0
#                 output = (0, "coke", diff)
#                 print(output)
#                 return nextstate, output
            
#             else:
#                 output = (nextstate, "--", 0)
#                 print(output)
#                 return nextstate, output

class CM(sm.SM):
    start_state = (0,'--',0)
    
    def get_next_state(self, state, inp):
        #print('state: {}, input {}'.format(state, inp))
        if state[0] == 0:
            if inp == 100:
                next_state = (0, 'coke', 0)
            elif inp == 50:
                next_state = (50, '--', 0)
            else:
                next_state = (0, '--', inp)

        elif state[0] == 50:
            if inp == 50:
                next_state = (0, 'coke', 0)
            elif inp == 100:
                next_state = (0,'coke', 50)
            else: 
                next_state = (50, '--', inp)

        else:
            next_state = (0,'--',0)
        print(inp, next_state)
        return next_state

c=CM()
c.start()
c.step(50)
c.step(50)
c.step(100)
c.step(10)
c.step(50)
c.step(100)
c.step(10)


#Cohort 2
class SimpleAccount(sm.SM):
    def __init__(self, start_balance):
        self.start_state = start_balance

    def get_next_state(self, state, inp):
        print(state, inp)
        if inp < 0 and state <100:
            nextstate = state + inp -5
        else:
            nextstate = state + inp
        # print(nextstate)
        return nextstate #, nextstate

# acct=SimpleAccount (110)
# acct.start ()
# acct.step (10)
# acct.step (-25)
# acct.step (-10)
# acct.step (-5)
# acct.step (20)
# acct.step (20)


#HW1
from libdw import sm

class CommentsSM(sm.SM):
    start_state = None

    def get_next_state(self, state, inp):
        print(state)
        if state == None and inp != '#':
            nextstate = None
        elif state == None and inp == '#':
            nextstate = inp
        elif state != None and inp != '\n':
            nextstate = inp
        elif state != None and inp == '\n':
            nextstate = None
        else:
            nextstate = state
        return nextstate #,nextstate

# string = 'asdf #comment \n not'
# m = CommentsSM()
# m.transduce(string)#, verbose=True)

#HW2

from libdw import sm

class FirstWordSM(sm.SM):
    start_state = 1

    def get_next_values(self, state, inp):
        # print(state, inp)
        if state==1:
            if inp==" ":
                nextstate=0
                return nextstate,None
            else:
                nextstate=1
                return nextstate,inp
        elif state==0:
            if inp=="\n":
                nextstate=2
                return nextstate,None
            else:
                nextstate=0
                return nextstate,None
        elif state==2:
            if inp==" ":
                nextstate=2
                return nextstate,None
            elif inp=="\n":
                nextstate=2
                return nextstate,None
            else:
                nextstate=1
                return nextstate,inp



# inputstr = 'This is the \n newline here'
# m = FirstWordSM ()
# m.transduce(inputstr, verbose=True)

#Quiz
class Triangle:
    def __init__(self, color = 'green', filled = True, side1 = 1.0, side2 = 1.0 , side3 = 1.0):
        self.color = color
        self.filled = filled
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1+self.side2+self.side3)/2
        area = ( s*(s-self.side1)*(s-self.side2)*(s-self.side3) )**0.5
        return area

class Bee(sm.SM):
    start_state = 1
    def get_next_state(self, state, inp):
        if state == 1:
            if inp == 'a':
                nextstate = 2
            elif inp == 'b':
                nextstate = 1

        elif state == 2:
            if inp == 'a':
                nextstate = 2
            elif inp == 'b':
                nextstate = 1
        print('current state is: {}, input is: {}, next state is {}'.format(state, inp, nextstate))
        return nextstate

# b = Bee()
# b.start()
# b.step('a')
# b.step('a')
# b.step('b')
# b.step('a')
# b.step('a')