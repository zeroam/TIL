from osgeo import gdal

# Enable GDAL/OGR exceptions
gdal.UseExceptions()

# open dataset that does not exist
gs = gdal.Open('test.tif')
# results in python RuntimeError exception that
# 'test.tif' does not exist in the file system