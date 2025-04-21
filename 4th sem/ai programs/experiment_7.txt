'''
Forward Chaining
'''

database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary", "Green", "Yellow"]
def display():
    print("\n X is \n1..Croaks \n2.Eat Flies \n3.shrimps \n4.Sings ", end='')
    print("\n Select One ", end='')
def main():
    print("Forward Chaining", end='')
    display()
    x = int(input())
    print(" \n", end='')
    if x == 1 or x == 2:
        print(" Chance Of Frog ", end='')
    elif x == 3 or x == 4:
        print(" Chance of Canary ", end='')
    else:
        print("\Invalid", end='')
    if x >= 1 and x <= 4:
        print("In X is ", end='')
    print (database[x-1], end='')
    print("In Color Is 1.Green 2.Yellow", end='')
    print("\n Select Option ", end='')
    k = int(input())
    if k == 1 and (x == 1 or x == 2):
        print(" yes it is ", end='')
        print(knowbase[0], end='')
        print(" And Color Is ", end='')
        print(knowbase[2], end='')
    elif k == 2 and (X == 3 or x == 4):
        print(" yes it is ", end='')
        print(knowbase[1], end='')
        print(" And Color Is ", end='')
        print(knowbase[3], end='')
    else:
        print("Invalid Knowlwdgebase", end='')

if __name__ == "__main__":
    main()


'''
Backward Chaining
'''

database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary"]
color = ["Green", "Yellow"]
def display():
    print("\n In X is In \n1.frog \n2.canary", end='')
    print("\n Select One ", end='')
def main():
    print("\nBackward--Chaining", end='')
    display()
    x = int(input())
    print(" \n", end='')
    if x == 1:
        print(" Chance Of eating flies ", end='')
    elif x == 2:
        print(" Chance of shrimping ", end='')
    else:
        print("\Select Option", end='')
    if x >= 1 and x <= 2:
        print("\n X is ", end='')
        print(knowbase[x-1], end='')
        print("\n1 green \n2.yellow")
        k = int(input())
        if k == 1 and x == 1: # frog® and green1
            print(" yes it is in ", end='')
            print(color[0], end='')
            print(" colour and will ", end='')
            print (database [0])
        elif k == 2 and x == 2: # canary1 and yelLow3
            print(" yes it is in", end='')
            print (color[1], end='')
            print(" Colour and will ", end='')
            print(database[1])
        else:
            print("\nInvalid Knowledgebase", end='')

if __name__ == "__main__":
    main()