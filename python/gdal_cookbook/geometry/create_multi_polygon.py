from osgeo import ogr

multipolygon = ogr.Geometry(ogr.wkbMultiPolygon)

# Create ring #1
ring1 = ogr.Geometry(ogr.wkbLinearRing)
ring1.AddPoint(1204067.0548148106, 634617.5980860253)
ring1.AddPoint(1204067.0548148106, 620742.1035724243)
ring1.AddPoint(1215167.4504256917, 620742.1035724243)
ring1.AddPoint(1215167.4504256917, 634617.5980860253)
ring1.AddPoint(1204067.0548148106, 634617.5980860253)

# Create polygon #1
poly1 = ogr.Geometry(ogr.wkbPolygon)
poly1.AddGeometry(ring1)
multipolygon.AddGeometry(poly1)

# create ring #2
ring2 = ogr.Geometry(ogr.wkbLinearRing)
ring2.AddPoint(1179553.6811741155, 647105.5431482664)
ring2.AddPoint(1179553.6811741155, 626292.3013778647)
ring2.AddPoint(1194354.20865529, 626292.3013778647)
ring2.AddPoint(1194354.20865529, 647105.5431482664)
ring2.AddPoint(1179553.6811741155, 647105.5431482664)

# create polygon #2
poly2 = ogr.Geometry(ogr.wkbPolygon)
poly2.AddGeometry(ring2)
multipolygon.AddGeometry(poly2)

print(multipolygon.ExportToWkt())