import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
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



def trendline(df,var):
    df = df[[var,'x']]
    df = df.dropna()
    fit = np.polyfit(df['x'], df[var], 1)
    fit_fn = np.poly1d(fit)

    trend_line = fit_fn(df['x'])
    index = df.index
    return index,trend_line


print(sites.keys())

fig,ax = plt.subplots(1,1,figsize=(12,6))

var = 'TMIN.D-1 (degC) '
site_num = '820'
index,trend_line = trendline(sites[site_num],var)
ax.plot(sites[site_num].index, sites[site_num][var],label='Site: '+site_num,c='k')
ax.plot(index, trend_line,label='Trend Line',c='r',linewidth=3)

ax.set_ylabel(var)
ax.set_xlabel('Date')
ax.legend()
ax.grid()

os.chdir(output_dir)
plt.tight_layout()
plt.savefig('trend_'+site_num+'_'+var+'.png',c='k')
