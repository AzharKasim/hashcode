f = open("a.txt", "r")
firstInput = list(map(int, f.readline().split()))
print(firstInput)

simulationDuration = firstInput[0]
numIntersection = firstInput[1]
numStreets = firstInput[2]
numCars = firstInput[3]
bonusPoints = firstInput[4]

print("HI: " ,simulationDuration)
print("HI: " ,numIntersection)
print("HI: " ,numStreets)
print("HI: " ,numCars)
print("HI: " ,bonusPoints)

streetsNamesTotalList = []
listOfPaths = []
incomingStreets = []
uniqueCarPaths = {} 
mapStreetToIntersection = {}
mapStreetToWeight = {}
mapPathsStreetToIntersection = []

class Street:
    def __init__(self, _name, _startpt, _endpt):
        self.name = _name
        self.startPt = _startpt
        self.endPt = _endpt
        
streetsObj = []

class Intersection:
    def __init__(self):
        self.mID = 0
        self.mStreetsList = []
        
interObjList = []
    
for i in range(numStreets):
    eachStreetsName= list(f.readline().split())
    print("STREETS: ",eachStreetsName)
    streetsDirection = (eachStreetsName[0], eachStreetsName[1])
    print(streetsDirection)
    u = int(eachStreetsName[0])
    v = int(eachStreetsName[1])
    
    myStreet = Street(eachStreetsName[2], u, v)
    streetsObj.append(myStreet)
    
for i in range(len(streetsObj)):
    print(streetsObj[i].name) 
    print(streetsObj[i].startPt) 
    print(streetsObj[i].endPt)
    
for i in range(numIntersection):
    myInter = Intersection()
    myInter.mID = i;
    for street in streetsObj:
        if street.startPt == i or street.endPt == i:
            myInter.mStreetsList.append(street)
    interObjList.append(myInter)
    
for i in range(len(interObjList)):
    print(interObjList[i].mID)
    for j in range(len(interObjList[i].mStreetsList)):
        print(interObjList[i].mStreetsList[j].name)
