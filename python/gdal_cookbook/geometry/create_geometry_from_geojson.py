from osgeo import ogr

geojson = """{"type":"Point", "coordinates":[108420.33,753808.59]}"""
point = ogr.CreateGeometryFromJson(geojson)
print(f'{point.GetX()},{point.GetY()}')