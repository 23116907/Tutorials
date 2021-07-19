# A function is a block of code which only runs when it is called. No curly brackets


# Create function
def sayHello(name='Sam'):
    print(f'Hello {name}')

sayHello()

def getSum(num1, num2):
    total = num1+num2
    return total
print(getSum(3, 4))

#Lambda function is a small anonymous function.

getSum = lambda num1, num2 : num1 + num2

print (getSum(10, 3))