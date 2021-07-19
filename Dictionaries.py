person = {
    'first_name':'John',
    'last_name':'Smith',
    'age': 30
}
#Use Constructor
#person2= dict(first_name='Sara', last_name='Williams')

#Get Value
print(person['first_name'], person['last_name'], person['age'])
print(person.get('last_name'))

#print(person2, type(person2))

#add key/value
person['phone'] = '555'

print(person.items())

#Copy dict

person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

#Remove Item

del(person['age'])
person.pop('phone')

#Clear
person.clear()

print(len(person2))

person.clear()

people = [
    {'name': 'Martha', 'age':30},
    {'name': 'Kevin', 'age':35}
]

print(people[1]['name'])

print(person)