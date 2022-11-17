# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:43:48 2022

@author: jandirk
"""

import xarray as xr
import pandas as pd
ds=xr.open_dataset('data/m5_temperatures.nc')

latmin,latmax,lonmin,lonmax=3,16,32,48
dsET = ds.air[:,(ds.lat>latmin)&(ds.lat<latmax),(ds.lon>lonmin)&(ds.lon<lonmax)]

yearAvg = dsET.groupby(group=dsET.time.dt.year).mean()


from matplotlib import pyplot as plt, animation
%matplotlib

def animateLatLonNC(dataset,lonDim='lon',latDim='lat',timeDim='time',saveAni = False):

    fig, ax = plt.subplots()
    cax = ax.pcolormesh(dataset[lonDim], dataset[latDim], dataset[0], cmap='coolwarm',vmin=280,vmax=310)
    fig.colorbar(cax)

    def animate(i):
       cax.set_array(np.array(dataset[i]).flatten())
       ax.set_title(dataset[timeDim].dt.strftime('%B %Y')[i].values)

    anim = animation.FuncAnimation(fig, animate, interval=100, frames=len(dataset.time))
    return fig
    
    if saveAni==True:    
        anim.save('animation.mp4')
    