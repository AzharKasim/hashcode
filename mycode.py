f = open("a.txt", "r")
firstInput = list(map(int, f.readline().split()))
print(firstInput)

simulationDuration = firstInput[0]
numIntersection = firstInput[1]
numStreets = firstInput[2]
numCars = firstInput[3]
bonusPoints = firstInput[4]

print(simulationDuration)
print(numIntersection)
print(numStreets)
print(numCars)
print(bonusPoints)

streetsNamesTotalList = []
listOfPaths = []
incomingStreets = []
uniqueCarPaths = {} 
mapStreetToIntersection = {}
mapStreetToWeight = {}
mapPathsStreetToIntersection = []

for i in range(numStreets):
    eachStreetsName= list(f.readline().split())
    print(eachStreetsName)
    streetsDirection = (eachStreetsName[0], eachStreetsName[1])
    print(streetsDirection)
    mapStreetToIntersection[eachStreetsName[2]] = streetsDirection
    mapStreetToWeight[eachStreetsName[2]] = eachStreetsName[3]

print(mapStreetToIntersection)
print(mapStreetToWeight)
uniqueCarPathsIntersection = []
for j in range(numCars):
    eachCarPath = list(f.readline().split())
    streetsNamesTotalList.append(eachCarPath)
    car_paths = eachCarPath.copy()
    del car_paths[0]
    #print("S", eachCarPath)
    #print("A", car_paths) 
    uniqueCarPaths[j] = car_paths

for a in uniqueCarPaths:
    print('a', a)
for k in streetsNamesTotalList:
    listOfPaths.append(k[0])

listOfPaths = sorted(listOfPaths, reverse=True)
totalHops = sum(list(map(int,listOfPaths)))

print(listOfPaths)
print(totalHops)
firstLineAnswer = str(int(listOfPaths[0])-1)

print('firstLineAns: ' , firstLineAnswer)
f = open("jam.txt", "w")
f.write(firstLineAnswer)

carsCompleteCounter = 0
timeCounter = 0 
#print(range(len(streetsNamesTotalList)))
while(carsCompleteCounter != numCars):
    print('time: ', timeCounter)
    for carIndex in range(len(streetsNamesTotalList)):
        nthCar = uniqueCarPaths[carIndex]
        print('nthCar', nthCar)
    carsCompleteCounter += 1
    timeCounter+=1