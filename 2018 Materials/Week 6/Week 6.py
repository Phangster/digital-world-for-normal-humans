#Q1
def reverse(string):
    new = ''
    n = len(string)
    while n > 0:
        new += string[n-1]
        n=n-1
    return new

# print(reverse('testing'))

#Q2
def check_password(password):
    if len(password) < 8:
        print('not long enough')
        return False
    elif password.isalnum()== False:
        print('not alnum')
        return False
    elif len(password.strip('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) < 2:
        return False
    else:
        return True

#print(check_password('0testte2'))


#Q3
def longest_common_prefix(string1, string2):
    final = ''
    n=0
    if len(string1)>len(string2):
        n=len(string2)
    else:
        n=len(string1)
    for i in range(n):
        if string1[i] == string2[i]:
            final+= string1[i]
        else:
            pass
    return final

# print(longest_common_prefix('distance', 'disin'))

#Q4
class Coordinate:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.cdi = (self.x**2+self.y**2)**0.5
        #print('coordinates set:',x,y, self.cdi)

def get_maxmin_mag(f):
    main = []
    pmax = None
    pmin = None
    for line in f:
        l = ((line.strip('\n')).split('\t'))
        a = Coordinate(l[0], l[1])
        main.append(a)
    pmax = [i for i in main if i.cdi ==max(x.cdi for x in main)][0]
    pmin = [i for i in main if i.cdi ==min(x.cdi for x in main)][0]
    return pmax, pmin

# f = open('xy.dat', 'r')
# print(get_maxmin_mag(f))

#HW1
def binary_to_decimal(binstr):
    digit = 0
    for i in binstr:
        digit = digit*2 +int(i)
    return digit

#HW2
def uncompressed(string):
    l = [l for l in string]
    final = ''
    for num, i in enumerate(l):
        try:
            l[num] = int(i)
            final += l[num]*l[num+1]
        except:
            pass

    #print(l)
    return final

#print(uncompressed('1a2b3c'))

#HW3
def get_base_counts2(dna):
    print(dna)
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    no_lower = ''.join([i for i in dna if i.isupper()])
    no_num = ''.join([i for i in dna if i.isalpha()])
    print(no_lower)
    if no_lower.isalpha() != True:
        return 'The input DNA string is invalid'
    elif len(no_num) != len(no_lower):
        return 'The input DNA string is invalid'
    for char in no_lower:
        if char == 'A':
            d['A']+=1
        elif char == 'T':
            d['T']+=1
        elif char == 'C':
            d['C']+=1
        elif char == 'G':
            d['G']+=1
        # else:
        #     return 'The input DNA string is invalid'
    return d

#print(get_base_counts2('CcCCCCGGT'))

#HW4
f = open('constants.txt', 'r')
def get_fundamental_constants(f):
    d = {}
    for line in f:
        l = line.strip(' ').split()
        try: 
            k, v = l[0], l[1]
            d[k] = v
            # print(k,v)
        except:
            pass
    d.pop('name', None)
    d = {k:float(v) for k,v in d.items()}
    return d

# print(get_fundamental_constants(f))

#HW5
f = open('scores.txt', 'r')
def process_scores(f):
    l = []
    for line in f:
        l = line.strip('\n\r').split(' ')
    l = [float(i) for i in l]
    return sum(l), sum(l)/len(l)

print(process_scores(f))