# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 17:01:55 2020

@author: alber
"""
from modules.cube import Cube
from modules.eye import Eye
import cv2
import numpy as np

if __name__ == '__main__':
    cube = Cube()
    eye = Eye(9,15,0.6,0)


    while True:
        # cv2.imshow("lala", img)


        image = np.zeros((768, 1024, 3), np.uint8)
        cube.draw(eye, image)
        cv2.imshow('cube', image)

        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


        # The function waitKey waits for a key event infinitely (when delay<=0)
        k = chr(cv2.waitKey(0))
        if k == 'w':                       # toggle current image
            eye.forward()
        elif k == 's':
            eye.backward()
        elif k == 'a':
            eye.turn_left()
        elif k == 'd':
            eye.turn_right()
        elif k == 'z':
            eye.left()
        elif k == 'c':
            eye.right()
        elif k == 'q':  #escape key
            break


    cv2.destroyAllWindows()

