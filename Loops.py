

## While Loop

count = 0

while count < 5:
    print(str(count))
    count = count+1
else:
    print("No true "+ str(count))


## For Loop
    
numbers = [0, 1, 2, 3, 4, 5]

for num in numbers:
    print("List "+ str(num))


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for (key,value) in person.items():
    print("Key "+ key)
    print("Value "+ str(value))


for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)    