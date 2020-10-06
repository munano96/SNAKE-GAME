from config import Config
import random

class Snake():
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    HEAD = 0

    def __init__(self):
        self.x = random.randint(5, Config.CELLWIDTH -6)
        self.y = random.randint(5, Config.CELLHEIGHT -6)
        self.direction = self.RIGHT
        self.munanoCoords = [{'x': self.x,   'y': self.y},
                             {'x': self.x - 1, 'y': self.y},
                             {'x': self.x - 2, 'y': self.y}]

    def update(self, apple):
        if self.munanoCoords[self.HEAD]['x'] == apple.x and self.munanoCoords[self.HEAD]['y'] == apple.y:
            apple.setNewLocation()
        else:
            del self.munanoCoords[-1]
        if self.direction == self.UP:
           newHead = {'x': self.munanoCoords[self.HEAD]['x'],
                      'y': self.munanoCoords[self.HEAD]['y']
                           -1}

        elif self.direction == self.DOWN:
             newHead = {'x': self.munanoCoords[self.HEAD]['x'],
                      'y': self.munanoCoords[self.HEAD]['y']
                           +1}

        elif self.direction == self.LEFT:
             newHead ={'x': self.munanoCoords[self.HEAD]
                       ['x'] -1, 'y': self.munanoCoords[self.HEAD]['y']}

        elif  self.direction == self.RIGHT:
             newHead ={'x': self.munanoCoords[self.HEAD]
                       ['x'] +1, 'y': self.munanoCoords[self.HEAD]['y']}

        self.munanoCoords.insert(0, newHead)




