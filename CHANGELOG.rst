Changelog
=========

:Version: 2.2.0 of 2023-10-08
Added type annotations (thanks to @charlesincharge for the initiative on an initial PR).
Adapted type checking of size parameter for compatibility with mypy.  

:Version: 2.1.0 of 2022-04-16
Fix by @onnoeberhard for too-small dc-component: When cumulating the generated noise,
the displacement would grow too slowly in the long limit.
Test that would have discovered the above issue.
Other tests are now deterministic.


:Version: 2.0.0 of 2022-04-16

Allow for control over random number generator state by adding optional random_state
argument thanks to contributions from i-aki-y.
Drop Python 2.7 support to use of NumPy's recommended default_rng constructor.

:Version: 1.2.0 of 2022-03-13

Improve doc strings based on user questions.
Check that fmin parameter is in the right range.


:Version: 1.1.1 of 2019-02-08

Use numpy's sum instead of python's (thanks to RuABraun).


:Version: 1.1 of 2019-02-08

Allow for generation of arrays of time series thanks to contributions from 
Alex Spaeth. The second positional argument "samples" was renamed to "size" to 
reflect this. This change is backwards compatible unless "samples" was used as 
a keyword argument.


:Version: 1.0 of 2017-09-24

Version bump after testing upload to GitHub and PyPI, as well as pip installation
and output correctness under Python 2.7 and 3.6.


:Version: 1.0-rc.1 of 2017-09-23

Refactoring: moved powerlaw_psd_gaussian into the present pure python module to 
release it to the public in pip-installable form.


:Version: [unreleased] of 2014-04-07

powerlaw_psd_gaussian was part of a personal collection of random number
generation algorithms for research written in python and c.
