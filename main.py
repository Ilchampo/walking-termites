#!/usr/bin/env python3

def findChip(steps, interval, termites, chips, canvas):
    import turtle as t
    import termites as term
    import random as r

    t.setworldcoordinates(-maxLimit-2, -maxLimit-2, maxLimit+2, maxLimit+2)
    
    # Set variables
    limits = [-maxLimit, maxLimit, -maxLimit, maxLimit]
    termiteList = []
    chipList = []
    tTermiteList = list()
    tChipList = list()
    
    # Create termites
    for pi in range (termites):
        termiteList.append(term.Termite((r.randint(limits[0], limits[1]), r.randint(limits[2], limits[3]))))
        tTermiteList.append(t.Turtle(shape="turtle"))
        tTermiteList[pi].color(termiteList[pi].getColor())
        tTermiteList[pi].speed(0)
        tTermiteList[pi].shapesize(0.4, 0.6)
        tTermiteList[pi].penup()
        tTermiteList[pi].goto(termiteList[pi].getPosition())

    # Create chips
    for pi in range (chips):
        chipList.append(term.Chip(pi, (r.randint(limits[0], limits[1]), r.randint(limits[2], limits[3]))))
        tChipList.append(t.Turtle(shape="turtle"))
        tChipList[pi].color(chipList[pi].getColor())
        tChipList[pi].speed(0)
        tChipList[pi].shapesize(0.4, 0.6)
        tChipList[pi].penup()
        tChipList[pi].goto(chipList[pi].getPosition())

    # Turle screen
    screen = t.getscreen()

    

    # Exits window when clicking
    t.exitonclick()

def main(args):
    if len(args) == 5:
        steps = int(args[0])
        interval = int(args[1])
        termites = int(args[2])
        chips = int(args[3])
        canvas = int(args[4])
        findChip(steps, interval, termites, chips, canvas)
    else:
        print(main.__doc__)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])