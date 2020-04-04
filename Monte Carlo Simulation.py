import random
import os
import matplotlib
import matplotlib.pyplot as plt
import time

lower_bust = 31.235
higher_profit = 63.208

sampleSize = 1000
startingFunds = 100000


os.system("cls")
print("\n")

'''def randomDice():
    result = random.randint(1,100)
    if result == 100:
        #print("\u001b[31mYou Lose\u001b[35;1m")
        return False
    elif result <= 50:
        #print("\u001b[31mYou Lose\u001b[35;1m")
        return False
    elif 100 > result > 50:
        #print("\u001b[32;1mYou Win\u001b[35;1m")
        return True'''

def randomDice():
    result = random.randint(1,100)

    if result <= 50:
        #print("\u001b[31mYou Lose\u001b[35;1m")
        return False
    elif result >= 51:
        #print("\u001b[32;1mYou Win \u001b[35;1m")
        return True

def multiplebettor(funds,initial_wager,wager_count):
    global multiple_busts
    global multiple_profits

    value = funds
    wager = initial_wager
    wX = []
    vY = []

    currentwager = 1
    previousWager = "win"
    previousWagerAmount = initial_wager

    while currentwager <= wager_count:
        if previousWager == "win":
            # print("YOU WIN")
            if randomDice():
                value += wager
                # print(value)
                wX.append(currentwager)
                vY.append(value)
            else:
                value -= wager
                previousWager = "loss"
                # print(value)
                previousWagerAmount = wager
                wX.append(currentwager)
                vY.append(value)
                if value <= 0:
                    # print("BROKE ||").currentwager, "bets"
                    multiple_busts += 1
                    break

        elif previousWager == "loss":
            # print("YOU LOST")
            if randomDice():
                wager = previousWagerAmount * random_multiple

                if (value - wager) < 0:
                    wager = value
                # print("You Won", wager)
                value += wager
                # print(value)
                wager = initial_wager
                previousWager = "win"
                wX.append(currentwager)
                vY.append(value)
            else:
                wager = previousWagerAmount * random_multiple
                if (value - wager) < 0:
                    wager = value
                # print("YOU LOST", wager)
                value -= wager
                previousWager = "loss"
                previousWagerAmount = wager
                wX.append(currentwager)
                vY.append(value)
                if value <= 0:
                    # print("Broke",currentwager)
                    multiple_busts += 1
                    break
                # print(value)
                previousWager = "loss"

        currentwager += 1
    # print(value)
    #plt.plot(wX, vY, color)
    if value > funds:
        multiple_profits += 1

def dAlembert(funds,initial_wager,wager_count):
    global Return
    global da_busts
    global da_profits

    value = funds
    wager = initial_wager
    currentWager = 1
    previousWager = "win"
    prevoiousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == "win":
            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager
            #print("current wager : ", wager, "value : ", value)
            if randomDice():
                value += wager
            else:
                value -= wager
                previousWager = "loss"
                #print("we lost, current value : ", value)
                previousWagerAmount = wager

                if value <= 0:
                    da_busts += 1
                    break
        elif previousWager == "loss":
            wager = previousWagerAmount + initial_wager
            if (value - wager) <= 0:
                wager = value
            #print("Lost the last wager, current wager : ", wager, 'value',value)

            if randomDice():
                value += wager
                previousWagerAmount = wager
                #print("we won, current value : " , value)
                previousWager = "win"
            else:
                value -= wager
                #print("we lost, current value : ", value)
                previousWagerAmount = wager

                if value <= 0:
                    da_busts += 1
                    break
        currentWager += 1
    if value > funds:
        da_profits += 1
    #print(value)
    Return += value


def doublebettor(value,initial_wager,wager_count,color):
    funds = value
    wager = initial_wager

    global double_busts
    global double_profits

    wX = []
    vY = []

    currentwager = 1
    previousWager = "win"
    previousWagerAmount = initial_wager

    while currentwager <= wager_count:
        if previousWager == "win":
            #print("YOU WIN")
            if randomDice():
                value += wager
                #print(value)
                wX.append(currentwager)
                vY.append(value)
            else:
                value -= wager
                previousWager = "loss"
                #print(value)
                previousWagerAmount = wager
                wX.append(currentwager)
                vY.append(value)
                if value <= 0:
                    #print("BROKE ||").currentwager, "bets"
                    double_busts += 1
                    break

        elif previousWager == "loss":
            #print("YOU LOST")
            if randomDice():
                wager = previousWagerAmount * 2

                if (value - wager) < 0:
                    wager = value
                #print("You Won", wager)
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = "win"
                wX.append(currentwager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                #print("YOU LOST", wager)
                value -= wager
                previousWager = "loss"
                previousWagerAmount = wager
                wX.append(currentwager)
                vY.append(value)
                if value <= 0:
                    #print("Broke",currentwager)
                    double_busts += 1
                    break
                #print(value)
                previousWager = "loss"


        currentwager += 1
    #print(value)
    plt.plot(wX,vY,color)
    if value > funds:
        double_profits += 1

def bettingmachine(value,initialwager,wager_count,color):
    funds = value
    wager = initialwager
    global machine_busts
    global machine_profits
    wX=[]
    vY=[]

    currentwager = 1

    while currentwager <= wager_count:
        if randomDice():
            value += wager
            wX.append(currentwager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentwager)
            vY.append(value)

        currentwager += 1
    if value <= 0:
        value = 0
        machine_busts += 1
        #value = "\u001b[31mB R O K E || N I G G A\u001b[35;1m"
    #print("Funds : " + "\u001b[36;1m " + str(value) + "\u001b[35;1m")
    plt.plot(wX,vY,color)
    if value > funds:
        value = 0
        machine_profits += 1


#x = 0   # Number of person betting

#while x < 10:
    #bettingmachine(10000,100,10000)
    #x += 1

#plt.ylabel("Account Value")
#plt.xlabel("Wager Count")
#plt.show()

while True:
    #wagerSize = 100
    #wagerCount = 1000
    wagerSize = random.uniform(1.0,1000.00)
    wagerCount = random.uniform(10.0,10000)

    Return = 0.0
    da_busts = 0.0
    da_profits = 0.0
    daSampSize = 1000

    counter = 1
    while counter <= daSampSize:
        dAlembert(startingFunds,wagerSize,wagerCount)
        counter += 1

    ROI = Return - (daSampSize - startingFunds)
    totalInvested = daSampSize * startingFunds

    percentROI = (ROI/totalInvested) * 100.00

    if percentROI > 0.865:
        print("#######################################################")
        print("Total invested : ", daSampSize * startingFunds)
        print("Total Return : ", Return)
        print("Return on Investment : ", Return - (daSampSize - startingFunds))
        print("Percent ROI : ", percentROI)
        print("Bust Rate : ", (da_busts/daSampSize)* 100.00)
        print("Profit Rate : ", (da_profits/daSampSize)* 100.00)
        print("Wager size : ",wagerSize)
        print("Wager count : ", wagerCount)
        print("Wager size percentage : ", (wagerSize / startingFunds) * 100.00)

'''while True:
    multiple_busts = 0.0
    multiple_profits = 0.0
    
    multipleSampSize = 100000
    currentSample = 1

    random_multiple = random.uniform(0.1,10.0)

    while currentSample <= multipleSampSize:
        multiplebettor(startingFunds,wagerSize,wagerCount)
        currentSample += 1
    if ((multiple_busts/multipleSampSize) * 100.00 < lower_bust) and ((multiple_profits/multipleSampSize)*100.00 > higher_profit):
        print('##################')
        print('Found a winner, the multiple was : ', random_multiple)
        print('Lower bust to beat', lower_bust)
        print('Higher profit rate to beat: ', higher_profit)
        print('Bust rate : ', (multiple_busts/multipleSampSize) * 100.00)
        print('Profit rate : ', (multiple_profits/multipleSampSize)* 100.00)
        print('###################')
    else:
        print('##################')
        print('Found a loser, the multiple was : ', random_multiple)
        print('Lower bust to beat', lower_bust)
        print('Higher profit rate to beat: ', higher_profit)
        print('Bust rate : ', (multiple_busts / multipleSampSize) * 100.00)
        print('Profit rate : ', (multiple_profits / multipleSampSize) * 100.00)
        print('###################')'''

    #doublebettor(startingFunds,wagerSize,wagerCount, 'c')


