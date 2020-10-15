import turtle
import random
import maze

a = turtle.Turtle()
screen = turtle.Screen()

a.speed(0)
screen.delay(0)
screen.tracer(0)

coords = []

class Node:
    def __init__(self, x, y, att):
        self.x, self.y = x, y
        self.visited = False
        self.path = att

    def draw(self):
        a.pu()
        a.color("red")
        a.goto(self.x, self.y)
        a.pd()
        a.begin_fill()
        a.circle(1)
        a.end_fill()


def create_nodes():
    global coords
    for i in range(-200, 200):
        l = []
        for j in range(-100, 100):
            if maze.is_position_blocked(j, i):
                l.append(Node(j, i, 0))
            else:
                l.append(Node(j, i, 1))
        coords.append(l)

def run_maze():
    visted_s = []
    node = coords[200][100]

    while 1:
        possible = []
        node.visited = True
        visted_s.append(node)
        node.draw()
        for i, l in enumerate(coords):
            for j, zz in enumerate(l):
                if zz == node:
                    x, y = j, i
        
        up, down, left, right = [None]*4
        if y > 0:
            down = coords[y-1][x]
            possible.append(down)
        if y < len(coords) - 1:
            up = coords[y+1][x]
            possible.append(up)
        if x > 0:
            left = coords[y][x-1]
            possible.append(left)
        if x < len(coords[0]) - 1:
            right = coords[y][x+1]
            possible.append(right)

        available = list(filter(lambda x: x.visited == False and x.path , possible))
        if len(available) == 0:
            if len(visted_s) > 1:
                visted_s = visted_s[:-1]
                node = visted_s[-1]
                visted_s = visted_s[:-1]
                continue
            continue

        n = random.choice(available)
        node.draw()
        node = n
        print(n.x, n.y ,"sdfasfa")

def run():
    create_nodes()
    run_maze()