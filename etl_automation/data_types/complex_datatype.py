d = 2j + 1

print("id of d", id (d))
print('value of d', d)
print('type of d', type(d))

# id of d 2295027046704
# value of d (1+2j)
# type of d <class 'complex'>

print ("Metodes of d", dir(d))

# ['__abs__', '__add__', '__bool__', '__class__', '__complex__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
#  '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__',
#  '__rpow__', '__rsub__',
#  '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'conjugate', 'imag', 'real']

print ("Real value of d", d.real)

# Real value of d 1.0

print("Imagenary value of d", d.imag)

# Imagenary value of d 2.0