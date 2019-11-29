from osgeo import ogr

multiline = ogr.Geometry(ogr.wkbMultiLineString)

line1 = ogr.Geometry(ogr.wkbLineString)
line1.AddPoint(1214242.4174581182, 617041.9717021306)
line1.AddPoint(1234593.142744733, 629529.9167643716)
multiline.AddGeometry(line1)

line1 = ogr.Geometry(ogr.wkbLineString)
line1.AddPoint(1184641.3624957693, 626754.8178616514)
line1.AddPoint(1219792.6152635587, 606866.6090588232)
multiline.AddGeometry(line1)

print(multiline.ExportToWkt())