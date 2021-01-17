# Liste String iliskisi
text = 'ali topu at'

# print(text.split())
# print(text[2:6])

# Liste tanımlama String list Numeric list Dynamic list + Constructor
ints = [ 1, 2, 3 ] # integer list
floats = [ 1.0 , 3.4 , 46.5 ] # float list
texts = [ 'a' , 'asfasd', 'name' ] # String list

dynamicList = ['a' , 23, 1.0 , True] # Dynamic list

liste = list() # []
# print(liste)

# birlestirme
liste1 = [ 'a' , 'asfasd', 'name' ]
liste2 = [ 1.0 , 3 , 123 ]

val = liste1 + liste2 + liste1

# len
val = len(liste1)

# index
val = liste2[2]

# nested list

val = [liste1, liste2] # [ ['a' , 'asfasd', 'name'], [1.0 , 3 , 123] ]

# print(val)

# *********************************

# Metodlar
numbers = [ 1, 5, 3, 4, 2 ]
letters = [ 'a', 'c', 'e', 'd', 'b' ]

# min max
val1 = min(numbers)
val2 = min(letters)

val1 = max(numbers)
val2 = max(letters)

# index
val1 = numbers[-1]
val2 = letters[1:4]

# append
numbers.append(12)
letters.append('z')
val1 = numbers
val2 = letters

# insert
numbers.insert(2,3)
letters.insert(4,'c')
val1 = numbers
val2 = letters

# pop(index)
numbers.pop(-2)
val1 = numbers

# remove(value)
letters.remove('a')
val2 = letters

# sort
numbers.sort()
val1 = numbers

# reverse
letters.reverse()
val2 = letters

# count
val1 = numbers.count(3)
val2 = letters.count('C') # aynısından arar "c" => 2 , "C" => 0

# clear
val1 = numbers.clear
val2 = letters.clear # []

print(val1)
print(val2)