import random, personClass

def addPerson(stats, peopleArray, canvas):
    stats[3] += 1
    x = random.randint(3,497)
    y = random.randint(3,497)
    oval = canvas.create_oval(x-3,y-3,x+3,y+3,fill="black")
    peopleArray.append(personClass.person(x, y, oval, canvas))
    
def addTenPeople(stats, peopleArray, canvas):
    stats[3] += 10
    for x in range(0,10):
        x = random.randint(3,497)
        y = random.randint(3,497)
        oval = canvas.create_oval(x-3,y-3,x+3,y+3,fill="black")
        peopleArray.append(personClass.person(x, y, oval, canvas))

def addFiftyPeople(stats, peopleArray, canvas):
    stats[3] += 50
    for x in range(0,50):
            x = random.randint(3,497)
            y = random.randint(3,497)
            oval = canvas.create_oval(x-3,y-3,x+3,y+3,fill="black")
            peopleArray.append(personClass.person(x, y, oval, canvas))

def addIPerson(stats, canvas, peopleArray):
    stats[2] += 1
    stats[3] += 1
    x = random.randint(3,497)
    y = random.randint(3,497)
    oval = canvas.create_oval(x-3,y-3,x+3,y+3,fill="red")
    newPerson = personClass.person(x, y, oval, canvas)
    newPerson.startInfection()
    peopleArray.append(newPerson)

def addTenIPeople(stats, canvas, peopleArray):
    stats[2] += 10
    stats[3] += 10
    for x in range(0,10):
            x = random.randint(3,497)
            y = random.randint(3,497)
            oval = canvas.create_oval(x-3,y-3,x+3,y+3,fill="red")
            newPerson = personClass.person(x, y, oval, canvas)
            newPerson.startInfection()
            peopleArray.append(newPerson)
        
def addFiftyIPeople(stats, canvas, peopleArray):
    stats[2] += 50
    stats[3] += 50
    for x in range(0,50):
            x = random.randint(3,497)
            y = random.randint(3,497)
            oval = canvas.create_oval(x-3,y-3,x+3,y+3,fill="red")
            newPerson = personClass.person(x, y, oval, canvas)
            newPerson.startInfection()
            peopleArray.append(newPerson)

def drawVents(vents, canvas):
    if vents.get():
        canvas.create_rectangle(0,0,60,60, fill="gray", tags="vent")
        canvas.create_rectangle(0,440,60,500, fill="gray", tags="vent")
        canvas.create_rectangle(440,0,500,60, fill="gray", tags="vent")
        canvas.create_rectangle(440,440,500,500, fill="gray", tags="vent")
    else:
        canvas.delete("vent")