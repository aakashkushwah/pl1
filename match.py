import time


tup = (3,3)

match tup:
    case (0, 0):
        print('origin')
    case (1, x):
        print(f'1, {x}')
    case (y, 2):
        print(f'{y}, 1')
    case (x, y):
        print(f'{x}, {y}')
    case _:
        raise ValueError('Not a valid point')
    

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

def where_is(point: Point) -> str:
    match point:
        case Point(x=0, y=0):
            return 'origin'
        case Point(x=0, y=y):
            return f'y={y}'
        case Point(x=x, y=0):
            return f'x={x}'
        case Point(x=x, y=y) if x == y:
            return f'y=x'
        case Point():
            return 'somewhere else'
        case _:
            return 'not a point'

print(where_is(Point(x=1, y=2)))
print(where_is(Point(x=0, y=2)))
print(where_is(Point(x=2, y=0)))
print(where_is(Point(x=2, y=2)))

second_per_min = 60
def start_break_msgs(mins: int = 0.1):
    """This prints a message every second for 
    the number of minutes specified."""    
    second_per_min = 45
    n = mins * second_per_min     
    while n > 0:
        time.sleep(1)
        n -= 1
        print(f'{n} seconds remaining')

# start_break_msgs(0.1)
print(second_per_min) 
foo = start_break_msgs
# foo() 
print(foo)# 60, not 45

def f(a, L=[]):
    L.append(a)
    return L

print(f(1)) # [1]
print(f(2)) # [1, 2]
print(f(3)) # [1, 2, 3]
print(f(4, [])) # [4]
print(f(5)) # [1, 2, 3, 5]

def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f1(1)) # [1]
print(f1(2)) # [2]