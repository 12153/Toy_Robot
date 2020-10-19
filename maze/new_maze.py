import random
import turtle

# a = turtle.Turtle()
# screen = turtle.Screen()
# a.speed(0)
# screen.delay(0)
# screen.tracer(0)

class node:
    def __init__(self, x, y):
        self.x       = x
        self.y       = y
        self.visited = False
        self.color   = "blue"
        self.walls   = [True]*4

    # def draw(self):
    #     a.pu()
    #     a.goto(self.x, self.y)
    #     a.color("black", 'cyan')
        # a.begin_fill()
        # for i in range(4):
        #     if self.walls[i]:
        #         a.pd()
        #     a.fd(20)
        #     a.rt(90)
        #     a.pu()
        # a.end_fill()

class maze:
    def __init__(self, h, w):
        self.h      = h
        self.w      = w
        self.maze   = []

    def gen_maze(self):
        for i in range(-200, 200, 20):
            l = []
            for j in range(-100, 100, 20):
                l.append(node(j, i+20))
            self.maze.append(l)
        # for i in self.maze:
        #     for n in i:
        #         n.draw()

    def unvisited(self):
        for line in self.maze:
            for n in line:
                if n.visited == False:
                    return True
        return False

    def make_maze(self):
        to_visit = []
        node = self.maze[0][5]
        while self.unvisited():
            neighbours = []

            if to_visit:
                node = random.choice(to_visit)
                to_visit.remove(node)

            # node.color = "cyan"            
            # node.draw()

            for i, l in enumerate(self.maze):
                for j, zz in enumerate(l):
                    if zz == node:
                        x, y = j, i

            up, down, left, right = [None]*4
            if y > 0:
                down = self.maze[y-1][x]
                neighbours.append(down)
            if y < self.h - 1:
                up = self.maze[y+1][x]
                neighbours.append(up)
            if x > 0:
                left = self.maze[y][x-1]
                neighbours.append(left)
            if x < self.w - 1:
                right = self.maze[y][x+1]
                neighbours.append(right)


            available = list(filter(lambda x: x, neighbours))
            for n in available:
                # n.draw()
                if n not in to_visit and n.visited == False:
                    to_visit.append(n)
                    n.visited = True
                    if n == up:
                        node.walls[0] = False
                        n.walls[2] = False
                    if n == down:
                        node.walls[2] = False
                        n.walls[0] = False
                    if n == left:
                        node.walls[3] = False
                        n.walls[1] = False
                    if n == right:
                        node.walls[1] = False
                        n.walls[3] = False

            # node.color = "blue"
            # node.draw()


    def creat_obstacles(self):
        obstacle_list = []
        win_blocks = []
        for line in self.maze:
            for n in line:
                if n.walls[0] == True:
                    for i in range(0,20,4):
                        obstacle_list += [(n.x+i, n.y)]
                if n.walls[1] == True:
                    obstacle_list += [(n.x+18, n.y-20)]
                    for i in range(0,20,4):
                        obstacle_list += [(n.x+18, n.y-i)]
                if n.walls[2] == True:
                    for i in range(0,20,4):
                        obstacle_list += [(n.x+i, n.y-20)]
                if n.walls[3] == True:
                    obstacle_list += [(n.x-2, n.y-20)]
                    for i in range(0,20,4):
                        obstacle_list += [(n.x-2, n.y-i)]
                        
        obstacle_list = list(set(obstacle_list))
        for obs in obstacle_list:
            if obs[1] == 200 or obs[0] == 98 or obs[1] == -200 or obs[0] == -102:
                win_blocks += [obs]
            if (-5 <= obs[1] <= 5) and (-5 <= obs[0] <= 5):
                win_blocks += [obs]
        obs_list = list(filter(lambda x: x not in win_blocks, obstacle_list))
        for obs in obs_list:
            if obs[1] == -196:
                obs_list += [[obs[0], -200]]
        return obs_list

m = maze(20, 10)
m.gen_maze()
m.make_maze()
obs = m.creat_obstacles()

def get_obstacles():
    o = obs
    return o


if __name__ == "__main__":    
    get_obstacles()