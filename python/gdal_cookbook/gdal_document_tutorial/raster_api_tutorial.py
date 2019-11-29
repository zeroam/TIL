import sys
import struct
import numpy
from osgeo import ogr, osr, gdal

# Opening the File
filename = 'south_korea.shp'
shp_dataset = ogr.Open(filename, gdal.GA_ReadOnly)
if not shp_dataset:
    sys.exit(f'Open failed: {filename} with GDAL'.center(30, '*'))
shp_dataset = None

filename = 'korea.tif'
tif_dataset = gdal.Open(filename, gdal.GA_ReadOnly)
if not tif_dataset:
    sys.exit(f'Open failed: {filename} with GDAL'.center(30, '*'))


# Getting Dataset Information
print('Driver: {}/{}'.format(tif_dataset.GetDriver().ShortName,
                             tif_dataset.GetDriver().LongName))
print('Size is {} x {} x {}'.format(tif_dataset.RasterXSize,
                                    tif_dataset.RasterYSize,
                                    tif_dataset.RasterCount))
print('Projection is {}'.format(tif_dataset.GetProjection()))
print('GeoTransform is {}'.format(tif_dataset.GetGeoTransform()))


# Fetching a Raster Band
band = tif_dataset.GetRasterBand(1)
print('Band Type={}'.format(gdal.GetDataTypeName(band.DataType)))

min = band.GetMinimum()
max = band.GetMaximum()
if not min or not max:
    (min, max) = band.ComputeRasterMinMax(True)
print('Min={:.3f}, Max={:.3f}'.format(min, max))

if band.GetOverviewCount() > 0:
    print('Band has {} overviews'.format(band.GetOverviewCount()))

if band.GetRasterColorTable():
    print('Band has a color table with {} entries'.format(band.GetRasterColorTable().GetCount()))


# Reading Raster Data
scanline = band.ReadRaster(xoff=0, yoff=0,
                        xsize=band.XSize, ysize=1,
                        buf_xsize=band.XSize, buf_ysize=1,
                        buf_type=gdal.GDT_Float32)

tuple_of_floats = struct.unpack('f' * band.XSize, scanline)


# Techniques for Creating Files
fileformat = 'GTiff'
driver = gdal.GetDriverByName(fileformat)
metadata = driver.GetMetadata()
if metadata.get(gdal.DCAP_CREATE) == 'YES':
    print(f'Driver {fileformat} supports Create() method.')
if metadata.get(gdal.DCAP_CREATECOPY) == 'YES':
    print(f'Driver {fileformat} supports CreateCopy() method.')


# Using CreateCopy()
dst_filename = 'create_copy.tif'
dst_ds = driver.CreateCopy(dst_filename, tif_dataset, strict=0,
                        options=['TILED=YES', 'COMPRESS=PACKBITS'])
## Once we're done, close properly the dataset
dst_ds = None
tif_dataset = None


# Using Create()
dst_filename = 'create.tif'
dst_ds = driver.Create(dst_filename, xsize=512, ysize=512,
                    bands=1, eType=gdal.GDT_Byte)
dst_ds.SetGeoTransform([444720, 30, 0, 3751320, 0, -30])
src = osr.SpatialReference()
src.SetUTM(11, 1)
src.SetWellKnownGeogCS('NAD27')
dst_ds.SetProjection(src.ExportToWkt())
raster = numpy.zeros((512, 512), dtype=numpy.uint8)
dst_ds.GetRasterBand(1).WriteArray(raster)
## Once we're done, close properly the dataset
dst_ds = None