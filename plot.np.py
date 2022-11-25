# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 04:54:11 2022

@author: user
"""

import pandas as pd
import numpy as np

Non_dim=pd.read_csv('data/Non_dim.csv')

Non_dim.set_axis(Non_dim.Month,0)
import matplotlib.pyplot as plt
%matplotlib
import numpy as np

fig,ax = plt.subplots()
ax.set_title('Homogeneity Test of Selected Rainfall Stations',c='r',size=10,fontstyle='italic',weight='extra bold')
ax.set_ylabel('Non-dimentsionalvalue')
ax.set_xlabel('Month')
ax.set_xticks(np.arange(0,12,1))
ax.set_xticks(np.arange(0.5,11,1),minor=True)
ax.set_xticklabels(Non_dim.Month)
ax.plot(Non_dim.ArbaMinch,c='k',label='ArbaMinch',ls='--')
ax.plot(Non_dim.Chinch,c='b',label='Chinch',lw=1,ls='-',marker='+',markersize=20)
ax.plot(Non_dim.Zigit,c='r',label='Zigit',lw=1,ls='-.',marker='D',markersize=10)
fig.legend()
fig.savefig('output/figNon_dim.jpg')

fig,ax=plt.subplots()
ax.scatter(Non_dim.Month,Non_dim.ArbaMinch,c=Non_dim.Chinch,cmap='coolwarm',vmin=60,vmax=150)
ax.set_xlabel('Month')
ax.set_ylabel('Non-dimentsionalvalue')
ax.set_title('Color variation shows chnincha variation')

from matplotlib import cm
cbar = fig.colorbar(cm.ScalarMappable(cmap='coolwarm'))

cbar.set_ticks(np.linspace(0,1,3))
cbar.set_ticklabels(['<150','200','>250'])

fig,ax=plt.subplots()
ax.hist(Non_dim.Chinch)






