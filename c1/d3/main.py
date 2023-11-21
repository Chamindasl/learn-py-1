from turtle import color

empty_dict = {}

student = {
    'name': 'indika',
    'age': 20,
    'grade': 'A'
}


student['course'] = 'Python Programming'

del student['grade']

print(student)

print(student['name'])

if 'course' in student:
    print( 'is prasant')
else:
    print('not prasant')

# part 3
phone_numbers = {
    'Alice': '123-456-7890',
    'lice': '123-456-7891',
    'ice': '123-456-7892'
}
contact_name = 'Alice'
phone_number = phone_numbers.get(contact_name)
if phone_number in phone_numbers:
    print('is presant')
else:
    print('is not presant')


print(list(phone_numbers.keys()))

print(list(phone_numbers.values()))

print(list(phone_numbers.items()))

#Part 4

dict1 = {
    'color': 'red',
    'shape': 'circal',
    'size':'big'
}

dict2 = {
    'color': 'red',
    'shape': 'square',
    'size':'small'
}

print(dict1.update(dict2))
