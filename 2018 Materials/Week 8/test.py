class car():
    def update(self, param= None):
        if param == None:
            print('none')
        else:
            print('self')

c1 = car()
c1.update(param=1)