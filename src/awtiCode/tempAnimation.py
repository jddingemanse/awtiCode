import numpy as np
from matplotlib import pyplot as plt, animation

def animateLatLonNC(dataset,lonDim='lon',latDim='lat',timeDim='time',saveAni = False):

    fig, ax = plt.subplots()
    cax = ax.pcolormesh(dataset[lonDim], dataset[latDim], dataset[0], cmap='coolwarm',vmin=280,vmax=310)
    fig.colorbar(cax)

    def animate(i):
       cax.set_array(np.array(dataset[i]).flatten())
       ax.set_title(dataset[timeDim].dt.strftime('%B %Y')[i].values)

    anim = animation.FuncAnimation(fig, animate, interval=100, frames=len(dataset.time))
    fig.show()
    return anim
    
    if saveAni==True:    
        anim.save('animation.mp4') 
