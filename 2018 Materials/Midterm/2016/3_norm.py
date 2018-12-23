import cmath

def norm(z1, z2, z3):
	z1_conj = z1.conjugate()
	z2_conj = z2.conjugate()
	z3_conj = z3.conjugate()

	norm = cmath.sqrt(z1 * z1_conj + z2 * z2_conj + z3 * z3_conj).real
	return round(norm, 3)

# Test cases
print 'test 1'
z1=1+3j
z2=-1+3j
z3=-1-3j
ans=norm(z1,z2,z3)
print ans

print 'test 2'
z1=1+2j
z2=-1+2j
z3=-1-2j
ans=norm(z1,z2,z3)
print ans

print 'test 3'
z1=1+1j
z2=-1+1j
z3=-1-1j
ans=norm(z1,z2,z3)
print ans
