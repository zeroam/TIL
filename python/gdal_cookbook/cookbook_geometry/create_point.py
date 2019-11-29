from osgeo import ogr
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(1116651.439379124, 637392.6969887456)
print(point.ExportToWkt())