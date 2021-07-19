# If/Else conditions are used to decide to do something based on something being true of false

x=11
y=20

if x>y:
    print(f'{x} is greater than {y}')

#if/else
if x>y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print (f'{y} is greater than {x}')


if x>2 and x <=10:
    print (f'{x} is greater than 2 and less than or eqaul to 10')

if x>2 or x <=10:
    print (f'{x} is greater than 2 and less than or eqaul to 10')

#not
if not (x == y):
    print(f'{x} is not equal to {y}')

numbers = [1,2,3,4,5]

if x in numbers:
    print(x in numbers)
elif x not in numbers:
    print(x in numbers)
