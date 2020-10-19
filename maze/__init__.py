import sys
from .obstacles import *
from .maze_runner import *

args = [x.lower() for x in sys.argv]

if 'maze' in args:
    from .maze_gen import *
elif 'new' in args:
    from .new_maze import *