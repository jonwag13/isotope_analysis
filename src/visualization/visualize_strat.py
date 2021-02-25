import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

mpl.rcParams['font.size'] = 14
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['figure.titlesize'] = 'medium'
mpl.rcParams['grid.color'] = 'k'
mpl.rcParams['grid.linestyle'] = ':'
mpl.rcParams['grid.linewidth'] = 0.5


#This directory
this_dir = os.path.dirname(__file__ )

#Raw data directory
input_dir = os.path.abspath(os.path.join(this_dir,'../../data/processed'))

#Processed data directory
output_dir = os.path.abspath(os.path.join(this_dir,'../../reports/figures'))


os.chdir(input_dir)
ts = pd.read_csv('timp_space.csv')
td = pd.read_csv('timp_depth.csv')
td['Date'] = pd.to_datetime(td['Date'],format='%d%m%y').dt.date

print(ts.columns, '\n', td.columns)


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

var = 'dD'
min = [td[var].min(),ts[var].min()]
vmin = sorted(min)[0]
max = [td[var].max(),ts[var].max()]
vmax = sorted(max)[1]
print(vmin,vmax)

# #Spatial plot
# fig,(ax1) = plt.subplots(ncols=1)
# cm = plt.cm.get_cmap('RdBu_r')
#
# #Lat, lon, var
# x = ts['Longitude']
# y = ts['Latitude']
# c = ts[var]
# sc = ax1.scatter(x,y,c=c,cmap=cm,vmin=vmin,vmax=vmax)
#
# #Lat, lon, var
# x = td['Longitude'].where(td['Depth.cm'] == 0)
# y = td['Latitude']
# c = td[var]
# sc = ax1.scatter(x,y,c=c,cmap=cm,marker='s',vmin=vmin,vmax=vmax)
# plt.colorbar(sc)
# plt.show()


var = 'ug.L'
min = [td[var].min()]
vmin = sorted(min)[0]
max = [td[var].max()]
vmax = sorted(max)[0]

#Strat Plots
fig,(ax1) = plt.subplots(figsize=(3.3,10),ncols=1,sharex=True,sharey=True)

pit_subset = td.where(td['Pit'] == 1).sort_values('Depth.cm')
y = pit_subset['Depth.cm']
x = pit_subset[var]
ax1.hlines(0,vmin,vmax,colors='r',linestyle='--',linewidth=3,zorder=0)
ax1.plot(x,y,label=1,linewidth=3,c='k')
ax1.scatter(x,y,s=55,c='k')
ax1.invert_yaxis()
ax1.set_xlim(-5,205)
ax1.set_ylim(160,-5)
ax1.set_title('Pit 1: ' + td['Date'].where(td['Pit'] == 1).dropna().unique()[0].strftime('%Y-%m-%d'))
ax1.set_ylabel('Depth (cm)')
ax1.set_xlabel(var)
ax1.grid()

# pit_subset = td.where(td['Pit'] == 2).sort_values('Depth.cm')
# y = pit_subset['Depth.cm']
# x = pit_subset[var]
# ax2.hlines(0,vmin,vmax,colors='r',linestyle='--',linewidth=3,zorder=0)
# ax2.plot(x,y,label=2,linewidth=3,c='k')
# ax2.scatter(x,y,s=55,c='k')
# ax2.invert_yaxis()
# ax2.set_xlim(vmin,vmax)
# ax2.set_ylim(160,0)
# ax2.set_title('Pit 2: ' + td['Date'].where(td['Pit'] == 2).dropna().unique()[0].strftime('%Y-%m-%d'))
# ax2.set_xlabel(var + ' ‰')
# ax2.grid()
#
# pit_subset = td.where(td['Pit'] == 3).sort_values('Depth.cm')
# y = pit_subset['Depth.cm']
# x = pit_subset[var]
# ax3.hlines(0,vmin,vmax,colors='r',linestyle='--',linewidth=3,zorder=0)
#
# ax3.plot(x,y,label=3,linewidth=3,c='k')
# ax3.scatter(x,y,s=55,c='k')
# ax3.invert_yaxis()
# ax3.set_xlim(vmin,vmax)
# ax3.set_ylim(160,-5)
# ax3.set_title('Pit 3: ' + td['Date'].where(td['Pit'] == 3).dropna().unique()[0].strftime('%Y-%m-%d'))
# ax3.grid()

os.chdir(output_dir)
plt.tight_layout()
plt.savefig(var+'_strat.png')
