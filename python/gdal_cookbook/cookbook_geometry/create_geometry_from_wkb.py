from osgeo import ogr
from base64 import b64decode

wkb = b64decode("AIAAAAFBMkfmVwo9cUEjylouFHrhAAAAAAAAAAA=")
point = ogr.CreateGeometryFromWkb(wkb)
print(f'{point.GetX()},{point.GetY()}')