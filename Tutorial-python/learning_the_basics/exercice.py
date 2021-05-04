name = input('My name is: ')
age = input('My age is: ')

def user_data(name, age):
    return name + " "+ str(age)


print(user_data(name,age))


def calculate_decades (age): 
    return int(age/10)

print(calculate_decades(23))