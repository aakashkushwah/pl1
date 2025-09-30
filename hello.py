# sample comment

# side comment
print("Hello, World!");

is_ok = True
print("Is everything OK?", is_ok)
name = ('Aakash Kushwah ' 
         'is learning Python. '
            'He is enjoying it!')
if is_ok:
    print("All systems go!", name[-10:-2])

print(len(name))

fav_numbers = [0,1,2,3,10]
print(fav_numbers)
print(fav_numbers[2:4])
fav_numbers.append(69)
print(fav_numbers)
fav_numbers.remove(1)
print(fav_numbers)
print(fav_numbers.index(10))
fav_numbers.sort()
print(fav_numbers)
fav_numbers.reverse()
print(fav_numbers)

fav_num_str = str(fav_numbers)
print(fav_num_str+" is my favorite numbers.")
fav_num_str = fav_num_str.replace("[","").replace("]","")
print(fav_num_str+" is my favorite numbers.")
print(len(fav_num_str))
fav_numbers[:]=[]
print(fav_numbers)

a, b = 0, 1
while(a < 10):
    print(a, end=', ')
    a, b = b, a + b
print()

a, b = 0, 1
while(a < 10):
    print(a)     
    c = a + b
    a = b
    b = c
print()

name, age = 'Aakash Kushwah', 38
print(f'{name} is {age} years old.')

## taking inputs
# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
# print(f'The sum of {x} and {y} is {x + y}.')

# if x > y:
#     print(f'{x} is greater than {y}.')
# elif x < y:
#     print(f'{x} is less than {y}.')
# else:
#     print(f'{x} is equal to {y}.')
import time
bs = 1
while bs > 0:
    bs = bs -1
    time.sleep(1)
    print(bs)

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
for w in words:
    print(w, end=', ')
print()
print(', '.join(words))

# for i, w in enumerate(words):
#     print(w, end=' ')
# print()  # Ad
print('AK 1')
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太': 'active'}

dict_of_users = {}
dict_of_users[tuple(sorted(users.items()))] = True
print(dict_of_users)

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

for user in users.keys():
    print(user)

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

for user, status in active_users.items():
    print(user, status)

print()

for i in range(5):
    print(i)

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

b = 256
c = 56
print(b//c)

def fib(n):    # write Fibonacci series up to n
    pass
