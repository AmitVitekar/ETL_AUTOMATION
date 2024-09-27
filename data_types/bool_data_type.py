a = True

print("type of a",type(a))
print("Value of a", a)
print("id of a", a)

# type of a <class 'bool'>
# Value of a True
# id of a True

print ("methodes of a", dir (a))

# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__',
#  '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__',
#  '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__',
#  '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__',
#  '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
#  '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator',
#  'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

b = False

print ("Adding a and b using '__add__' methodes :", a.__add__(b))

# Adding a and b using '__add__' methodes : 1

# True = 1
# False = 0
# so True + Flase = 1