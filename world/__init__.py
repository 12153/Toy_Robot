import sys
from .text import *
if len(sys.argv) > 1:
    if sys.argv[1].lower() == 'turtle':
        from .turtle import *