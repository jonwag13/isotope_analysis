import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


#This directory
this_dir = os.path.dirname(__file__ )

#Raw data directory
input_dir = os.path.abspath(os.path.join(this_dir,'../../data/processed'))

#Processed data directory
output_dir = os.path.abspath(os.path.join(this_dir,'../../reports/figures'))


os.chdir(input_dir)
ts = pd.read_csv('timp_space.csv')
td = pd.read_csv('timp_depth.csv')

print(ts.columns, '\n', td.columns)
print(td.head())


# # Plot ts with elev contours
# from mpl_toolkits import mplot3d
# x = ts['Longitude']
# y = ts['Latitude']
# z = ts['Elev.m']
# c = ts['d18O']
#
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# cm = plt.cm.get_cmap('RdBu_r')
# sc = ax.scatter(x,y,z,c=c,cmap=cm)
# plt.colorbar(sc)
# plt.show()

# #Stratigraphy plot
# fig,(ax1,ax2,ax3) = plt.subplots(ncols=3)
# cm = plt.cm.get_cmap('RdBu_r')
#
# x = ts['Longitude']
# y = ts['Latitude']
# c = ts['Elev.m']
# sc = ax1.scatter(x,y,c=c,cmap=cm)
#
# x = ts['Longitude']
# y = ts['Latitude']
# c = ts['d18O']
# sc = ax2.scatter(x,y,c=c,cmap=cm)
#
# x = td['Longitude']
# y = td['Latitude']
# c = td['d18O']
# sc = ax2.scatter(x,y,c=c,cmap=cm,marker='s')
#
# y = td['Depth.cm']
# x = np.ones(len(y))
# c = td['d18O']
# sc = ax3.scatter(x,y,c=c,cmap=cm,marker='s')
# ax3.invert_yaxis()
#
# plt.show()
