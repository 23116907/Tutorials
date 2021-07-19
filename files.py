# Python has functions for creating, reading, updating, and deleting files.

#Open a file
myFile = open('myfile.txt', 'w')

#Get some info
print('Name:',myFile.name)
print('Is Closed:',myFile.closed)
print('Opening Mode:',myFile.mode)

#Write to file
myFile.write('I love Python')
myFile.write('and Java')
myFile.close()

#Append to File
myFile = open('myfile.txt', 'a')
myFile.write("I also like PHP")

