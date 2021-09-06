import random, math, dropletClass

class person:
    def __init__(self, x, y, shape, canvas):
        self.x = x
        self.y = y
        self.shape = shape
        self.canvas = canvas
        self.infected = False
        self.cured = False
        self.infectedTimer = -1
        self.cureTimer = -1
        self.immunityTimer = -1
        self.directionTimer = 0
        self.direction = random.randint(0,359)
    def startInfection(self):
        self.infected = True
        self.infectedTimer = 0
        self.cureTimer = 0
        self.canvas.itemconfig(self.shape, fill="red")
    def tickCuredTimer(self, stats, recoveryLength, rein): 
        if self.cureTimer == -1:
            pass
        else:
            if self.cureTimer >= recoveryLength:
                stats[1] += 1
                stats[2] -= 1
                self.cured = True
                self.infected = False
                self.cureTimer = -1
                self.infectedTimer = -1
                self.canvas.itemconfig(self.shape, fill="blue")
                if rein.get():
                    self.immunityTimer = 0
            else:
                self.cureTimer += 1
    def tickImmunityTimer(self, immunityLength):
        if self.immunityTimer == -1:
            pass
        else:
            if self.immunityTimer >= immunityLength:
                self.cured = False
                self.canvas.itemconfig(self.shape, fill="black")
                self.immunityTimer = -1
            else:
                self.immunityTimer += 1
    def tickInfectedTimer(self, sneezeTimer, germs, bigDistance, mediumDistance, smallDistance, sideSneeze, bigNumber, mediumNumber, smallNumber, bigTimer, mediumTimer, smallTimer):
        if self.infectedTimer == -1:
            pass
        else:
            if self.infectedTimer > random.randint(math.floor(sneezeTimer/2), sneezeTimer):
                self.spew(germs, bigDistance, mediumDistance, smallDistance, sideSneeze, bigNumber, mediumNumber, smallNumber, bigTimer, mediumTimer, smallTimer)
                self.infectedTimer = 0
            else:
                self.infectedTimer += 1
    def spew(self, germs, bigDistance, mediumDistance, smallDistance, sideSneeze, bigNumber, mediumNumber, smallNumber, bigTimer, mediumTimer, smallTimer):
        bigdrops = random.randint(0,bigNumber)
        mediumdrops = random.randint(0,mediumNumber)
        smalldrops = random.randint(0, smallNumber)
        direct = self.direction
        if sideSneeze:
            direct += 90
            if direct > 360:
                direct -= 360
        xdelta = math.cos(direct)
        ydelta = math.sin(direct)
        for d in range(0, bigdrops):
            x = self.x+xdelta*random.randint(0,bigDistance)
            y = self.y+ydelta*random.randint(0,bigDistance)
            oval = self.canvas.create_oval(x-2,y-2,x+2,y+2,fill="yellow")
            germs.append(dropletClass.droplet(0, x, y, direct, oval, self.canvas, bigTimer, mediumTimer, smallTimer))
        for d in range(0, mediumdrops):
            x = self.x+xdelta*random.randint(0,mediumDistance)
            y = self.y+ydelta*random.randint(0,mediumDistance)
            oval = self.canvas.create_oval(x-1,y-1,x+1,y+1,fill="yellow")
            germs.append(dropletClass.droplet(1, x, y, direct, oval, self.canvas, bigTimer, mediumTimer, smallTimer))
        for d in range(0, smalldrops):
            x = self.x+xdelta*random.randint(0,smallDistance)
            y = self.y+ydelta*random.randint(0,smallDistance)
            oval = self.canvas.create_oval(x,y,x,y,fill="yellow")
            germs.append(dropletClass.droplet(2, x, y, direct, oval, self.canvas, bigTimer, mediumTimer, smallTimer))
    def tickDirectionTimer(self):
        if self.directionTimer >= random.randint(50,100):
            olddir = self.direction
            while self.direction == olddir:
                self.direction = random.randint(0,359)
            self.directionTimer = 0
        else:
            self.directionTimer += 1
    def kill(self, peopleArray):
        peopleArray.remove(self)
        self.canvas.delete(self.shape)
    def move(self, socdis, peopleArray):
        if socdis.get():
            angles = [0]*360
            for p in peopleArray:
                if p == self:
                    continue
                distance = distance = math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
                if distance < 50:
                    if self.x == p.x:
                        m = (self.y - p.y)/((self.x+1) - p.x)
                    else:
                        m = (self.y - p.y)/(self.x - p.x)
                    angle = math.floor(math.degrees(math.atan(m)))
                    while angle < 0:
                        angle += 360
                    while angle > 360:
                        angle -= 360
                    angles[angle] = 1
                    if angle < 20:
                        for y in range(angle, angle+20):
                            angles[y] = 1
                        for y in range(0,angle):
                            angles[y] = 1
                        for y in range(340+angle, 359):
                            angles[y] = 1
                    elif angle > 340:
                        for y in range(angle-20, angle):
                            angles[y] = 1
                        for y in range(angle, 359):
                            angles[y] = 1
                        for y in range(0, 20-(359-angle)):
                            angles[y] = 1
                    else:
                        for x in range(0,20):
                            angles[angle-x] = 1
                            angles[angle+x] = 1
            if 0 in angles:
                while angles[self.direction] == 1:
                    self.direction = random.randint(0,359)
        xdelta = math.cos(self.direction)
        ydelta = math.sin(self.direction)
        if not ((xdelta < 0 and self.x > 2 + xdelta) or (xdelta > 0 and self.x < 498 + xdelta)):
            xdelta = 0
        if not ((ydelta < 0 and self.y > 2 + ydelta) or (ydelta > 0 and self.y < 498 + ydelta)):
            ydelta = 0
        self.x += xdelta*2
        self.y += ydelta*2
        self.canvas.move(self.shape, xdelta*2, ydelta*2)