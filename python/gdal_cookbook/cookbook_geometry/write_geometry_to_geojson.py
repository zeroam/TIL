from osgeo import ogr

# Create test polygon
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
ring.AddPoint(1161053.0218226474, 667456.2684348812)
ring.AddPoint(1214704.933941905, 641092.8288590391)
ring.AddPoint(1228580.428455506, 682719.3123998424)
ring.AddPoint(1218405.0658121984, 721108.1805541387)
ring.AddPoint(1179091.1646903288, 712782.8838459781)
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring)

geojson = poly.ExportToJson()
with open('test.geojson', 'w') as f:
    f.write(geojson)