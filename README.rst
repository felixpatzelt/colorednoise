colorednoise.py
===============

Generate Gaussian distributed noise with a power law spectrum with arbitrary 
exponents. 

An exponent of two corresponds to brownian noise. Smaller exponents 
yield long-range correlations, i.e. pink noise for an exponent of 1 (also 
called 1/f noise or flicker noise).

Based on the algorithm in:
	
    Timmer, J. and Koenig, M.:
    On generating power law noise. 
    Astron. Astrophys. 300, 707-710 (1995)
    
Further reading: 
`Colors of noise on Wikipedia <//en.wikipedia.org/wiki/Colors_of_noise>`_


Installation
------------

	pip install colorednoise
	
	
Dependencies
------------

	- Python >= 3.6.15
	- NumPy >= 1.17.0
	
Older Python 3 versions were not tested, but are likely to work.
For Python 2 please use colorednoise version 1.x.


Examples
--------

.. code:: python

	import colorednoise as cn
	beta = 1 # the exponent
	samples = 2**18 # number of samples to generate
	y = cn.powerlaw_psd_gaussian(beta, samples)
	
	# optionally plot the Power Spectral Density with Matplotlib
	#from matplotlib import mlab
	#from matplotlib import pylab as plt
	#s, f = mlab.psd(y, NFFT=2**13)
	#plt.loglog(f,s)
	#plt.grid(True)
	#plt.show()
	
	
.. code:: python

	# generate several time series of independent indentically distributed variables 
	# repeat the simulation of each variable multiple times
	import colorednoise as cn
	n_repeats   = 10   # repeat simulatons
	n_variables = 5    # independent variables in each simulation
	timesteps   = 1000 # number of timesteps for each variable
	y = cn.powerlaw_psd_gaussian(1, (n_repeats, n_variables, timesteps))
	
	# the expected variance of for each variable is 1, but each realisation is different
	print(y.std(axis=-1))
	
.. code:: python

	# generate a broken power law spectrum: white below a frequency of 
	import colorednoise as cn
	y = cn.powerlaw_psd_gaussian(1, 10**5, fmin=.05)
	s, f = mlab.psd(y, NFFT=2**9)
	#plt.loglog(f,s)
	#plt.grid(True)
	#plt.show()
