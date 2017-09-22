colorednoise.py
===============

Generate gaussian distributed noise with a power-law spectrum with arbitrary 
exponents. An exponent of two corresponds to brownian noise. Smaller exponents 
yield long-range correlations, i.e. pink noise for an exponent of 1 (also 
called 1/f noise or flicker noise).

Based on the algorithm in 
    Timmer, J. and Koenig, M.:
    On generating power law noise. 
    Astron. Astrophys. 300, 707-710 (1995)
    
Further reading: 
`Colors of noise on Wikipedia <//en.wikipedia.org/wiki/Colors_of_noise>`_

----

Installation: 
	``pip install .``
	
Dependencies:
	python 2.7
	numpy