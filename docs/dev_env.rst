Development Environment
=======================

Project Setup
-------------

doc-git is developed on Python 3.4. Here are the steps of setting up this environment.

Linux
~~~~~

#. Python 3.4 and pip can be installed from package management system. For example, in Debian, you can install them via::

     sudo apt-get install python3.4 pip

#. Install virtualenv and virtualenvwrapper::

     sudo pip install viertualenv virtualenvwrapper

#. Create a new virtualenv for the project::

     mkvirtualenv negativetime -p python3.4

#. The new virtualenv should be activated automatically. If not, you can activiate it by::

     workon negativetime

#. Change into the root directory of negativetime, and install the dependencies::

     pip install -r requirements/dev.txt

#. Create the development database ``db.sqlite3`` by run this command under the negative-time folder::

     python manage.py syncdb

Windows
~~~~~~~

#. Download `Python 3.4.0`_
#. Install Python
#. Append ``C:\Python34\;C:\Python34\Scripts;`` into the environmental variable ``PATH`` (Follow this `guide`_ if you don't know how to edit the ``PATH``)
#. Download `distribute_setup.py`_
#. Run ``python distribute_setup.py`` in command prompt (cmd)
#. Download `get-pip.py`_
#. Run ``python get-pip.py`` in command prompt
#. Run ``pip install virtualenv`` in command prompt
#. Change directory into the location that you want negative-time dependencies to be installed to via ``cd`` in command prompt
#. Run ``virtualenv negativetime`` (negativetime in the command can be changed to any name of the folder that you want django to be installed to)
#. Change directory into the negative-time folder by ``cd negative-time``
#. Activate the django virtual environment by ``Scripts\activate.bat``, `(negativetime)` should be shown in the command prompt after the virtual environment is activated.
#. Change into the root directory of negativetime, and install the dependencies::

     pip install -r dev/requirements.txt

#. Create the development database ``db.sqlite3`` by run this command under the negativetime folder::

     python manage.py syncdb

IDE
---

There is a few cross-platform IDE available for python:

`Aptana`_
  An IDE derived from Eclipse for web application development
`PyCharm`_
  A great proprietary Python IDE developed by JetBrains
`PyDev`_
  An Eclipse plugin for python
`Vim`_
  A powerful text editor. `Vim as a Python IDE`_ talks about how to customize vim to a Pythoon IDE

.. Link
.. _Python 3.4.0: https://www.python.org/downloads/release/python-340/
.. _guide: http://www.computerhope.com/issues/ch000549.htm
.. _distribute_setup.py: http://python-distribute.org/distribute_setup.py
.. _get-pip.py: https://raw.github.com/pypa/pip/master/contrib/get-pip.py
.. _Aptana: http://www.aptana.com/
.. _PyCharm: http://www.jetbrains.com/pycharm/
.. _PyDev: http://pydev.org/
.. _Vim: http://www.vim.org/
.. _Vim as a Python IDE: http://unlogic.co.uk/posts/vim-python-ide.html
