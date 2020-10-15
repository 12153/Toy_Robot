import unittest
import world
import robot
from io import StringIO
from unittest.mock import patch
from contextlib import redirect_stderr, redirect_stdout


class test_obs(unittest.TestCase):
    def test_1(self):
        world.random.randint = lambda a, b: 1
        world.create_obstacles()

        self.assertEqual(world.get_obstacles(), [[1, 1]])
        world.clean_global()
        world.clean_globals()

    def test_2(self):
        world.random.randint = lambda a, b: 7
        world.create_obstacles()

        self.assertEqual(len(world.get_obstacles()), 7)
        world.clean_global()
        world.clean_globals()

    def test_3(self):
        for i in range(4):
            world.random.randint = lambda a, b: (1 if b == 10 else i)
            world.create_obstacles()

        self.assertEqual(world.get_obstacles(), [
                         [0, 0], [1, 1], [2, 2], [3, 3]])
        world.clean_global()
        world.clean_globals()

    @patch("sys.stdin", StringIO("HAL\nforward 11\nright\nforward 11\noff"))
    def test_4(self):
        f = StringIO()
        with redirect_stdout(f):
            world.random.randint = lambda a, b: (1 if b == 10 else 10)
            robot.robot_start()
        output = f.getvalue()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
There are some obstacles:
- At position 10,10 (to 14,14)
HAL: What must I do next?  > HAL moved forward by 11 steps.
 > HAL now at position (0,11).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,11).
HAL: What must I do next? Sorry, there is an obstacle in the way.
 > HAL now at position (0,11).
HAL: What must I do next? HAL: Shutting down..
""", output)
        world.clean_global()
        world.clean_globals()


if __name__ == '__main__':
    unittest.main()
