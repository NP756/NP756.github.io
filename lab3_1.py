totalList = []
warningList = []
safeList = []
dangerList = []

q = True
i = 0

while q == True:
    vibration = float(input("Enter vibration value (-1 to quit): "))
    totalList.append(vibration)

    if vibration == -1:
        q = False
 
warningValue = float(input("Enter threshold for warning values: "))
dangerValue = float(input("Enter threshold for danger values: "))        

while i < len(totalList):
    if totalList[i] < warningValue:
        warningList.append(totalList[i])
    if totalList[i] > dangerValue:
        dangerList.append(totalList[i])
    if totalList[i] > warningValue and totalList[i] < dangerValue:
        safeList.append(totalList[i])

print("There are safe readings: ")
print(safeList)
                            
print("There are warning readings: ")
print(warningList)

print("There are danger readings: ")
print(dangerList)
                            
