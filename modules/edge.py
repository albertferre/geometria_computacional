# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:46:27 2020

@author: alber
"""
from modules.vertice import Vertice
import cv2

class Edge():
    def __init__(self, vertice1, vertice2):
        self.vertice1 = vertice1
        self.vertice2 = vertice2

    def draw(self,eye:Vertice, image):
        COLOR = (255, 255, 255)
        LINE_WIDTH = 1


        p1 = self.vertice1.projection_transform(eye)
        p2 = self.vertice2.projection_transform(eye)

        (x1, y1) = (int(p1.x), int(p1.y))
        (x2, y2) = (int(p2.x), int(p2.y))
        cv2.line(image, (x1, y1) , (x2, y2), COLOR,LINE_WIDTH)





if __name__ == '__main__':
    vertice1 = Vertice(4,14,0)
    vertice2 = Vertice(5,14,0)
    eye = Vertice(9,15,0)

    edge = Edge(vertice1, vertice2)



    edge.draw_line(eye)


    # vertice2.projection_transform(eye).x
    # vertice2.projection_transform(eye).y