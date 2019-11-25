import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import rasterio as rio
import os


#This directory
this_dir = os.path.dirname(__file__ )

#Raw data directory
input_dir = os.path.abspath(os.path.join(this_dir,'../../data/processed'))

#Processed data directory
output_dir = os.path.abspath(os.path.join(this_dir,'../../reports/figures'))

os.chdir(input_dir)
# im = Image.open('12TVK4470.tif')
# imarray = np.array(im)

lidar = rio.open('12TVK4470.tif')

plt.imshow(lidar.read(1),cmap='pink')
plt.show()
