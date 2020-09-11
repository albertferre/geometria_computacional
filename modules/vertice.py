# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:59:56 2020

@author: alber
"""

from math import pi, sin, cos
from modules.pixel import Pixel

class Vertice():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def projection_transform(self, eye) -> Pixel:

        alpha = eye.alpha
        d=(eye.x*cos(alpha)) + (eye.y*sin(alpha)) + (0.5)
        lambd=(d-((cos(alpha)*eye.x)+(sin(alpha)*eye.y)))/((cos(alpha)*(self.x-eye.x))+(sin(alpha)*(self.y-eye.y)))

        p1 = eye.x + (lambd*(self.x-eye.x))
        p2 = eye.y + (lambd*(self.y-eye.y))
        p3 = eye.z + (lambd*(self.z-eye.z))

        p3 = p3 - eye.z + 0.1

        p1 = p1 - eye.x - (0.5*cos(alpha))
        p2 = p2 - eye.y - (0.5*sin(alpha))
        p2 = (sin(pi-alpha)*p1) + (cos(pi-alpha)*p2)

        p2 = p2 + 0.14

        # Resolució pantalla -> 640 x 480 pixels
        # Dimensions de la pantalla -> 0.28 x 0.2 metres

        x = p2 * 320 / 0.14
        y = p3 * 240 / 0.1

        y = 480 - y

        # b.x=x1;
        # b.y=y1;
        # b.lambda=lambda
        return Pixel(x, y, lambd)

