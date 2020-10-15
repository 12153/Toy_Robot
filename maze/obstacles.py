import random
import maze

obstacle_list = []

def make_obstacles(r):
    global obstacle_list
    for _ in range(random.randint(1,10)):
        x = random.randint(-100, 100)
        y = random.randint(-200, 200)
        obstacle_list.append([x,y])
    obstacle_list = maze.get_obstacles()
    print(f'{r.name}: Loaded obstacles.')

def get_obstacles():
    global obstacle_list
    a = obstacle_list
    return a


def print_obstacles():
    if len(obstacle_list) > 0:
        print("There are some obstacles:")
        for i in obstacle_list:
            print(f'- At position {i[0]},{i[1]} (to {i[0]+4},{i[1]+4})')

def is_position_blocked(x, y):
    for obs in obstacle_list:
        if (obs[0] <= x <= obs[0]+4) and (obs[1] <= y <= obs[1]+4):
            return True
    return False

def is_path_blocked(x1, y1, x2, y2):
    for o in obstacle_list:
        if x1 == x2:
            if (y1 < o[1] < y2 or y1 > o[1] > y2) and o[0] <= x1 <= o[0] + 4:
                return True
        if y1 == y2:
            if (x1 < o[0] < x2 or x1 > o[0] > x2) and o[1] <= y1 <= o[1] + 4: 
                return True
    return False

