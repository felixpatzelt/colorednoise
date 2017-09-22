import unittest
import colorednoise as cn

class TestPowerlawPsdGaussian(unittest.TestCase):
    def test_powerlaw_psd_gaussian_output_shape(self):
        n = cn.powerlaw_psd_gaussian(1, 100)
        self.assertEqual(n.shape, (100,))
