# A loop is used for iterating over a sequence.

people = ['John', 'Paul', 'Sara', 'Susan']

#simple for loop

#for person in people:
   # print(f'Current Person:{person}')

for person in people:
    if person == 'Sara':
        break
    print(f'Current Person:{person}')

for person in people:
    if person == 'Sara':
        continue
    print(f'Current Person:{person}')

for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number:{i}')

#while loops execute a set of statements as condition is true
count = 0
while count < 10:
    print(f'Count:{count}')
    count += 2

