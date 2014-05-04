Documentation
=============

To generate documentation, follow these steps.

#. Create a virtualenv for documentation::

     mkvirtualenv negativetime-doc -p python3.4

#. Work on the new virtualenv::

     workon negativetime-doc

#. Intall the dependencies::

     pip install -r requirements/docs.rst

#. Change Make the documentation::

     cd docs
     make html

#. The documentation are generated in docs/_build/html/
