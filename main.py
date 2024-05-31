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
building_positions = [(56, 119, 33), (56, 119, 19)]


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
                    GCD = math.gcd(xDifference, math.gcd(yDifference, zDifference))
                else:
                    horizontalGradient = zDifference
                    additionalHorizontalChange = 0
                    additionalHorizontalChangeInterval = 0
                    GCD = math.gcd(yDifference, zDifference)
                yInterval = yDifference / GCD
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
                for k in range(xDifference + 1):
                    nextZ = currentZ + horizontalGradient
                    if l != additionalHorizontalChange:
                        if l < additionalHorizontalChange:
                            l = l + 1
                            nextZ = nextZ + 1
                        else:
                            l = l - 1
                            nextZ = nextZ - 1
                    elif l == additionalHorizontalChangeInterval:
                        l = 0
                    geometry.placeCuboid(editor, (currentX, currentY, currentZ),
                                         (currentX + xChange, currentY + yInterval, nextZ),
                                         gdpc.Block("dirt_path"))
                    currentX = currentX + xChange
                    currentY = currentY + yInterval
                    currentZ = nextZ
                    if currentX == finalX:
                        break


build_roads(building_positions)
