Installing Sphinx
=================


Local Installation
==================

.. tip::
    When you need to write a lot of documentation, it's a **good idea** to do it all locally. 


1. Cloning the Repo
------------------------
Clone the `sphinx-documentation-demo <https://github.com/bioteam/sphinx-documentation-demo>`_ GitHub repository into a local directory:

.. code-block:: bash

    git clone git@github.com:bioteam/sphinx-documentation-demo.git

2. Installing Sphinx 
---------------------------------
Sphinx, and extensions for Sphinx, are *python packages* that can be installed on your computer.
The packages you need to install are in :code:`requirements.txt` in the :code:`sphinx-documentation-demo` repository.
It's a good idea to install them in a **virtual environment**.



2a. Using :code:`venv` to install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    python -m venv sphinx_venv
    source sphinx_venv/bin/activate
    pip install -r requirements.txt



3. Building Documentation
-------------------------
The documentation for the :code:`sphinx-documentation-demo` is located in :code:`docs/`.
While in the root project directory, do:

.. code-block:: bash

    sphinx-build -M html docs/ _build

This will tell Sphinx to generate static HTML documentation from :term:`rST` files within :code:`docs/` and then place them in :code:`_build`.
You can open the file :code:`docs/index.html` on your computer to view the HTML documentation in your web browser.



3a. Using :code:`sphinx-autobuild`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The :code:`sphinx-autobuild` extension allows us to build local documentation whenever we make changes.
It also refreshes the web browser so you can see the changes "live". This makes it **very convenient for rapid development**.

While in the virtual environment, run the following command:

.. code-block:: bash

    sphinx-autobuild docs _build

You can then point your web browser to: http://127.0.0.1:8000/

Remote Build on GitHub
======================

.. todo::

    Finish the guide for remote building on GitHub.