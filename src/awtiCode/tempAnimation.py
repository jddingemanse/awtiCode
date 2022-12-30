import numpy as np
from matplotlib import pyplot as plt, animation

def animateLatLonNC(dataset,lonDim='lon',latDim='lat',timeDim='time',saveAni = False,**kwargs):
    """
    This function returns an animation of an xarray DataSet data variable, over time, for latitudes and longitudes. It is built for temperatures in Kelvin.

    Parameters
    ----------
    dataset : xarray Dataset datavariable
        If you have a dataset with data_var air, you can insert dataset.air into this function.
    lonDim : str, optional
        The name of the longitude dimension in the dataset. The default is 'lon'.
    latDim : str, optional
        The name of the latitude dimension in the dataset. The default is 'lat'.
    timeDim : str, optional
        The name of the time dimension in the dataset. The default is 'time'.
    saveAni : boolean, optional
        If True, saves the animation on your laptop as 'animation.mp4'. The default is False.
    **kwargs : other settings
        Other settings that can be supplied are 'cmap', 'vmin' and 'vmax'.

    Returns
    -------
    anim : TYPE
        DESCRIPTION.

    """
    
    
    if 'cmap' in kwargs.keys():
        cmap = kwargs['cmap']
    else:
        cmap = 'coolwarm'
    
    if 'vmin' in kwargs.keys():
        vmin = kwargs['vmin']
    else:
        vmin = 280
    
    if 'vmax' in kwargs.keys():
        vmax = kwargs['vmax']
    else:
        vmax = 310
    
    fig, ax = plt.subplots()
    cax = ax.pcolormesh(dataset[lonDim], dataset[latDim], dataset[0], cmap=cmap,vmin=vmin,vmax=vmax)
    fig.colorbar(cax)

    def animate(i):
       cax.set_array(np.array(dataset[i]).flatten())
       ax.set_title(dataset[timeDim].dt.strftime('%B %Y')[i].values)

    anim = animation.FuncAnimation(fig, animate, interval=100, frames=len(dataset.time))
    fig.show()
    
    if saveAni==True:    
        anim.save('animation.mp4') 
    return anim