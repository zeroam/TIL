import sys
try:
    from osgeo import ogr, osr, gdal
except:
    sys.exit('ERROR: cannot find GDAL/OGR modules')

# example GDAL error handler function
def gdal_error_handler(err_class, err_num, err_msg):
    errtype = {
        gdal.CE_None: 'None',
        gdal.CE_Debug: 'Debug',
        gdal.CE_Warning: 'Warning',
        gdal.CE_Failure: 'Failure',
        gdal.CE_Fatal: 'Fatal',
    }
    err_msg = err_msg.replace('\n', ' ')
    err_class = errtype.get(err_class, 'None')
    print('Error Number: %s' % (err_num))
    print('Error Type: %s' % (err_class))
    print('Error Message: %s' % (err_msg))


if __name__ == '__main__':
    # install error handler
    gdal.PushErrorHandler(gdal_error_handler)

    # Raise a dummy error
    gdal.Error(gdal.CE_Warning, 2, 'test error')
    gdal.Error(3, 2, 'test error')

    # uninstall error handler
    gdal.PopErrorHandler()