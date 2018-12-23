import wk2_template as a
from pythymiodw import *

mech=ThymioReal()
a.forward(mech,100,5)
print(mech.get_temperature())
mech.quit()
