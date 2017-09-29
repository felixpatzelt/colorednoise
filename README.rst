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

	- Python >= 2.7 or >= 3.6
	- NumPy
	
Other Python versions were not tested, but are likely to work.


Example
-------

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
	
