####        Password Generator      ####

import random
def password(length):
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_0123456789'
    password = ''
    for _ in range(length):
        password = password + char[random.randint(0, len(char)-1)]
    
    return password

p1 = password(10)
print(p1)

p2 = password(50)
print(p2)


