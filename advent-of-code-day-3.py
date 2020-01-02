def convertPathToCoordinates(path):
    if type(path) != str:
        return path
    axis = path[0]
    value = int(path[1:])
    if (axis == "R"):
        return (value, 0)
    elif (axis == "L"):
        return (-value, 0)
    elif (axis == "U"):
        return (0, value)
    elif (axis == "D"):
        return (0, -value)

def addPaths(pathA, pathB):
    if type(pathA) == str:
        pathA = convertPathToCoordinates(pathA)
    elif type(pathB) == str:
        pathB = convertPathToCoordinates(pathB)
    return tuple(map(sum, zip(pathA, pathB)))

def createWireRouteCoordinates(string):
    arr = string.split(",")
    pathCoordinates = [(0,0)]
    for i in range(0, len(arr), 1):
        pathCoordinates.append(addPaths(pathCoordinates[-1], arr[i]))
    return pathCoordinates


wireA = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
wireB = "U62,R66,U55,R34,D71,R55,D58,R83"
wireC = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
wireD = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
wireE = "R8,U5,L5,D3"
wireF = "U7,R6,D4,L4"

#print(createWireRouteCoordinates(wireA))
#print(createWireRouteCoordinates(wireB))
#print(createWireRouteCoordinates(wireC))
#print(createWireRouteCoordinates(wireD))
print(createWireRouteCoordinates(wireE)) # [(0, 0), (8, 0), (8, 5), (3, 5), (3, 2)]
print(createWireRouteCoordinates(wireF)) # [(0, 0), (0, 7), (6, 7), (6, 3), (2, 3)]