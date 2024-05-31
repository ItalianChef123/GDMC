import gdpc
from gdpc import geometry
import math

editor = gdpc.Editor()
buildArea = editor.getBuildArea()
buildRect = buildArea.toRect()
print("Loading world slice")
worldSlice = editor.loadWorldSlice(buildRect)
print("World slice loaded")
heightMap = worldSlice.heightmaps["WORLD_SURFACE"]
building_positions = [(56, 119, 33), (60, 122, 33)]


def build_roads(positions):
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i != j:
                xDifference = positions[j][0] - positions[i][0]
                yDifference = positions[j][1] - positions[i][1]
                zDifference = positions[j][2] - positions[i][2]
                if xDifference != 0:
                    horizontalGradient = int(zDifference / xDifference)
                    additionalHorizontalChange = int(((zDifference / xDifference) - horizontalGradient) * xDifference)
                    GCD = math.gcd(additionalHorizontalChange, xDifference)
                    additionalHorizontalChange = additionalHorizontalChange / GCD
                    additionalHorizontalChangeInterval = xDifference / GCD
                    verticalGradient = int(yDifference / xDifference)
                    additionalVerticalChange = int(((yDifference / xDifference) - horizontalGradient) * xDifference)
                    print(additionalVerticalChange)
                    GCD = math.gcd(additionalVerticalChange, xDifference)
                    additionalVerticalChange = additionalVerticalChange / GCD
                    additionalVerticalChangeInterval = xDifference / GCD
                    print(additionalVerticalChangeInterval)
                else:
                    horizontalGradient = zDifference
                    additionalHorizontalChange = 0
                    additionalHorizontalChangeInterval = 0
                    verticalGradient = yDifference
                    additionalVerticalChange = 0
                    additionalVerticalChangeInterval = 0
                currentX = positions[i][0]
                currentY = positions[i][1]
                currentZ = positions[i][2]
                finalX = positions[j][0]
                if xDifference < 0:
                    xChange = -1
                elif xDifference > 0:
                    xChange = 1
                else:
                    xChange = 0
                l = 0
                m = 0
                for k in range(xDifference + 1):
                    nextZ = currentZ + horizontalGradient
                    nextY = currentY + verticalGradient
                    print(nextY)
                    print(currentX)
                    if l != additionalHorizontalChangeInterval:
                        if l < additionalHorizontalChange:
                            l = l + 1
                            nextZ = nextZ + 1
                        elif l > additionalHorizontalChange:
                            l = l - 1
                            nextZ = nextZ - 1
                    else:
                        l = 0
                    if m != additionalVerticalChangeInterval:
                        if m < additionalVerticalChange:
                            m = m + 1
                            nextY = nextY + 1
                        elif m > additionalHorizontalChange:
                            m = m - 1
                            nextY = nextY - 1
                    else:
                        m = 0
                    geometry.placeCuboid(editor, (currentX, currentY, currentZ),
                                         (currentX + xChange, nextY, nextZ),
                                         gdpc.Block("dirt_path"))
                    currentX = currentX + xChange
                    currentY = nextY
                    currentZ = nextZ
                    if currentX == finalX:
                        break


build_roads(building_positions)
