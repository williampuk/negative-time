Version Control System
======================

:term:`Version Control System` (VCS) is a necessity for any software development project. :term:`Git` is a powerful and popular :term:`VCS`.
doc-git use :term:`Git` to manage the source code. The source code of doc-git is host on `Github`_.

Getting Started with Git
------------------------

Linux
~~~~~

#. Git should be available in the packet management system. For example, you can install Git in Debian by this command::

     sudo apt-get install git

#. Configure the user name and email::

     git config --global user.name {Your Name}
     git config --global user.email {Your Email}

#. Git configuration for colored output::

     git config --global color.diff auto
     git config --global color.status auto
     git config --global color.branch auto
     git config --global color.log auto

#. Some useful alias::

     git config --global br branch
     git config --global cm "commit -m"
     git config --global co checkout
     git config --global st "status -sb"
     git config --global graph "log --graph --all --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(bold white)— %an%C(reset)%C(bold yellow)%d%C(reset)' --abbrev-commit --date=relative"

#. Import SSH key into `Github`_

   #. Open a terminal in your local system.
   #. Enter ssh-keygen at the command line.
   #. The command prompts you for a file to save the key in. If the .ssh directory doesn't exist, the system creates one for you. Accept the default location.Enter and re-enter a passphrase when prompted.
   #. The command prompts your for a passphrase, keep the passphrase empty.
   #. The command creates your default identity with its public and private keys.
   #. Go to the profile page of `Github`_ (Edit your profile -> SSH keys)
   #. In "Add SSH key", paste the public key ``~/.ssh/id_rsa.pub`` to the text box and click "Add SSH key"

#. There are many merge tools available on linux, e.g. vimdiff, kdiff3 and meld. To configure the difftool and mergetool::

     git config --global diff.tool {your tool}
     git config --global merge.tool {your tool}

#. Clone doc-git repository::

     git clone git@github.com:williampuk/negative-time.git

Windows
~~~~~~~

#. Download and Install `Git Extensions`_
#. During install Git Extensions

   #. Select install msysgit and kdiff3
   #. Choose Putty as your ssh client

#. Open `Git Extensions`_, it will ask you to fill in your name and email, please fill in the email of `Github`_ your and your name
#. Import SSH key into `Github`_

   #. In `Git Extensions`_, click "Remote -> PuTTY -> Generate / import key”
   #. Click "Generate"
   #. Copy the public key on the top
   #. Go to the profile page of `Github`_ (Edit your profile -> SSH keys)
   #. In "Add SSH key", paste the public key ``~/.ssh/id_rsa.pub`` to the text box and click "Add SSH key"
   #. Back to putty, click "Save private key" to save the private key

#. Setup Pagent

   #. In `Git Extensions`_, click "Remote -> PuTTY -> Start authentication agent"
   #. Pageant will be launched
   #. add the saved private key file to pageant

#. Setup difftool and mergetool

   #. The diff tool came with `Git Extensions`_ is kdiff3. You may install other diff tool (e.g. `DiffMerge`_, `WinMerge`_).
   #. The difftool and mergetool can be configured in `Git Extensions`_ "Settings -> Settings -> Global Settings"

#. Clone doc-git repository

   #. Click "clone repository"
   #. Fill in "Repository to be clone" as "git@github.com:williampuk/negative-time.git"
   #. Select "Destination" as a place your want to download the project to

Git Workflow
------------

doc-git follows the Git branching model mentioned in Vincent Driessen's `A successful Git branching model`_. It consits of 5 types of branch:

- master
- develop
- feature branches
- release branches
- hotfix branches

doc-git uses `Shared Repository Model`_ for collaborative development. Pull requests are heavily used in the workflow. The use of pull request follows the David Winterbottom's `Effective pull requests and other good practices for teams using github`_.

.. Link
.. _Github: https://www.github.com/
.. _Git Extensions: http://code.google.com/p/gitextensions/
.. _DiffMerge: http://www.sourcegear.com/diffmerge/
.. _WinMerge: http://winmerge.org/
.. _Shared Repository Model: https://help.github.com/articles/using-pull-requests#shared-repository-model
.. _A successful Git branching model: http://nvie.com/posts/a-successful-git-branching-model/
.. _Effective pull requests and other good practices for teams using github: http://codeinthehole.com/writing/pull-requests-and-other-good-practices-for-teams-using-github/
