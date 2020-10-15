import world
import unittest
from io import StringIO


class test_world(unittest.TestCase):
    def test_1(self):
        x = world.do_forward("HAL", 20)[1]
        self.assertEqual(x, " > HAL moved forward by 20 steps.")

    def test_2(self):
        x = world.do_back("HAL", 20)[1]
        self.assertEqual(x, " > HAL moved back by 20 steps.")

    def test_3(self):
        x = world.do_back("HAL", 10)[1]
        self.assertEqual(x, " > HAL moved back by 10 steps.")

    def test_4(self):
        x = world.do_left_turn("HAL")[1]
        self.assertEqual(x, " > HAL turned left.")
        
    def test_5(self):
        x = world.do_right_turn("HAL")[1]
        self.assertEqual(x, " > HAL turned right.")

    def test_6(self):
        x = world.do_forward("HAL", 20)[1]
        x += world.do_forward("HAL", 30)[1]
        self.assertEqual(x, " > HAL moved forward by 20 steps. > HAL moved forward by 30 steps.")