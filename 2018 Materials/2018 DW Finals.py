#3
def equity(f):
    total_rec = 0
    total_pay = 0
    net_equ = 0
    for k, v in f.items():
        total_rec += v[0]
        total_pay += v[1]
        net_equ += v[0] - v[1]
    return total_rec, total_pay, net_equ


# f1={'A': [100, 0], 'B': [100, 0], 'C': [100, 0]}
# f2={'M': [30, 20], 'N': [50, 70], 'O': [60, 80]}
# f3={'J': [0, 30], 'K': [0, 20], 'L': [0, 40]}

# print(equity(f1))
# print(equity(f2))
# print(equity(f3))

#2

def wordcount (s):
    output = []
    s_clean = s[:]
    for char in ':;,.-':
        print(char)
        s_clean.replace(char, ' ')
    line_split = s_clean.split('\n')
    print ('line_split: {}'.format(line_split))
    for line in line_split:
        d = {}
        count = 0
        str_split = line.split()
        print(str_split)
        



# print(wordcount('Tom Dick Harry'))
# print(wordcount("Hello world\nHello Hello"))
# print(wordcount ("Hello  hello")) 		 
# print(wordcount ("Hello  World")) 		 
# print(wordcount ("Hello, Hello World"))  
# print(wordcount ("Hello \nWorld")) 
# print(wordcount ("Hello \nWorld\n")) 		 
# print(wordcount ("Hello \n\nWorld")) 	
# print(wordcount ("asdasf \n \n \n\nasdasfd;; asfdasd\n Hello hello hello hello world world world"))
# print(wordcount ("Hello, world\nHello. Hello\n."))
 
#5

class Person:
    def __init__(self, name = 'Unknown', age = 0, contact_details = {'phone':'+65 0000 0000', 'email':'nobody@nowhere.com.sg'}):
        self._name = name
        self._age = age
        self._contact_details = contact_details

    def get_name(self):
        return self._name

    def set_name(self, inp):
        if type(inp) == str and len(inp)>=1:
            self._name = inp
        else:
            pass

    name = property(get_name, set_name)

    def get_age(self):
        return self._age

    def set_age(self, inp):
        if type(inp) == int and inp>=0:
            self._age = inp
        else:
            pass

    age = property(get_age, set_age)
    
    def get_contact(self):
        return self._contact_details

    def set_contact(self, inp):
        self._contact_details = inp

    contact_details = property(get_contact, set_contact)

    def get_email(self):
        return self._contact_details['email']

    def set_email(self, inp):
        try:
            at_count = len([x for x in inp if x == '@'])
            after_at = inp.split('@')[1]
            print(f'after@:===={after_at}')
            dot_count = len([x for x in after_at if x == '.'])
            strip_valid_chars = after_at.strip('._')
            print(strip_valid_chars)
        except:
            pass
        if at_count == 1:
            print('@ count pass')
            if dot_count >=1:
                print('. count pass')
                if strip_valid_chars.isalnum():
                    print('alnum pass')
                    self._contact_details['email'] = inp
        else:
            pass

    email = property(get_email, set_email)




# TEST CASES
#   please uncomment to use, and compare
#   the output against that in the printed paper

# Task A Test Code
    
# print('Task A:')
# p = Person()
# print(p.name, p.age)
# print(p.contact_details)

# d = {'phone': '+65 8888 8888', 'email': 'chicken@floss.com.sg'}
# p = Person('Charlie the Chicken', 88, d)
# print(p.name, p.age)
# print(p.contact_details)
    
# Task B Test Code
    
# print('Task B:')
# p = Person()
# p.name = ""
# print(p.name)

# p = Person()
# p.age = 88
# p.age = 'this is, in fact, a string'
# print(p.age)


# Task C Test Code
    
# print('Task C:')
# p = Person()
# print(p.email)
# print(p.email == p.contact_details['email'])

# p = Person()
# p.email = 'chicken@floss.com.sg'
# p.email = 'nasi.kukus'
# p.email = 'ayam.goreng@berempah'
# p.email = 'sedap!@makanan.com.sg'
# print(p.email)
    
#print() 



# Task D Test Code
    
#print('Task D:')
#p = Person()
#print(p.mother)
    
#p = Person()
#p.mother = 'Mary Poppins'
#print(p.mother)

#p = Person()
#p.mother = p
#print(p.mother)

#p = Person()
#q = Person('Charlie the Chicken', 88)
#p.mother = q
#print(p.mother.name)

#p = Person()
#q = Person('Charlie the Chicken', 88)
#r = Person('Alison', 22)
#s = Person('Eileen', 55)
#q.mother = r
#r.mother = s
#s.mother = p
#p.mother = q
#print(q.mother.name)
#print(r.mother.name)
#print(s.mother.name)
#print(p.mother)



