import boid
import numpy as np
import math
import tkinter
import random
import time


class Shoal:
    def __init__(self, size):
        self.bocal = 800
        self.size = size
        self.boids = [boid.Boid(self.bocal) for i in
                      range(0, self.size)]

        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=self.bocal, height=self.bocal, background='white')
        self.canvas.pack()

    def show(self):

        self.canvas.delete(tkinter.ALL)
        for boid in self.boids:
            boid.show(self.canvas)
        self.canvas.update()

    def update(self):

        for boid in self.boids:
            boid.flock(self.boids)
            boid.update()
