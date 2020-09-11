from modules.vertice import Vertice
from modules.edge import Edge
import numpy as np
import cv2

class Cube():
    def __init__(self):
        self.vertices = [Vertice(4, 14, 0)
                         , Vertice(5, 14, 0)
                         , Vertice(5, 15, 0)
                         , Vertice(4, 15, 0)
                         , Vertice(4, 14, 1)
                         , Vertice(5, 14, 1)
                         , Vertice(5, 15, 1)
                         , Vertice(4, 15, 1)]

        self.edges = [Edge(self.vertices[0], self.vertices[1]),
                      Edge(self.vertices[0], self.vertices[3]),
                      Edge(self.vertices[0], self.vertices[4]),
                      Edge(self.vertices[1], self.vertices[2]),
                      Edge(self.vertices[1], self.vertices[5]),
                      Edge(self.vertices[2], self.vertices[3]),
                      Edge(self.vertices[2], self.vertices[6]),
                      Edge(self.vertices[3], self.vertices[7]),
                      Edge(self.vertices[4], self.vertices[5]),
                      Edge(self.vertices[4], self.vertices[7]),
                      Edge(self.vertices[5], self.vertices[6]),
                      Edge(self.vertices[6], self.vertices[7])]


    def draw(self, eye:Vertice, image):

        for edge in self.edges:
            edge.draw(eye, image)


if __name__ == '__main__':
    cube = Cube()
    eye = Vertice(9,15,0.6)

    cube.draw(eye)