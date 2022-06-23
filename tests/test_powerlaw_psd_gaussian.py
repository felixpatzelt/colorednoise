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
        rng = np.random.default_rng(1)
        
        for exponent in [.5, 1, 2]:
            y = cn.powerlaw_psd_gaussian(exponent, size, fmin=fmin, random_state=rng)
            ystd = y.std(axis=-1)
            var_in = (abs(1 - ystd) < 3 * ystd.std()).mean() # var within 3 sigma
            self.assertTrue(var_in > 0.95) # should even be > 0.99 since distr. normal
        
    def test_small_sample_var(self):
        # test deviation from unit variance for short time series with odd and even length
        rng = np.random.default_rng(1)
        for nsamples in [10,11]:
            ystd = cn.powerlaw_psd_gaussian(
                0, (500, 500, nsamples), random_state=rng
            ).std(axis=-1)
            assert(abs(1 - ystd) < 3 * ystd.std()).mean() > 0.95
        
    def test_slope_distribution(self):
        # test deviation from scaling by fitting log-binned spectra
        size = (100, 2**16)
        fmin = 0
        rng = np.random.default_rng(1)
        
        for exponent in [.5, 1, 2]:
            y = cn.powerlaw_psd_gaussian(exponent, size, fmin=fmin, random_state=rng)
            yfft = np.fft.fft(y)
            f = np.fft.fftfreq(y.shape[-1])
            m = f > 0 # mask
            fit, fcov = np.polyfit(
                np.log10(f[m]), np.log10(abs(yfft[...,m].T**2)), 1, cov=True
            )
        
            slope_in = (exponent + fit[0] < 3 * np.sqrt(fcov[0,0])).mean()
            self.assertTrue(slope_in > 0.95)
            
    def test_cumulative_scaling(self):
        # check that mean squared displacement for cumulated white noise
        # scales like number of steps as expected for diffusion in 1 dimension
        
        n_repeats = 1000
        n_steps   = 100
        rng = np.random.default_rng(1)

        y  = cn.powerlaw_psd_gaussian(0, (n_repeats, n_steps), random_state=rng)

        mean_squared_displacement = (y.sum(axis=-1)**2).mean(axis=0)
        standard_error            = (y.sum(axis=-1)**2).std(axis=0) / np.sqrt(n_repeats)
        
        assert np.abs(n_steps - mean_squared_displacement) < 3 * standard_error

    def test_random_state_type(self):
        exp = 1
        n = 5
        seed = 1

        good_random_states = [
            np.random.default_rng(seed), 
            np.random.RandomState(seed), 
            int(seed), 
            np.int32(1),
            True, 
            None
        ]
        for random_state in good_random_states:
            cn.powerlaw_psd_gaussian(exp, n, random_state=random_state)

        bad_random_states = ["1", 0.15, [1]]
        for random_state in bad_random_states:
            self.assertRaises(
                ValueError, 
                cn.powerlaw_psd_gaussian, 
                exp, 
                n, 
                random_state=random_state
            )


    def test_random_state_reproducibility(self):
        exp = 1
        n = 5
        seed = 1

        rs1 = np.random.default_rng(seed)
        rs2 = np.random.default_rng(seed)

        y1 = cn.powerlaw_psd_gaussian(exp, n, random_state=rs1)
        np.random.seed(123)
        y2 = cn.powerlaw_psd_gaussian(exp, n, random_state=rs2)

        np.testing.assert_array_equal(y1, y2)
