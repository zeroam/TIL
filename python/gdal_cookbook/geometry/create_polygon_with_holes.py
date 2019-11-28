from osgeo import ogr

# Create outer ring
outRing = ogr.Geometry(ogr.wkbLinearRing)
outRing.AddPoint(1154115.274565847, 686419.4442701361)
outRing.AddPoint(1154115.274565847, 653118.2574374934)
outRing.AddPoint(1165678.1866605144, 653118.2574374934)
outRing.AddPoint(1165678.1866605144, 686419.4442701361)
outRing.AddPoint(1154115.274565847, 686419.4442701361)

# Create inner ring
innerRing = ogr.Geometry(ogr.wkbLinearRing)
innerRing.AddPoint(1149490.1097279799, 691044.6091080031)
innerRing.AddPoint(1149490.1097279799, 648030.5761158396)
innerRing.AddPoint(1191579.1097525698, 648030.5761158396)
innerRing.AddPoint(1191579.1097525698, 691044.6091080031)
innerRing.AddPoint(1149490.1097279799, 691044.6091080031)

# Create polygon
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(outRing)
poly.AddGeometry(innerRing)

print(poly.ExportToWkt())