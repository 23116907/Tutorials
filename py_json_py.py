import json

userJSON = '{"first_name":"Jack", "last_name":"Smith", "age":30}'

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'], user['last_name'], 'age', user['age'])

car = {'make': 'Ford', 'model':'Mustang', 'year':1970}

carJSON = json.dumps(car)

print(car['make'], car['model'], 'of', car['year'])