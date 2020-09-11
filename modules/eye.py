# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 17:07:52 2020

@author: alber
"""
from math import sin, cos
from modules.vertice import Vertice

class Eye(Vertice):
    def __init__(self, x, y, z, alpha):
        super().__init__(x, y, z)
        self.alpha = alpha

    def forward(self):
        self.x=self.x-(1*cos(self.alpha))
        self.y=self.y-(1*sin(self.alpha))

    def backward(self):
        self.x=self.x+(1*cos(self.alpha))
        self.y=self.y+(1*sin(self.alpha))

    def right(self):
        self.x=self.x-(0.5*sin(self.alpha));
        self.y=self.y+(0.5*cos(self.alpha));

    def left(self):
        self.x=self.x+(0.5*sin(self.alpha));
        self.y=self.y-(0.5*cos(self.alpha));

    def turn_right(self):
        self.alpha = self.alpha-0.05

    def turn_left(self):
        self.alpha = self.alpha+0.05