import numpy as np
import math
import tkinter
import random
import time


class Boid:

    def __init__(self, bocal):
        self.bocal = bocal
        self.avoidPercep = 100
        self.alignPercep = 100
        self.cohesionPercep = 300
        self.radius = 5

        self.position = np.random.rand(2) * self.bocal
        self.maxSpeed = 7
        self.maxAcc = 3
        self.maxForce = 3
        self.speed = setMag(np.random.rand(2) - 0.5, self.maxSpeed * 2)
        self.acc = setMag(np.random.rand(2) - 0.5, self.maxAcc * 2)

    def update(self):

        self.position += self.speed

        self.speed += self.acc
        if np.linalg.norm(self.speed) > self.maxSpeed:
            self.speed = setMag(self.speed, self.maxSpeed)

        self.acc = np.zeros(2)

        self.edges()

    def edges(self):

        if self.position[0] > self.bocal:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = self.bocal
        if self.position[1] > self.bocal:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = self.bocal

    def show(self, canvas):

        canvas.create_oval(self.position[0] - self.radius, self.position[1] - self.radius,
                           self.position[0] + self.radius, self.position[1] + self.radius, fill="blue")

    def align(self, boids):
        total = 0
        steering = np.zeros(2)
        for other in boids:
            if other != self and self.dist(other) < self.alignPercep:
                steering += other.speed
                total += 1

        if total != 0:
            steering /= total
            steering = setMag(steering, self.maxSpeed)
            steering -= self.speed
            if np.linalg.norm(steering) > self.maxForce:
                steering = setMag(steering, self.maxForce)
        return steering

    def cohesion(self, boids):
        return ()

    def avoid(self, boids):
        return ()

    def flock(self, boids):
        self.acc += self.align(boids)

        if np.linalg.norm(self.acc) > self.maxAcc:
            self.acc = setMag(self.acc, self.maxAcc)

    def dist(self, other):
        return np.sqrt((self.position[0] - other.position[0]) ** 2 + (self.position[1] - other.position[1]) ** 2)


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    else:
        return v / norm


def setMag(v, newMag):
    return newMag * normalize(v)
