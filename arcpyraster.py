import arcpy

raster = Raster('sample.tif')
#this method calculate statistics for our raster
print(raster.computeHistograms())