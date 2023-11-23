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
    print('is prasant')
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

# Part 4

dict1 = {
    'color': 'red',
    'shape': 'circal',
    'size': 'big'
}

dict2 = {
    'color': 'red',
    'shape': 'square',
    'size': 'small'
}

print(dict1.update(dict2))

school = {
    'students': ['indika', 'ashvin', 'sethu'],
    'teachers': ['mr.hart', 'ms.costalo', 'ms.gavi']
}
print(school)

school['students'].append('chaminda')

print(school)

school['teachers'][0] = 'mr.barry'

print(school)

school['teachers'] = 'mr.barry'

print(school)

#part 2


enter_course = input('enter the course name:')
enter_duration = input('enter the course duration: ')

course_info = {
    'course': enter_course,
    'duration': enter_duration
}

print(course_info)

enter_name = input('enter the name:')
enter_phone_number = input('enter the phone number:')


phone_numbers = {
    'name': enter_name,
    'number': enter_phone_number
}
print(phone_numbers)

course_name = input("Enter a course name: ")
new_duration = int(input("Enter the updated duration: "))

friend_name = input('enter friend name:')
friend_age = input('enter friend age:')
friends_info = {
    'f_n': friend_name,
    'f_a': friend_age
}
print(friends_info)

friends_remove = input('enter the remove name:')

if friends_remove in friends_info:
    del friends_info[friends_remove]
    print(friends_remove +'is remove')
else:
    print('not found')


countries_info = {
    'srilanka': 'colombo',
    'India': 'mobai',
    'france': 'paris',
}
country_remove = input('enter country name')

if country_remove in countries_info:
    del countries_info[country_remove]
    print(country_remove)
else:
    print('not found')