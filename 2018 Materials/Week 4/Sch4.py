#Week 4

def linspace(start, stop, *args, **kwargs):
    incriment = (stop - start)
    if 'num' in kwargs:
        incriment /= kwargs['num']-1
    elif args == ():
        incriment/=49
    elif type(args[0]) == int:
        incriment/= args[0]-1
    else:
        incriment/=49

    l = []
    start = start
    while start<stop:
        l.append(round(start, 5))
        start +=incriment
    if l[-1] != stop:
        l.append(stop)
    return l

print(linspace(2.0, 3.0, 3))
print(linspace(1, 3.0, num = 5))
print(linspace(2.0, 3.0))
print(linspace(-1, 2, 5))

def meshgrid(x, y, z):
    xlen = len(x)
    ylen = len(y)
    zlen = len(z)
    xlist = [[[x[j] for i in range(zlen)] for j in range(xlen)] for k in range(ylen)]
    ylist = [[[y[k] for i in range(zlen)] for j in range(xlen)] for k in range(ylen)]
    zlist = [[[z[i] for i in range(zlen)] for j in range(xlen)] for k in range(ylen)]
    return xlist, ylist, zlist

x=[1,2,3]
y=[4,5,6,7]
z=[8,9]
print('test 1')
ans=meshgrid(x,y,z)
print(ans)

x=[0,0.5,1]
y=[2 ,2.5 ,3.0 ,3.5]
z=[4.0 ,4.5]
print('test 2')
ans=meshgrid(x,y,z)
print(ans)

([[[1.0 , 1.0], [2.0, 2.0], [3.0, 3.0]] , 
[[1.0 , 1.0], [2.0, 2.0],[3.0 , 3.0]] , 
[[1.0 , 1.0] , [2.0 , 2.0] , [3.0 , 3.0]] ,
[[1.0 , 1.0] ,[2.0 , 2.0] , [3.0 , 3.0]]] , 

[[[4.0 , 4.0] , [4.0 , 4.0] , [4.0 , 4.0]] ,
[[5.0 , 5.0], [5.0, 5.0], [5.0, 5.0]] , 
[[6.0 , 6.0], [6.0, 6.0],[6.0 , 6.0]] , 
[[7.0 , 7.0] , [7.0 , 7.0] , [7.0 , 7.0]]] , 

[[[8.0 , 9.0] ,[8.0 , 9.0] , [8.0 , 9.0]] , 
[[8.0 , 9.0] , [8.0 , 9.0] , [8.0 , 9.0]] ,
[[8.0 , 9.0], [8.0, 9.0], [8.0, 9.0]] , 
[[8.0 , 9.0], [8.0, 9.0],[8.0 , 9.0]]])


([[[0, 0], [0.5, 0.5], [1, 1]], 
[[0, 0], [0.5, 0.5], [1, 1]], 
[[0, 0], [0.5, 0.5], [1, 1]], 
[[0, 0], [0.5, 0.5], [1, 1]]], 

[[[2, 2], [2, 2], [2, 2]], 
[[2.5, 2.5], [2.5, 2.5], [2.5, 2.5]], 
[[3.0, 3.0], [3.0, 3.0], [3.0, 3.0]], 
[[3.5, 3.5], [3.5, 3.5], [3.5, 3.5]]], 

[[[4.0, 4.5], [4.0, 4.5], [4.0, 4.5]], 
[[4.0, 4.5], [4.0, 4.5], [4.0, 4.5]], 
[[4.0, 4.5], [4.0, 4.5], [4.0, 4.5]], 
[[4.0, 4.5], [4.0, 4.5], [4.0, 4.5]]])
