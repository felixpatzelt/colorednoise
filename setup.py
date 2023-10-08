from setuptools import setup

setup(
    name='colorednoise',
    version='2.2.0',
    description='Generate Gaussian (1/f)**beta noise (e.g. pink noise)',
    long_description="""Generate Gaussian distributed noise with a power law spectrum.
        Based on the algorithm in 
            Timmer, J. and Koenig, M.:
            On generating power law noise. 
            Astron. Astrophys. 300, 707-710 (1995)
    """,
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Intended Audience :: Education',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3.10',
      'Topic :: Scientific/Engineering',
      'Topic :: Software Development :: Libraries',
      'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='1/f flicker power-law correlated colored noise generator',
    url='http://github.com/felixpatzelt/colorednoise',
    download_url=(
      'https://github.com/felixpatzelt/colorednoise/archive/2.2.0.tar.gz'
    ),
    author='Felix Patzelt',
    author_email='felix@neuro.uni-bremen.de',
    license='MIT',
    py_modules=['colorednoise'],
    install_requires=[
        'numpy>=1.17.0',
    ],
    python_requires='>=3',
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
)