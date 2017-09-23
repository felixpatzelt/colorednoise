import unittest
import numpy as np
import colorednoise as cn

class TestPowerlawPsdGaussian(unittest.TestCase):
    # these only test very basic functioning as of yet
    def test_powerlaw_psd_gaussian_output_shape(self):
        n = cn.powerlaw_psd_gaussian(1, 16)
        self.assertEqual(n.shape, (16,))

    def test_powerlaw_psd_gaussian_output_finite(self):
        n = cn.powerlaw_psd_gaussian(1, 16)
        self.assertTrue(np.isfinite(n).all())
