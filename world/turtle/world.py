import turtle
import maze
robo = turtle.Turtle('turtle')
headings = [90, 0, 270, 180]
size = 210
screen = turtle.Screen()
screen.setworldcoordinates(-size, -size, size, size)
screen.tracer(0)

def draw_screen():
    a = turtle.Turtle()
    a.hideturtle()
    screen.tracer(0)
    a.pu()
    a.goto(-100, -200)
    a.pd()
    a.goto(100, -200)
    a.goto(100, 200)
    a.goto(-100, 200)
    a.goto(-100, -200)
    screen.tracer(1)


def draw_square(x, y):
    a = turtle.Turtle()
    a.hideturtle()
    screen.tracer(0)
    a.pu()
    a.goto(x, y)
    a.pd()
    a.seth(0)
    a.begin_fill()
    for _ in range(4):
        a.fd(4)
        a.lt(90)
    a.end_fill()
    screen.tracer(1)

def validate_pos(r, dist: int, user_input: str):
    """Validates the position of the robot """
    args = user_input.lower().split(' ', 1)
    new = r.pos[r.direction%2] + int(args[1])*(-1 if r.direction > 1 else 1)*(-1 if 'back' in args else 1)
    if r.direction%2 == 0:
        if (-200 <= new <= 200) == False:
            print(f"{r.name}: Sorry, I cannot go outside my safe zone.")
            return False
    else:
        if (-100 <= new <= 100) == False:
            print(f"{r.name}: Sorry, I cannot go outside my safe zone.")
            return False
    if r.direction%2 == 0:
        pos = maze.is_position_blocked(r.pos[1], new)
        path = maze.is_path_blocked(r.pos[1], r.pos[0], r.pos[1], new)
    else:
        pos = maze.is_position_blocked(new, r.pos[0])
        path = maze.is_path_blocked(r.pos[1], r.pos[0], new, r.pos[0])
    if pos or path:
        print(f"{r.name}: Sorry, I cannot go outside my safe zone.")
        return False
    return True

def sprint(r, user_input: str):
    args = user_input.lower().split(' ', 1)
    if len(args) == 1:
        return f"{r.name}: Sorry, I did not understand '{user_input}'.", True
    if args[1].isdigit() == False:
        return f"{r.name}: Sorry, I did not understand '{user_input}'.", True
    n = int(args[1])
    if validate_pos(r, (n*(n+1)//2), user_input):
        for i in range(-n, 0):
            cmd = f'forward {-i}'
            out = move(r, cmd)[0]
            print(out)
    robo.pu()
    robo.seth(headings[r.direction])
    robo.goto(r.pos[1], r.pos[0])
    return '', True


def move(r, user_input):
    """moves the robot backward or forward depending on user input
    ie. 'forward 20' will move the robot forward by 20 and
    'back 20' will move the robot back 20"""
    args = user_input.lower().split(' ', 1)
    d = ('back' if 'back' in args else 'forward')
    if len(args) == 1:
        return f"{r.name}: Sorry, I did not understand '{user_input}'", True
    if args[1].isdigit() == False:
        return f"{r.name}: Sorry, I did not understand '{user_input}'", True
    if validate_pos(r, int(args[1]), user_input):
        n = int(args[1])*(-1 if r.direction > 1 else 1)*(-1 if 'back' in args else 1)
        r.pos[r.direction%2] += n
        robo.pu()
        robo.seth(headings[r.direction])
        screen.tracer(1)
        robo.speed(1)
        robo.goto(r.pos[1], r.pos[0])
        return f' > {r.name} moved {d} by {args[1]} steps.', True
    else:
        return '', True

def off(r, user_input):
    """Turns off the robot..."""
    return f'{r.name}: Shutting down..', False

def turn(r, user_input):
    args = user_input.lower().split(' ', 1)
    n = (-1 if 'left'in args else 1)
    r.direction = (r.direction + n)%4
    d = ('left' if 'left' in args else 'right')
    robo.seth(headings[r.direction])
    return f' > {r.name} turned {d}.', True

def help_f(r, user_input):
    help_string="""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""
    return help_string, True

def show_position(r):
        return (f' > {r.name} now at position ({r.pos[1]},{r.pos[0]}).')

def replay(r, user_input):
    commands = {'off':off, 'help':help, 'forward': move, 'left':turn, 'right':turn, 'back':move,'sprint':sprint , 'replay':replay}
    options  = ["replay", "reversed", "silent"]
    arg = user_input.lower().split()
    silent = (True if 'silent' in arg else False)
    reverse = (True if 'reversed' in arg else False)
    h = r.history[::-1] if reverse else r.history
    new_args = list(filter(lambda x: x.isdigit() == False and '-' not in x, arg))
    for x in new_args:
        if x not in options:
            return f"{r.name}: Sorry, I did not understand '{user_input}'.", True
    ra = list(filter(lambda x: x.isdigit() or '-' in x, arg))
    if len(ra) == 1:
        ra = ra[0]
        if ra.isdigit():
            h = h[-int(ra):]
        else:
            ra = ra.split('-',1)
            r1, r2 = [x for x in ra]
            if r1.isdigit() and r2.isdigit():
                h = h[-int(r1): -int(r2)]
            else:
                return f"{r.name}: Sorry, I did not understand '{user_input}'.", True
    for i in h:
        user_input = cmd = i
        cmd = cmd.strip().lower().split()
        out = commands[cmd[0]](r, user_input)[0]
        if not silent:
            print(out)
            print(show_position(r))
    print(f' > HAL replayed {len(h)} commands'+(' in reverse' if reverse else '')+(' silently' if silent else '')+'.')
    return '', True

def set_up():
    screen.tracer(0)
    draw_screen()
    obs = maze.get_obstacles()
    for o in obs:
        draw_square(o[0], o[1])