# coding: utf-8

import random
import rhinoscriptsyntax as rs
from box import Box

num_x = 10
num_y = 10

rs.EnableRedraw(False)

for x in range(num_x):
    for y in range(num_y):
        origin = [x * 1000, y * 1000, 0]
        width = random.randint(100, 900)
        depth = random.randint(100, 900)
        height = random.randint(100, 900)

        obj = Box(origin, width, depth, height)
        obj.draw_box()
        obj.draw_info()

rs.EnableRedraw(True)
