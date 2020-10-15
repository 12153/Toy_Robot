import unittest
import subprocess
import robot
import world
from io import StringIO
from unittest.mock import patch
from contextlib import redirect_stderr, redirect_stdout


class test_robot(unittest.TestCase):
    @patch("sys.stdin", StringIO("HAL\nforward 10\noff\n"))
    def test_1(self):
        world.random.randint = lambda a, b: 0

        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..
""", output)
        world.clean_global()
        world.clean_globals()

    @patch("sys.stdin", StringIO("HAL\nleft\nleft\nleft\nleft\nleft\nback 10\noff"))
    def test_2(self):
        world.random.randint = lambda a, b: 1
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
There are some obstacles:
- At position 1,1 (to 5,5)
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (10,0).
HAL: What must I do next? HAL: Shutting down..
""", output)

    @patch("sys.stdin", StringIO("HAL\nleft\nleft\nback 20\nreplay silent\noff\n"))
    def test_3(self):
        world.random.randint = lambda a, b: 0
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 20 steps.
 > HAL now at position (0,20).
HAL: What must I do next?  > HAL replayed 3 commands silently.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..
""", output)

    @patch("sys.stdin", StringIO("HAL\nsprint 5\nleft\nback 20\nreplay silent\noff\n"))
    def test_4(self):
        world.random.randint = lambda a, b: 0
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL moved forward by 4 steps.
 > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.
 > HAL moved forward by 1 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved back by 20 steps.
 > HAL now at position (20,15).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL moved forward by 4 steps.
 > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.
 > HAL replayed 3 commands silently.
 > HAL now at position (5,35).
HAL: What must I do next? HAL: Shutting down..
""", output)

    @patch("sys.stdin", StringIO("HAL\nsprint 5\nleft\nback 20\nhelp\noff\n"))
    def test_4(self):
        world.random.randint = lambda a, b: 0
        f = StringIO()
        with redirect_stdout(f):
            robot.robot_start()
        output = f.getvalue()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL moved forward by 4 steps.
 > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.
 > HAL moved forward by 1 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved back by 20 steps.
 > HAL now at position (20,15).
HAL: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]

 > HAL now at position (20,15).
HAL: What must I do next? HAL: Shutting down..
""", output)
