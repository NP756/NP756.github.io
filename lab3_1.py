totalList = []
warningList = []
safeList = []
dangerList = []

i = 0

warningValue = int(input("Enter threshold for warning values: "))
dangerValue = int(input("Enter threshold for danger values: "))

while i >= 0:
    vibration = float(input("Enter vibration value (-1 to quit): "))
    totalList.append(vibration)
    if totalList[i] < warningValue:
        warningList.append(vibration[i])
    if totalList[i] > dangerValue:
        dangerList.append(vibration[i])
    if totalList[i] > warningValue and totalList[i] < dangerValue:
        safeList.append(vibration[i])
    if vibration == -1:
        i = -1

print("There are safe readings: ")
print(safeList)
                            
print("There are warning readings: ")
print(warningList)

print("There are danger readings: ")
print(dangerList)
                            
