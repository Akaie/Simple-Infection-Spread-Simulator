import random, math

class droplet:
    def __init__(self, size, x, y, direction, shape, canvas, bigTimer, mediumTimer, smallTimer):
        self.size = size
        self.x = x
        self.y = y
        self.direction = direction
        self.shape = shape
        self.canvas = canvas
        self.maxTimer = random.randint(math.floor(bigTimer/2), bigTimer)
        self.timer = 0
        self.done = False
        if size == 1:
            self.maxTimer = random.randint(math.floor(mediumTimer/2), mediumTimer)
        if size == 2:
            self.maxTimer = random.randint(math.floor(smallTimer/2), smallTimer)
    def tickTimer(self, germs):
        if self.timer <= self.maxTimer:
            self.timer += 1
        else:
            self.done = True
            self.canvas.delete(self.shape)
            if self in germs:
                germs.remove(self)
    def move(self, vents, ac, germs):
        if not self.done:
            if self.x < 2:
                self.x = 2
                self.canvas.coords(self.shape, self.x-(2-self.size), self.y-(2-self.size), self.x+(2-self.size), self.y+(2-self.size))
            if self.x > 498:
                self.x = 498
                self.canvas.coords(self.shape, self.x-(2-self.size), self.y-(2-self.size), self.x+(2-self.size), self.y+(2-self.size))
            if self.y < 2:
                self.y = 2
                self.canvas.coords(self.shape, self.x-(2-self.size), self.y-(2-self.size), self.x+(2-self.size), self.y+(2-self.size))
            if self.y > 498:
                self.y = 498
                self.canvas.coords(self.shape, self.x-(2-self.size), self.y-(2-self.size), self.x+(2-self.size), self.y+(2-self.size))
            if not vents.get():
                self.direction = random.randint(0,360)
                xdelta = math.cos(self.direction)
                ydelta = math.sin(self.direction)
                if not ((xdelta < 0 and self.x > 2 + xdelta) or (xdelta > 0 and self.x < 498 + xdelta)):
                    xdelta = 0
                if not ((ydelta < 0 and self.y > 2 + ydelta) or (ydelta > 0 and self.y < 498 + ydelta)):
                    ydelta = 0
                self.x += xdelta*2
                self.y += ydelta*2
                self.canvas.move(self.shape, xdelta*2, ydelta*2)
            else:
                distance = math.sqrt((self.x - 0)**2 + (self.y - 0)**2)
                xmult = 1
                ymult = 1
                dx = 0 - self.x
                dy = 0 - self.y
                if self.x > 250 and self.y < 250:
                    distance = math.sqrt((self.x - 500)**2 + (self.y - 0)**2)
                    xmult = -1
                    ymult = -1
                    dx = 500 - self.x
                    dy = 0 - self.y
                elif self.x < 250 and self.y > 250:
                    distance = math.sqrt((self.x - 0)**2 + (self.y - 500)**2)
                    xmult = -1
                    ymult = -1
                    dx = 0 - self.x
                    dy = 500 - self.y
                elif self.x > 250 and self.y > 250:
                    distance = math.sqrt((self.x - 500)**2 + (self.y - 500)**2)
                    xmult = 1
                    ymult = 1
                    dx = 500 - self.x
                    dy = 500 - self.y
                angle = math.degrees(math.atan2(dy, dx))
                xdelta2 = math.cos(angle) * (100 / (distance))
                ydelta2 = math.sin(angle) * (100 / (distance))
                if (self.x + xdelta2 > 440 and self.y + ydelta2 > 440) or (self.x + xdelta2 < 60 and self.y + ydelta2 > 440) or (self.x + xdelta2 > 440 and self.y + ydelta2 < 60) or (self.x + xdelta2 < 60 and self.y + ydelta2 < 60):
                    if ac.get():
                        self.x = random.randint(200,300)
                        self.y = random.randint(200,300)
                        self.canvas.coords(self.shape, self.x-(2-self.size), self.y-(2-self.size), self.x+(2-self.size), self.y+(2-self.size))
                    else:
                        self.canvas.delete(self.shape)
                        if self in germs:
                            germs.remove(self)
                else:
                    if not ((xdelta2 < 0 and self.x > 2 + xdelta2) or (xdelta2 > 0 and self.x < 498 + xdelta2)):
                        xdelta2 = math.copysign(2, xdelta2)
                    if not ((ydelta2 < 0 and self.y > 2 + ydelta2) or (ydelta2 > 0 and self.y < 498 + ydelta2)):
                        ydelta2 = math.copysign(2, ydelta2)
                    self.x += xdelta2
                    self.y += ydelta2
                    self.canvas.move(self.shape, xdelta2, ydelta2)
    def absorbed(self, germs):
        germs.remove(self)
        self.canvas.delete(self.shape)