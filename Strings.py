name = 'Brad'
age=37

#Concatenate(insert variable into string)

print('Hello, my name is '+ name)

# string formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

#F-Strings
print(f'Hello, many name is {name} and I am {age}')

#String methods
s= 'hello world'

print(s.replace('world', 'everyone'))

sub = 'l'
print(s.count(sub))