import unittest
import numpy as np
import colorednoise as cn


class TestPowerlawPsdGaussian(unittest.TestCase):
    # these only test very basic functioning as of yet
    def test_powerlaw_psd_gaussian_scalar_output_shape(self):
        n = cn.powerlaw_psd_gaussian(1, 16)
        self.assertEqual(n.shape, (16,))

    def test_powerlaw_psd_gaussian_vector_output_shape(self):
        n = cn.powerlaw_psd_gaussian(1, (100,5))
        self.assertEqual(n.shape, (100,5))

    def test_powerlaw_psd_gaussian_output_finite(self):
        n = cn.powerlaw_psd_gaussian(1, 16, fmin=0.1)
        self.assertTrue(np.isfinite(n).all())

    def test_var_distribution(self):
        # test deviation from unit variance (with some margin for random errors)
        size = (100, 2**16)
        fmin = 0
        
        for exponent in [.5, 1, 2]:
            y = cn.powerlaw_psd_gaussian(exponent, size, fmin=fmin)
            ystd = y.std(axis=-1)
            var_in = (abs(1 - ystd) < 3 * ystd.std()).mean() # var within 3 sigma
            self.assertTrue(var_in > 0.95) # should even be > 0.99 since distr. normal
        
    def test_small_sample_var(self):
        # test deviation from unit variance for short time series with odd and even length
        for nsamples in [10,11]:
            ystd = cn.powerlaw_psd_gaussian(0, (500, 500, nsamples)).std(axis=-1)
            assert(abs(1 - ystd) < 3 * ystd.std()).mean() > 0.95
        
    def test_slope_distribution(self):
        # test deviation from scaling by fitting log-binned spectra
        size = (100, 2**16)
        fmin = 0
        
        for exponent in [.5, 1, 2]:
            y = cn.powerlaw_psd_gaussian(exponent, size, fmin=fmin)
            yfft = np.fft.fft(y)
            f = np.fft.fftfreq(y.shape[-1])
            m = f > 0 # mask
            fit, fcov = np.polyfit(
                np.log10(f[m]), np.log10(abs(yfft[...,m].T**2)), 1, cov=True
            )
        
            slope_in = (exponent + fit[0] < 3 * np.sqrt(fcov[0,0])).mean()
            self.assertTrue(slope_in > 0.95)
