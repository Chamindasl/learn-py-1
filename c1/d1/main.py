'''
qu-1
'''
print("----------p.1-----------")
name = 'Indika'
print(name)



'''
qu-2
'''
print("----------p.2-----------")
a = 2
b = 3
c = 4

print(a)
print(b)
print(c)

'''
qu-3
'''
print("----------p.3-----------")

favorite_color = 'orange'
print('My favorite color is '+ favorite_color)

'''
qu-4
'''
print("----------p.4-----------")

# camelCase
fullName = 'ssssssssssssssss'

# snake_case
full_name = 'ssssssssssssss'

# PascalCase
FullName = 'ssssssssssss'

print(fullName)
print(full_name)
print(FullName)



'''
qu-p.2/1
'''
print("----------5-----------")

def greet():
    name = 'Indika'

    return name

print(greet())


'''
qu-p.2/2
'''
print("----------6-----------")
def calculate_area():
    w = 3
    h = 2
    area = w * h
    return area
print(calculate_area())



def calculate_area1(w, h):
    area = w * h
    return area

print(calculate_area1(3,4))

'''
qu-p.2/7
'''
print("----------7-----------")


def is_even(num):
    if (num % 2 == 0):
        return True

    else:
        return False


print(is_even(34))
print(is_even(35))

'''
qu-p.2/9
'''
print("----------9-----------")
def concat_strings(my_first_name,my_last_name ):

    return my_first_name + ' '+ my_last_name

print('my name is '+ concat_strings('indika',' samanmalie'))

'''
qu-p.2/10
'''
print("----------10-----------")

def get_square_cube(num):
    square = num * num
    cube = square * num
    return square, cube

print(get_square_cube(3))
print(get_square_cube(4)[0])

s, c = get_square_cube(5)

print(s, c)








'''
qu-2
'''
print("----------3-----------")
print("----------3-----------")