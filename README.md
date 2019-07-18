# Converter tiles from SAS.Planet to QML OSM plugin format to using offline maps.
For using offline maps in QML(Qt) you need to use [OSM plugin](https://blog.qt.io/blog/2017/05/24/qtlocation-using-offline-map-tiles-openstreetmap-plugin/). This plugin gives you posibility to take map tiles from your local directory. Names of tile files have to be format: 

`osm_100-<l|h>-<map_id>-<z>-<x>-<y>.<extension>`

Where can we get tiles?
You can download tiles by [SAS.Planet](http://www.sasgis.org/download/)

![screen1](https://github.com/Moleque/qml_offline_map/blob/master/img/screen1.png?raw=true)

![screen2](https://github.com/Moleque/qml_offline_map/blob/master/img/screen2.png?raw=true)

And use this app for convert folder with tiles to right format of OSM plugin.

For using run:

`python main.py <tiles_dir> <map_id> <l|h>`
