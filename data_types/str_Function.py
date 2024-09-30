str1 = 'a b c d e f g f i'

print(str1.split())

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'f', 'i'] by default it consider ' ' is a separator

s = 'a-b-c-d-e-f-g'

print("split the string by using separator :", s.split(sep='-'))

# split the string by using separator : ['a', 'b', 'c', 'd', 'e', 'f', 'g']

s = '    ETL Automation   '

print("Length of string be-four strip :", len(s))

# Length of string be-four strip : 21

s1 = s.strip()
print(s1)

# ETL Automation
print("Length of string after strip :", len(s1))
# Length of string after strip : 14

print('*' * 40)

print('split is used for to remove leading and ending white space from the string as well as we can provided the '
      'specific string value')

str1 = '  123ETL  123Automation123'

print(str1.strip('123'))

#   123ETL  123Automation

str1 = '123ETL  123Automation123'

print(str1.strip('123'))

# ETL  123Automation

print('*' * 100)

print("'rstrip()': this function is used to remove white space of any specific value from right side ")

print('lstrip() : this function is used to remove white space of any specific value from left side ')

str1 = '123ETL  123Automation123'

print(str1.rstrip('123'))

# 123ETL  123Automation
print(str1.lstrip('123'))

# ETL  123Automation123

print('*' * 100)

# how to conver list data into string data type
# join function is used to convert list datainto string data

# separator.join('variable')

a = ['col1', 'col2', 'col3', 'col4', 'col5']

print("value of variable a is :", a)
print("Type of variable a is :", type(a))

# value of variable 'a' is : ['col1', 'col2', 'col3', 'col4', 'col5']
# Type of variable 'a' is : <class 'list'>

a1 = ','.join(a)

print("value of variable a is :", a1)
print("Type of variable a is :", type(a1))

# value of variable a1 is : col1,col2,col3,col4,col5
# Type of variable a1 is : <class 'str'>
print('*' * 100)

# format Function

column = ['col1', 'col2', 'col3', 'col4', 'col5']

coln = ','.join(column)

sql = 'select {colun} from tablename'.format(colun=column)

print(sql)

# select col1,col2,col3,col4,col5 from tablename