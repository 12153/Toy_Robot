import sys
from .obstacles import *
from .maze_runner import *

if len(sys.argv) > 2:
    if sys.argv[2] == 'maze':
        from .maze_gen import *