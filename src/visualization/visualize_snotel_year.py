import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
from scipy import stats
import os
import matplotlib.dates as mdates
from datetime import datetime

months = mdates.MonthLocator()
days = mdates.DayLocator(15)
myFmt = mdates.DateFormatter('%b %d, %Y')

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

sites = {}
for file in os.listdir(input_dir):
    os.chdir(input_dir)
    if 'snotel' in file:
        df = pd.read_csv(file)
        df = df.set_index(pd.DatetimeIndex(df['Date']))
        df['x'] = np.arange(len(df))
        sites[file.strip('snotel_.csv')] = df
        print(df.columns)
        df = df.sort_index()

lw = 2
fig,(ax1,ax2,ax3) = plt.subplots(figsize=(10,10),nrows=3,sharex=True)

data_subset = sites['820']['10-05-2011':'09-25-2012']
pit1_date =datetime.strptime('06-30-2012','%m-%d-%Y')
pit2_date =datetime.strptime('08-16-2012','%m-%d-%Y')
pit3_date =datetime.strptime('08-16-2012','%m-%d-%Y')

#Precip
ax1.bar(data_subset.index,data_subset['PREC.I-1 (in) '].diff(),width=0.5,color='k',linewidth=lw)

ax1.vlines(pit1_date,0,0.6,colors='blue')
ax1.text(pit1_date,0.35,'Pit 1',color='blue')

ax1.vlines(pit2_date,0,0.6,colors='blue')
ax1.text(pit2_date,0.35,'Pit 2,3',color='blue')

ax1.set_ylabel('PREC.I-1 (in)')
ax1.set_ylim(0,0.6)
ax1.grid()


#Snow Depth
ax2.plot(data_subset.index,data_subset['SNWD.I-1 (in) '],c='k',linewidth=lw)

ax2.vlines(pit1_date,0,60,colors='blue')
ax2.text(pit1_date,32,'Pit 1',color='blue')

ax2.vlines(pit2_date,0,60,colors='blue')
ax2.text(pit2_date,32,'Pit 2,3',color='blue')

ax2.set_ylabel('SNWD.I-1 (in)')
ax2.set_ylim(0,60)
ax2.grid()

#Air Temp
ax3.plot(data_subset.index,data_subset['TAVG.D-1 (degC) '],c='k',linewidth=lw)
ax3.plot(data_subset.index,data_subset['TMAX.D-1 (degC) '],c='k',linestyle='--',linewidth=lw)
ax3.plot(data_subset.index,data_subset['TMIN.D-1 (degC) '],c='k',linestyle='--',linewidth=lw)


ax3.vlines(pit1_date,-20,30,colors='blue')
ax3.text(pit1_date,-5,'Pit 1',color='blue')

ax3.vlines(pit2_date,-20,30,colors='blue')
ax3.text(pit2_date,-5,'Pit 2,3',color='blue')

#Temp 0 line
ax3.hlines(0,data_subset.index.min(),data_subset.index.max(),colors='r',linewidth=lw,zorder=0,linestyle=':')
ax3.xaxis.set_major_locator(months)
ax3.xaxis.set_major_formatter(myFmt)
ax3.xaxis.set_minor_locator(days)

ax3.set_ylabel('TAVG.D-1 (degC)')
ax3.set_ylim(-20,30)
ax3.grid()

fig.autofmt_xdate(rotation=20)
plt.tight_layout()

os.chdir(output_dir)
plt.savefig('820_climate_2012.png')
