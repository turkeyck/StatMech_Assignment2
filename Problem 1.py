import random
import time
import math

def Function(sides,diceNum,trialNum):
    c1=time.clock()
    print("========================")

    print("Number of sides = ", sides)
    print("Number of dice = ", diceNum)
    print("Number of trials = ", trialNum)

    print("-----Simulation(S)-----")


    # Histogram records the sum of each trial
    histogram = []
    for s in range(trialNum):
        histogram.append(0)
    print("Initialization")
#    print("histogram : ",histogram)

    # Histogram2 records the number of events of dice sum
    histogram2 = []
    for s in range(sides*diceNum):
        histogram2.append(0)
#    print("histogram2 : ",histogram2)


    # Histogram3 records the square sum of each trial
    histogram3 = []
    for s in range(trialNum):
        histogram3.append(0)
#    print("histogram3 : ",histogram3)



    r = 0

    for t in range(trialNum):
        for q in range(diceNum):
            r = int(random.random()*sides)+1
            histogram[t] += r
            histogram3[t] += r*r
        r1 = histogram[t] -1
        histogram2[r1] += 1

    print("After ",trialNum ,"trials, the sum of dice number of each trial")
    print(histogram)
    print("Distribution for the sum of dice [1,2,3...]")
    print(histogram2)

    print("-----Simulation(E)-----")

    print("-----Analysis(S)-------")


    sample = 0
    Sum = 0
    SqSum = 0


    Sum = histogram[sample]
    SqSum = histogram3[sample]

    mean = Sum / diceNum

    variance = SqSum / diceNum - mean*mean

    deviation = math.sqrt(variance)


    print("mean : ",mean)
    # print("SqSum : ",SqSum) # for debug
    print("variance : ",variance)
    print("standard deviation : ",deviation)

    meanTheo = (sides+1) / (2)

    varianceTheo = (sides+1)*(2*sides+1)/6 - meanTheo*meanTheo

    deviationTheo = math.sqrt(varianceTheo)

    print("mean(theory) = ",meanTheo)
    print("variance(theory) =",varianceTheo)
    print("standard deviation(theory) =",deviationTheo)

    devMean = abs(mean - meanTheo) / meanTheo * 100
    devVar = abs(variance - varianceTheo ) /varianceTheo *100
    devDev = abs(deviation - deviationTheo ) / deviationTheo *100

    print("(Mean) deviation form theory (%) =", devMean)
    print("(Variance) deviation form theory (%) =", devVar)
    print("(Standard deviation) deviation form theory (%) =", devDev)

    print("-----Analysis(E)-------")

    print("========================")


def run():
    Function(10,2,1)
    Function(20,10,1)
