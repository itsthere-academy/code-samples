# Simple [SpicePy](https://github.com/AndrewAnnex/SpiceyPy) demo

Draw the Earth the Moon orbits for 2021.

The code is intended to run in [VSCode Interactive Mode](https://code.visualstudio.com/docs/python/jupyter-support-py), thus the funny comment lines:

```
#%%
```

Each of such lines indicate a Jupyter cell, so the code can be executed in steps. Hopefully this makes it easier to experiment with and let you explore the data.

## Running the code
The code requires following pip packages to be installed:
* setuptools
* wheel
* numpy
* pandas
* spiceypy
* notebook
* plotly

You also need to download 2 files - so called 'kernels' from SPICE website. Create "data" directory and the put the files there:
* de430.bsp - planets ephemerids from [here](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/)
* naif0012.tls - leap seconds from [here](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/)

Have Fun!