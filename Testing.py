import time

import gdpc.editor_tools
from gdpc import Editor, Block, geometry

editor = Editor(buffering=True)

block = editor.getBlock((0, 115, 6))
print(block)

editor.placeBlock((0, 115, 6), Block("stone"))

geometry.placeCuboid(editor, (0, 115, 6), (1, 116, 7), Block("oak_planks"))

build_area = editor.getBuildArea()
print(build_area)

editor.placeBlock(build_area.center, Block("dragon_head"))

time.sleep(5)
geometry.placeCuboid(editor, build_area.offset, build_area.last, Block("dragon_head"))

editor.placeBlock(build_area.center, Block("stone_brick_stairs",
                                           {"facing": "east",
                                           "half": "bottom", "shape": "outer_right", "waterlogged": "false"}))

gdpc.editor_tools.placeContainerBlock(editor, build_area.end, Block("minecraft:hopper", {}),
                                      [((2, 0), "wheat"), ((4, 0), "egg")])

road_palette = [Block(id) for id in 3*["cobblestone"] + ["andesite"] + ["gravel"]]

geometry.placeCuboid(editor, (33, 119, -7), (29, 119, -11), road_palette)
geometry.placeCuboid(editor, (33, 120, -7), (29, 120, -11), Block("air"))
