import world
import maze

class Robot:
    def __init__(self, name):
        self.name = name
        self.pos = [0,0]
        self.direction = 0
        self.history = []

def get_name():
    name = ''
    while name == '':
        name = input("What do you want to name your robot? ")
    return name

def handle_command(r):
    commands = {'off':world.off, 'help':world.help_f, 'forward': world.move, 
    'left':world.turn, 'right':world.turn, 'back':world.move,
    'sprint':world.sprint, 'replay':world.replay}
    actions=["left","right","forward","back"]
    user_input = cmd = input(f"{r.name}: What must I do next? ")
    cmd = cmd.strip().lower().split()
    if cmd[0] not in commands:
        print(f"{r.name}: Sorry, I did not understand '{user_input}'.")
        return True
    if cmd[0] in actions:
        r.history += [user_input]
    (out, do_next) = commands[cmd[0]](r, user_input)
    if len(out) > 0:
        print(out)
    if cmd[0] in actions or cmd[0] == 'replay':
        print(world.show_position(r))
    return do_next

def robot_start():
    name = get_name()
    r = Robot(name)
    print(f'{name}: Hello kiddo!')

    maze.make_obstacles(r)
    maze.print_obstacles()
    world.set_up()
    maze.run()
    do_next = True
    while do_next:
        do_next = handle_command(r)

if __name__ == "__main__":
    robot_start()