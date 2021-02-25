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

fig,(ax1,ax2) = plt.subplots(ncols=2,sharex=True,sharey=True)

im = rio.open('n_4011135_se_12_1_20090709_20091001.jp2')
print(im.indexes)
print(im.crs.wkt)
print(im.bounds)
print('min,min:',im.transform * (0,0))
print('max,max:',im.transform * (im.width,im.height))
bounds = [im.bounds.left,im.bounds.right,im.bounds.bottom,im.bounds.top]
ax1.imshow(im.read(1),cmap='binary_r',extent=bounds,origin='upper',vmin=195,vmax=255)


im = rio.open('m_4011135_se_12_1_20110806_20111011.jp2')
print(im.indexes)
print(im.crs.wkt)
print(im.bounds)
print('min,min:',im.transform * (0,0))
print('max,max:',im.transform * (im.width,im.height))
bounds = [im.bounds.left,im.bounds.right,im.bounds.bottom,im.bounds.top]
ax2.imshow(im.read(1),cmap='binary_r',extent=bounds,origin='upper',vmin=195,vmax=255)

os.chdir(input_dir)
ts = pd.read_csv('timp_space.csv')
lon = ts['Longitude']
lat = ts['Latitude']
ts['utm'] = list(map(lambda lat,lon:utm.from_latlon(lat,lon), lat, lon))

ts['northing'] = [i[0] for i in ts['utm']]
ts['easting'] = [i[1] for i in ts['utm']]


print(ts.head)

ax1.set_xlim(445064,446165)
ax1.set_ylim(4470300,4472000)
plt.show()
