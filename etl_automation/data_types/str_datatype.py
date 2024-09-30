str1 = 'Etl automation Testing'

print("type of str1 :", type(str1))

print("Apply capitalize Function :", str1.capitalize())
# Apply capitalize Function : Etl automation testing - start letter in Upper othere all in lower
print("Apply Tital Function :", str1.title())
# Apply Tital Function : Etl Automation Testing  ---it covert

str1 = 'Etl automation Testing "Straße"'

print("Apply lower Function :", str1.lower())
# Apply lower Function : etl automation testing "straße"

print("Apply case-fold Function :", str1.casefold())

# Apply case-fold Function : etl automation testing "strasse"

# count

str1 = 'Etl automation Testing'

print(str1.count('a', 1, 10))

# it show the how many times the is present in betwen 1 and 10 index
