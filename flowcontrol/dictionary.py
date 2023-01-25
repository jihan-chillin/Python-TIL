person = {'name' : 'jihan', 'address' : 'shinchon', 'interest' : 'coding'}
print(person['name'])

for key in person:
    print(key, person[key])
    
    
persons = [
    {'name' : 'jihan', 'address' : 'shinchon', 'interest' : 'coding'},
    {'name' : 'jihan22', 'address' : 'seoul', 'interest' : 'coffee'},
    {'name' : 'jihan33', 'address' : 'changcheon', 'interest' : 'studying'}
]


print('========== persons ===========')

for person in persons:
    for key in person:
        print(key, ': ', person[key])
        print('---------------------')
