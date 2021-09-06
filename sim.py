from tkinter import *
import random, dropletClass, personClass, buttonFunctions

def onClosing():
    root.destroy()

def mainLoop(stats, socdis, peopleArray, vents, ac, germs, rein):
    ##########SETTINGS##########
    deathChance = 10000 #chance of death, default 1/10000, number is denominator
    bigDropChance = 8 #chance of a big droplet infecting someone with contact, default 1/8, number is denominator
    mediumDropChance = 16 #chance of a medium droplet infecting someone with contact, default 1/16, number is denominator
    smallDropChance = 32 #chance of a small droplet infecting someone with contact, default 1/32, number is denominator
    bigDistance = 30 #maximum distance big droplet travels, default 30
    mediumDistance = 45 #maximum distance medium droplet travels, default 45
    smallDistance = 60 #maxium distance small droplet travels, default 60
    bigTimer = 40 #maximum time big droplet will 'hang', minimum time is max/2, default 40
    mediumTimer = 200 #maximum time medium droplet will 'hang', minimum time is max/2, default 200
    smallTimer = 500 #maximum time small droplet will 'hang', minimum time is max/2, default 500
    bigNumber = 5 #maximum amount of big drops expelled when sneeze happens, minimum is 0, default 5
    mediumNumber = 10 #maximum amount of medium drops expelled when sneeze happens, minimum is 0, default 10
    smallNumber = 20 #maximum amount of small drops expelled when sneeze happens, minimum is 0, default 20
    recoveryLength = 2000 #amount of time it takes a dot to recover, default 2000
    immunityLength = 1000 #amount of time someone stays immune if fading immunity setting is checked, default 1000
    sneezeTimer = 200 #maxmum amount of time between sneezes, minimum is max/2, default 200
    sideSneeze = True #True if the sneeze expells to the side of a person as if head was turned, default True
    ############################
    canvas.after(10, mainLoop, stats, socdis, peopleArray, vents, ac, germs, rein)
    deathLabel.config(text="Deaths: "+str(stats[0]))
    infectedLabel.config(text="Infected: "+str(stats[2]))
    recoveredLabel.config(text="Recovered: "+str(stats[1]))
    totalLabel.config(text="Total People: " + str(stats[3]))
    for g in germs:
        g.move(vents, ac, germs)
        g.tickTimer(germs)
    for p in peopleArray:
        p.tickDirectionTimer()
        p.tickCuredTimer(stats, recoveryLength, rein)
        p.tickInfectedTimer(sneezeTimer, germs, bigDistance, mediumDistance, smallDistance, sideSneeze, bigNumber, mediumNumber, smallNumber, bigTimer, mediumTimer, smallTimer)
        p.tickImmunityTimer(immunityLength)
        p.move(socdis, peopleArray)
        death = random.randint(0,deathChance-1)
        if death == 0 and p.infected:
            stats[2] -= 1
            p.kill(peopleArray)
            stats[0] += 1
        for g in germs:
            if p.x-3 < g.x and p.x+3 > g.x and p.y-3 < g.y and p.y+3 > g.y:
                chance = random.randint(0,bigDropChance - 1)
                if g.size == 1:
                    chance = random.randint(0,mediumDropChance - 1)
                if g.size == 2:
                    chance = random.randint(0, smallDropChance - 1)
                if chance == 0 and not p.cured and not p.infected:
                    p.startInfection()
                    stats[2] += 1
                g.absorbed(germs)

if __name__ == "__main__":
    peopleArray = []
    germs = []
    
    stats = [0,0,0,0] #deaths, recovered, infected, total people
        
    root = Tk()
    canvas = Canvas(root, width=500, height=500, bg="white")
    canvas.grid(row=0, column=0, columnspan=4)
    Label(text="Add People:").grid(row=1, column=0)
    buttonAdd = Button(root, text="Add Person", command = lambda arg1=stats, arg2=peopleArray, arg3=canvas: buttonFunctions.addPerson(arg1, arg2, arg3))
    buttonAdd.grid(row=1, column=1)

    buttonTenAdd = Button(root, text="Add 10 People", command = lambda arg1=stats, arg2=peopleArray, arg3=canvas: buttonFunctions.addTenPeople(arg1, arg2, arg3))
    buttonTenAdd.grid(row=1, column=2)

    buttonTenAdd = Button(root, text="Add 50 People", command = lambda arg1=stats, arg2=peopleArray, arg3=canvas: buttonFunctions.addFiftyPeople(arg1, arg2, arg3))
    buttonTenAdd.grid(row=1, column=3)

    Label(text="Add Infected:").grid(row=2, column=0)
    buttonAddI = Button(root, text="Add Infected Person", command = lambda arg1=stats, arg2=canvas, arg3=peopleArray: buttonFunctions.addIPerson(arg1, arg2, arg3))
    buttonAddI.grid(row=2, column=1)

    buttonAddI = Button(root, text="Add 10 Infected People", command = lambda arg1=stats, arg2=canvas, arg3=peopleArray: buttonFunctions.addTenIPeople(arg1, arg2, arg3))
    buttonAddI.grid(row=2, column=2)

    buttonAddI = Button(root, text="Add 50 Infected People", command = lambda arg1=stats, arg2=canvas, arg3=peopleArray: buttonFunctions.addFiftyIPeople(arg1, arg2, arg3))
    buttonAddI.grid(row=2, column=3)

    vents = IntVar()
    ventCheck = Checkbutton(root, text="Airflow on", variable=vents, command= lambda arg1=vents, arg2=canvas: buttonFunctions.drawVents(arg1, arg2))
    ventCheck.grid(row=3, column=0)

    ac = IntVar()
    acCheck = Checkbutton(root, text="No filter in airflow", variable=ac)
    acCheck.grid(row=3, column=1)

    socdis = IntVar()
    socdisCheck = Checkbutton(root, text="Social Distancing", variable=socdis)
    socdisCheck.grid(row=3, column=2)

    rein = IntVar()
    reinCheck = Checkbutton(root, text="Fading Immunity", variable = rein)
    reinCheck.grid(row=3, column=3)

    totalLabel = Label(root, text="Total People: "+str(stats[3]))
    totalLabel.grid(row=4, column=0)

    deathLabel = Label(root, text="Deaths: "+str(stats[0]))
    deathLabel.grid(row=4, column=1)

    infectedLabel = Label(root, text="Infected: "+str(stats[2]))
    infectedLabel.grid(row=4, column=2)

    recoveredLabel = Label(root, text="Recovered: "+str(stats[1]))
    recoveredLabel.grid(row=4, column=3)

    mainLoop(stats, socdis, peopleArray, vents, ac, germs, rein)

    root.protocol("WM_DELETE_WINDOW", onClosing)
    root.mainloop()