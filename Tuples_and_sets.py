#Create Tuple
fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

fruits2 = ('Apples', )

print(fruits[1])

#Can't change values
#fruits[0] = 'Pears'

del fruits2

#print(fruits2)

print(len(fruits))

#print(fruits2, type(fruits2))

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set

print('Apples' in fruits_set)
# Prints true as a result

fruits_set.add('Grape')

#fruits_set.remove('Grape')

#Clear set
#ffruits_set.clear()

#del fruits_set
#results in error that its not defined

fruits_set.add('Apples')

print(fruits_set)


