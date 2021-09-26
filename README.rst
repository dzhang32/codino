codino
#######

.. image:: https://github.com/dzhang32/codino/workflows/test-deploy-package/badge.svg
    :target: https://github.com/dzhang32/codino/actions?query=workflow%3Atest-deploy-package

.. image:: https://codecov.io/gh/dzhang32/codino/branch/main/graph/badge.svg
    :target: https://app.codecov.io/gh/dzhang32/codino

|

``codino`` takes as input a codon design, the frequency of the nucleotides at each position, then outputs the expected amino acid frequency. Hopefully, in future, it will also do the reverse.

Installation instructions
-------------------------

Install the development version from GitHub using `pip`

.. code-block:: text

  python3 -m pip install git+https://github.com/dzhang32/codino.git

Or, by cloning this repo and running `setup.py`

.. code-block:: text

  git clone https://github.com/dzhang32/codino
  cd pyutils
  python3 setup.py install

Development tools
-----------------

The documentation website is automatically updated thanks to `Sphinx <https://www.sphinx-doc.org/>`_ and this `GitHub Action <https://github.com/JamesIves/github-pages-deploy-action>`_.
