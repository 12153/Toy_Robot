import turtle
import maze
import world

a = turtle.Turtle()
screen = turtle.Screen()
s = 210
zz = 5
screen.setworldcoordinates(-s,-s,s,s)
# screen.tracer(0)
screen.delay(0)
a.speed(0)


class Node:
    def __init__(self, x, y, n):
        self.x, self.y = x, y
        self.visited = False
        self.path = n
        self.color = "blue"

    def draw(self):
        a.pu()
        a.color("black", self.color)
        a.goto(self.x, self.y)
        a.pd()
        a.begin_fill()
        for _ in range(4):
            a.fd(5)
            a.lt(90)
        a.end_fill()

coords = []
obstacles = []
def do_things():
    global coords, obstacles
    obstacles = maze.get_obstacles()
    for i in range(-200, 200+zz, zz):
        l = []
        for j in range(-100,100+zz, zz):
            if maze.is_position_blocked(j, i):
                l.append(Node(j, i, False))
            else:
                l.append(Node(j, i,True))
            # l.append(Node(j, i, True))
        coords.append(l)

    # print(len(coords))
    # for i in coords:
    #     for n in i:
    #         if n.path == False:
    #             print(n.path)
    # input()
    # for i in coords:
    #     for j in i:
    #         j.draw()
    # screen.tracer(1)

def get_n(node):
    for i, line in enumerate(coords):
        for j, n in enumerate(line):
            if n.x == node.x and n.y == node.y:
                x, y = j, i
                break

    up, right,down,left = [None]*4
    if x > 0 and node.x > coords[y][x-1].x:
        left = coords[y][x-1]
    if x < len(coords[0]) - 1:
        right = coords[y][x+1]
    if y > 0 and node.y > coords[y-1][x].y:
        down = coords[y-1][x]
    if y < len(coords) - 1:
        up = coords[y+1][x]
    return [up, right, down, left]

def add_to(tup, q):
    for i, n in enumerate(q):
        if n[0] < tup[0]:
            q = q[:i+1] +[tup]+ q[i:]
            break
    return q

def run(r, user_input):
    do_things()
    global coords

    print(f'{r.name}: starting mazerun..')

    while r.pos[1]%zz != 0:
        while r.direction != 3:
            world.turn(r, "left")
        world.move(r, f'forward {r.pos[1]%zz}')
    while r.pos[0]%zz != 0:
        while r.direction != 2:
            world.turn(r, "left")
        world.move(r, f'forward {r.pos[0]%zz}')
    for i in coords:
        for n in i:
            if (n.x == r.pos[1] and n.y == r.pos[0]):
                start = n
                break
    # start = coords[0][0]
    args = user_input.lower().split()

    if "bottom" in args:
        cond = lambda x: True if x.y > -200  else False
    elif "right" in args:
        cond = lambda x: True if x.x < 100  else False
    elif "left" in args:
        cond = lambda x: True if x.x > -100  else False
    else:
        cond = lambda x: True if x.y < 200  else False
    q = [start]
    node = start
    prev = {node:None for node in [x for i in coords for x in i]}
    while cond(node):
        node.visited = True
        if q:
            # node = q[0][1]
            node = q[0]
            q = q[1:]
        # node.color = "red"
        # node.draw()

        neighbours = get_n(node)
        neighbours = list(filter(lambda x: x != None, neighbours))
        neighbours = list(filter(lambda x: x.visited == False and x.path, neighbours))
        for n in neighbours:
            n.visited = True
            # q = add_to((abs(80 - n.x*2), n), q)
            q.append(n)
            prev[n] = node

    path = []
    e = node
    while e != start:
        path.append(e)
        e = prev[e]
    path.append(start)
    path = path[::-1]
    for n in coords:
        for i in n:
            i.visited = False

    # a = turtle.Turtle()
    # a.pu()
    # a.goto(start.x, start.y)
    # a.pd()
    # for n in path:
    #     print(n.x, n.y)
    #     n.color = "yellow"
        # n.draw()

    for n in path:
        if n.x > r.pos[1]:
            while r.direction != 1:
                world.turn(r, "right")
            world.move(r, f'forward {zz}')
        elif n.x < r.pos[1]:
            while r.direction != 3:
                world.turn(r, 'left')
            world.move(r, f'forward {zz}')
        elif n.y < r.pos[0]:
            while r.direction != 2:
                world.turn(r, 'right')
            world.move(r, f'forward {zz}')
        elif n.y > r.pos[0]:
            while r.direction != 0:
                world.turn(r, 'right')
            world.move(r, f'forward {zz}')
    # world.move(r, f'forward {zz}')

    return '', True
            



    