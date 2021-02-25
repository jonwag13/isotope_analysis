import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import rasterio as rio
import utm
import os


#This directory
this_dir = os.path.dirname(__file__ )

#Raw data directory
input_dir = os.path.abspath(os.path.join(this_dir,'../../data/processed'))

#Processed data directory
output_dir = os.path.abspath(os.path.join(this_dir,'../../reports/figures'))

print('\n','*****Input Directory Files*****')
print(os.listdir(input_dir))
os.chdir(input_dir)

im = Image.open('20090709_clip.jp2')


plt.imshow(im.read(),cmap='binary_r',extent=bounds,origin='upper',vmin=195,vmax=255)

#plt.xlim(445064,446165)
#plt.ylim(4470300,4472000)
plt.show()
