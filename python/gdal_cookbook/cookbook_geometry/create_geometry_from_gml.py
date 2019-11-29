from osgeo import ogr

gml = """<gml:Point xmlns:gml="http://www.opengis.net/gml"><gml:coordinates>108420.33,753808.59</gml:coordinates></gml:Point>"""
point = ogr.CreateGeometryFromGML(gml)
print(f'{point.GetX()},{point.GetY()}')