import os
import shutil

HEADER = "osm_100-"   

def convert(root, dpi = "l", mapId = "1"):
    tree = os.walk(root)
    for folder in tree:
        if len(folder[2]) > 0:
            path = HEADER + dpi + "-" + mapId
            path += folder[0].replace(root, "").replace("\\0", "").replace("\\z", "-").replace("\\x", "-")
            for tile in folder[2]:
                filename = path + tile.replace("y", "-")
                os.rename(folder[0] + "\\" + tile, root + "\\" + filename)
    for folder in next(os.walk(root))[1]:
        shutil.rmtree(root + "\\" + folder, ignore_errors=True)


if __name__ == "__main__":
    convert("navionics")