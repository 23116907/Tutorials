# Create List
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Use a constructor

numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

#Get a Value
print(fruits[3])

#Get Length
print(len(fruits))

#Append to list
fruits.append('Mangos')

fruits.remove('Grapes')

#Insert into position
fruits.insert(2, 'Bananas')

#Change Value
fruits[0] = 'Blueberries'

#Remove with pop
fruits.pop(2)

fruits.reverse()

#Sort list
fruits.sort(reverse=True)

print(fruits)