totalList = []
warningList = []
safeList = []
dangerList = []

q = 0
i = 0

while q <= 0:
    vibration = float(input("Enter vibration value (-1 to quit): "))
    totalList.append(vibration)

    if vibration == -1:
        q = -1
 
warningValue = float(input("Enter threshold for warning values: "))
dangerValue = float(input("Enter threshold for danger values: "))        

while i < len(totalList):
    if totalList[i] < warningValue:
        warningList.append(totalList[i])
        i = i + 1
    if totalList[i] > dangerValue:
        dangerList.append(totalList[i])
        i = i + 1
    if totalList[i] > warningValue and totalList[i] < dangerValue:
        safeList.append(totalList[i])
        i = i + 1
 

print("There are safe readings: ")
print(safeList)
                            
print("There are warning readings: ")
print(warningList)

print("There are danger readings: ")
print(dangerList)
                            
