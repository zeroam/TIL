from osgeo import ogr

wkt = "POINT (1198054.34 648493.09)"
pt = ogr.CreateGeometryFromWkt(wkt)
bufferDistance = 500
poly = pt.Buffer(bufferDistance)
print(f'{pt.ExportToWkt()} buffered by {bufferDistance} is {poly.ExportToWkt()}')