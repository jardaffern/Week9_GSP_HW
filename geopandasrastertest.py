import matplotlib.pyplot as plt
#import pandas as pd
#import geopandas as gpd
import rasterio as rast
#import numpy as np
from scipy.ndimage import gaussian_filter
from rasterio.plot import show

with rast.open("sample.tif") as raster:
    #Code from Geopandas, transform rasterio plot to real world coords, and display Reds from imagery
    fig, ax = plt.subplots()
    extent = [raster.bounds[0], raster.bounds[2], raster.bounds[1], raster.bounds[3]]
    ax = rast.plot.show(raster, extent=extent, ax=ax, cmap="Reds")
    plt.show()

    # Gaussian blur with different standard deviations
    band1 = raster.read(1) #TODO: Learn best practice for implementing this when you don't know how many bands there are
    blurred_more = gaussian_filter(band1, sigma=5)  # Larger sigma for a more blurred version
    blurred_less = gaussian_filter(band1, sigma=2)  # Smaller sigma for less blurred version

    # Apply the DoG filter
    dog = blurred_less - blurred_more

    plt.imshow(dog, interpolation='nearest')
    plt.show()