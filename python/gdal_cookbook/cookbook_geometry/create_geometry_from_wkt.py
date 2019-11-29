from osgeo import ogr

wkt = "POINT (1120351.5712494177 741921.4223245403)"
point = ogr.CreateGeometryFromWkt(wkt)
print(f'{point.GetX()},{point.GetY()}')