"""Generate colored noise."""

from numpy import concatenate, real, std, abs
from numpy.fft import ifft, fftfreq
from numpy.random import normal

def powerlaw_psd_gaussian(exponent, samples, fmin=0):
    """Gaussian (1/f)**beta noise.
    
    Based on the algorithm in:
    Timmer, J. and Koenig, M.: 
    On generating power law noise. 
    Astron. Astrophys. 300, 707-710 (1995)
    
    Normalised to unit variance
    
    Parameters:
    -----------
    
    exponent : float
        The power-spectrum of the generated noise is proportional to
        
        S(f) = (1 / f)**beta
        flicker / pink noise:   exponent beta = 1
        brown noise:            exponent beta = 2
        
        Furthermore, the autocorrelation decays proportional to lag**-gamma 
        with gamma = 1 - beta for 0 < beta < 1.
        There may be finite-size issues for beta close to one.
    
    samples : int
        number of samples to generate
    
    fmin : float, optional
        Low-frequency cutoff.
        Default: 0 corresponds to original paper. It is not actually
        zero, but 1/samples.
        
    Returns
    -------
    out : array
        The samples


    Examples:
    ---------

    # generate 1/f noise == pink noise == flicker noise
    >>> import colorednoise as cn
    >>> y = cn.powerlaw_psd_gaussian(1, 5)
    """
    
    # frequencies (we asume a sample rate of one)
    f = fftfreq(samples)
    
    # scaling factor for all frequencies 
    ## though the fft for real signals is symmetric,
    ## the array with the results is not - take neg. half!
    s_scale = abs(concatenate([f[f<0], [f[-1]]]))
    ## low frequency cutoff?!?
    if fmin:
        ix = sum(s_scale>fmin)
        if ix < len(f):
            s_scale[ix:] = s_scale[ix]
    s_scale = s_scale**(-exponent/2.)
    
    # scale random power + phase
    sr = s_scale * normal(size=len(s_scale))
    si = s_scale * normal(size=len(s_scale))
    if not (samples % 2): si[0] = si[0].real

    s = sr + 1J * si
    # this is complicated... because for odd sample numbers,
    ## there is one less positive freq than for even sample numbers
    s = concatenate([s[1-(samples % 2):][::-1], s[:-1].conj()])

    # time series
    y = ifft(s).real

    return y / std(y)

