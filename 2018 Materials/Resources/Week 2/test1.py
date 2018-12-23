from pythymiodw import*
import wk2_template as a


mech=ThymioReal()
for i in range (4):
    a.forward(mech,100,3)
    mech.wheels(0,0)
    a.right(mech)
mech.quit()
