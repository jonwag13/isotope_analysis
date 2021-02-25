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

def gwl(x):
    y = 8 * x + 10
    return y

os.chdir(input_dir)
ts = pd.read_csv('timp_space.csv')
td = pd.read_csv('timp_depth.csv')
td['Date'] = pd.to_datetime(td['Date'],format='%d%m%y').dt.date

ts['dex'] = ts['dD'] - 8 * ts['d18O']
td['dex'] = td['dD'] - 8 * td['d18O']

print(ts.columns, '\n', td.columns)


fig = plt.figure(figsize=(10,10))

plt.scatter(ts['d18O'].where(ts['Lake'] == True),ts['dD'].where(ts['Lake'] == True),label='lake water',c='#233ee0')

plt.scatter(ts['d18O'].where(ts['Lake'] != True),ts['dD'].where(ts['Lake'] != True),label='snow surface',c='#24c728')

plt.scatter(td['d18O'].where(td['Pit'] == 1),td['dD'].where(td['Pit'] == 1),label='pit 1',c='#e69320')

plt.scatter(td['d18O'].where(td['Pit'] == 2),td['dD'].where(td['Pit'] == 2),label='pit 2',c='#8924c7')

plt.scatter(td['d18O'].where(td['Pit'] == 3),td['dD'].where(td['Pit'] == 3),label='pit 3',c='#ff00e8')

x = np.arange(-20,-10)
y = gwl(x)
plt.plot(x,y,label='GMWL',c='k',zorder=0)


plt.xlabel('d18O ‰')
plt.ylabel('dD ‰')
plt.legend()
plt.grid()

os.chdir(output_dir)
plt.savefig('gmwl_plot.png')
