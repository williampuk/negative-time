Coding Conventions
==================

This coding style guide describes a set of coding conventions that can produce readable and consistence codes.

Python
------

All python code should stricty follow :pep:`8`. For Django specific code, they should follow the `Django Coding Style`_. All functions and methods should be well documented with docstring followed the style guide in :pep:`257`. Here are some conventions in addition to :pep:`8` and `Django Coding Style`_.

- Use explicit relative imports
- Use class-based view over function-based view
- Follow this import order:

  1. Standard library import
  2. Imports from core Django
  3. Imports from third-party apps
  4. Import from the apps that in Visworld

.. note::
   This not an exhausive list of all coding conventions described in :pep:`8` and `Django Coding Style`_. Please make sure you have read through them.


JavaScript
----------

All javascript code should follow `idiomatic.js`_.

.. Link
.. _Django Coding Style: https://docs.djangoproject.com/en/1.5/internals/contributing/writing-code/coding-style/
.. _idiomatic.js: https://github.com/rwaldron/idiomatic.js/
