.. cv-templating documentation master file, created by
   sphinx-quickstart on Tue Apr 11 13:48:44 2017.

cv-templating documentation
===========================

**cv-templating** is a tool for automatic generation of curriculum vitae
from data. It is a report generator using ``jinja2``.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   tutorial
   requirements
   genindex

Motivation
----------

Update a `Europass CV
online <https://europass.cedefop.europa.eu/editors/en/cv/compose>`_, or
made it for the first time, is error prone and time-consuming if you
have several entries, or worst, if you need to put all your *resume* in
another format (for instance in HTML) or in another language.

Solution
--------

We can manage the generation of the CV quickly from data conveniently
stored as text files using templates based in
`jinja2 <http://jinja.pocoo.org/docs/dev/>`__.

In this solution, I use data stored in plain text files, facilitating
the utilisation of any tool for modifying them. Also, it is very
convenient for putting your CV information under control version.

You can see two generated examples: `Someone.html`_ and
`Someone.pdf`_.

.. note::

      If you only need your *curriculum vitae* in only one
      language and only using one format (for instance the Europass format
      using latex), then probably is better that you edit a new document using
      the document class *europasscv* provided by tex distributions or getting
      the last version from `Github
      repo <https://github.com/gmazzamuto/europasscv>`_.

.. note::

      There are many other solutions to manage CV, but I want not
      a standard and rigid system.

.. note::

      With Europass, there is also the option of serialising an
      XML file for uploading to the online editor. That is extremely less
      flexible because of the explicit use of a fixed data scheme.

What do you need
----------------

To use this solution you need (see `installation of
requirements <https://victe.github.io/cv-templating/requirements.html>`_
if it is needed):

-  Python (>2.7, >3.5) with modules yaml, jinja2, argparse, datetime and
   os installed. (Probably already installed with your Python).
-  A recent LaTeX distribution (I use texlive-2016) if you want to
   generate the CV in PDF format (mandatory if you want a Europass CV).

Install cv-templating
---------------------

Download the `dist
file <https://github.com/victe/cv-templating/releases>`_ and do:

.. code:: sh

    pip install  cv-templating-x.y.z.tar.gz

Where x.y.z should be the numbers of the downloaded version. It is
better if you use `virtual
environment <https://virtualenv.pypa.io/en/stable/>`_.

For knowing where the program is installed, run this:

.. code:: sh

    python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"

And go to the directory ``mcv`` inside the result of the last command.
Here is a directory named ``examples`` that you should review following
the tutorial_.

To execute the program:

.. code:: sh

    mcv path/to/config/file.yaml

Where ``path/to/config/file.yaml`` is the name and path of a config file
in ``YAML`` format (see below).

It is possible that this solution works with previous versions of Python
or Texlive, but I did not test that.

Also, if you want the Europass format (for PDF only), probably you need
to download the last version of the
`europasscv <https://github.com/gmazzamuto/europasscv>`_ class document
from GitHub (thanks, Giacomo Mazzamuto). Texlive distribution already
includes the document class, but the latest version has some nice
improvements. In the example directory. there is a version of November
2016.

Making the 'omelette'
---------------------

You only need to map the name of the variables used in the template with
the variables in the data files. The format of the data files follows
`yaml <http://www.yaml.org/refcard.html>`_ [#f1]_.

The information to feed the templates can be structured as you want, but
it is preferable to follow some folder structure. For instance, probably
is a good idea to have a folder for all the data (for example, you
guest, exactly: ``data``). Inside some file for general information, a
folder for projects and inside it a file for each project, or a folder
for each (if you want to store other info related to the project as
photos).

If you want to make an HTML-based CV, the syntax to use in the templates
is the `Jinja standard <http://jinja.pocoo.org/docs/dev/templates/>`_.

In the LaTeX case, the syntax for templating is a customization based on
`this snippet <http://flask.pocoo.org/snippets/55/>`_ of `Flask
framework <http://flask.pocoo.org/>`_.

There are examples of each type in the ``examples`` directory,
``excvhtml.jinja`` in the ``html`` folder and ``europass-someone.tex``
in the ``latex`` folder.

See the tutorial_ based on these examples showing how to proceed. You
can use the structure of files and directories as a seed for your
structure, modifying the templates provided as necessary.

Attention!: If the specified combination of base directory and output
directory does not exist, then the program makes a new one if the user
has permission to do that.

Problems and bugs
-----------------

If you find something wrong, please write an
`issue <https://github.com/victe/cv-templating/issues>`_ in the repo. I
do not have much time to spend in this project, but I will try to
respond to all your enquiries (maybe not so fast, please be indulgent
with me).

License
-------

The example based on europasscv is subject to the LaTeX Project Public
License Version 1.3.

The rest of the code, examples and tutorial follows MIT
`licence <license.html>`_, or it has an unknown license. You must
consider citing the authors of each part when you use their code.

.. rubric:: Footnotes

.. [#f1] YAML is more human readable than JSON.

.. include:: links.rst
