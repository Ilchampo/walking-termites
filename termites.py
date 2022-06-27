#!/usr/bin/env python3

# Create the Termite and methods
# limits = (up, right, down, left)
from turtle import left

class Termite:
    # Max steps per termite 100
    def __init__(self, position=(0, 0), color="green", flag=false, steps=100, path = []):
        self.lastPosition = position,
        self.position = position,
        self.color = color,
        self.flag = flag
        self.steps = steps
        self.path = path

    def getPosition(self):
        return self.position

    def getColor(self):
        return self.color

    def moveUp(self, interval=1):
        self.position = (self.position[0], self.position[1] + interval)

    def moveDown(self, interval=1):
        self.position = (self.position[0], self.position[1] - interval)

    def moveRight(self, interval=1):
        self.position = (self.position[0] + interval, self.position[1])

    def moveLeft(self, interval=1):
        self.position = (self.position[0] - interval, self.position[1])

    def moveUpRight(self, interval=1):
        self.position = (self.position[0] +
                         interval, self.position[1] + interval)

    def moveUpLeft(self, interval=1):
        self.position = (self.position[0] -
                         interval, self.position[1] + interval)

    def moveDownRight(self, interval=1):
        self.position = (self.position[0] +
                         interval, self.position[1] - interval)

    def moveDownLeft(self, interval=1):
        self.position = (self.position[0] -
                         interval, self.position[1] - interval)

    def samePosition(newPosition, lastPosition):
        return (newPosition == lastPosition)

    def moveTermite(self, random, limits, interval=1):
        direction = random.randint(0, 8)
        # Move Up
        if direction == 0:
            if self.position[1] < limits[0] and not self.samePosition(self.moveUp(interval), self.position):
                self.moveUp(interval)
        # Move Up Right
        elif direction == 1:
            if self.position[0] < limits[1] and self.position[1] < limits[0] and not self.samePosition(self.moveUpRight(interval), self.lastPosition):
                self.moveUpRight(interval)
        # Move Right
        elif direction == 2:
            if self.position[0] < limits[1] and not self.samePosition(self.moveRight(interval), self.lastPosition):
                self.moveRight(interval)
        # Move Down Right
        elif direction == 3:
            if self.position[1] < limits[2] and self.position[0] < limits[1] and not self.samePosition(self.moveDownRight(interval), self.position):
                self.moveDownRight(interval)
        # Move Down
        elif direction == 4:
            if self.position[1] < limits[2] and not self.samePosition(self.moveDown(interval), self.position):
                self.moveDown(interval)
        # Move Down Left
        elif direction == 5:
            if self.position[1] < limits[2] and self.position[0] < limits[3] and not self.samePosition(self.moveDownLeft(interval), self.position):
                self.moveDownLeft(interval)
        # Move Left
        elif direction == 6:
            if self.position[0] < limits[3] and not self.samePosition(self.moveLeft(interval), self.lastPosition):
                self.moveLeft(interval)
        # Move Up Left
        elif direction == 7:
            if self.position[0] < limits[3] and self.position[1] < limits[0] and not self.samePosition(self.moveUpLeft(interval), self.lastPosition):
                self.moveUpLeft(interval)
        self.lastPosition=self.position
        self.steps=self.steps - 1
        self.path.append(self.position)

    def eatChip (self, Chip):
        if self.position == Chip.getPosition():
            self.flag = true
            Chip.setColor("blue")

class Chip:
    def __init__(self, index, position = (0, 0), color = "red"):
        self.index = index
        self.position = position
        self.color = color
    
    def getPosition(self):
        return self.position
    
    def getColor(self):
        return self.color

    def setColor(color):
        self.color = color