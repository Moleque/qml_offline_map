import sys
import os
import shutil
import re

HEADER = "osm_100-"   


def convert(root = "tiles", mapId = "1", dpi = "l"):
    tree = os.walk(root)
    for folder in tree:
        if len(folder[2]) > 0:
            path = HEADER + dpi + "-" + mapId + "-"
            values = re.findall(r'\w(\d+)\\0', folder[0])
            path += str(int(values[0]) - 1) + "-" + values[1]
            for tile in folder[2]:
                filename = path + tile.replace("y", "-")
                os.rename(folder[0] + "\\" + tile, root + "\\" + filename)
    for folder in next(os.walk(root))[1]:
        shutil.rmtree(root + "\\" + folder, ignore_errors=True)


if __name__ == "__main__":
    root = "tiles"
    mapId = "1"
    dpi = "l"
    
    if sys.argv[1]:
        root = sys.argv[1]
    if sys.argv[2]:
        mapId = sys.argv[2]
    if sys.argv[3]:
        dpi = sys.argv[3]
    convert(root, mapId, dpi)