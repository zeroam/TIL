import sys
from osgeo import ogr, gdal

ds = gdal.OpenEx('point_out.shp', gdal.OF_VECTOR)
if ds is None:
    print('Open failed.\n')
    sys.exit(1)

lyr = ds.GetLayerByName('Point')    # Get point layer failed
lyr = ds.GetLayer()

lyr.ResetReading()

for feat in lyr:
    feat_defn = lyr.GetLayerDefn()
    for i in range(feat_defn.GetFieldCount()):
        field_defn = feat_defn.GetFieldDefn(i)

        # Tests below can be simplified with just :
        # print(feat.GetField(i))

    geom = feat.GetGeometryRef()
    if geom is not None and geom.GetGeometryType() == ogr.wkbPoint:
        print(f'{geom.GetX():.3f}, {geom.GetY():.3f}')
    else:
        print('no point geometry\n')

ds = None