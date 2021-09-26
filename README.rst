codino
#######

.. image:: https://github.com/dzhang32/codino/workflows/test-deploy-package/badge.svg
    :target: https://github.com/dzhang32/codino/actions?query=workflow%3Atest-deploy-package

.. image:: https://codecov.io/gh/dzhang32/codino/branch/main/graph/badge.svg
    :target: https://app.codecov.io/gh/dzhang32/codino

|

``codino`` converts a codon design (the frequency of each nucleotide at each position in a codon) to the expected amino acid frequencies, and vice versa.

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
  
Usage
-----

For a more complete example, please see `example.py <https://github.com/dzhang32/codino/blob/main/example.py>`_

.. code-block:: text

  from codino.process import Converter
  
  c = Converter()
  
  # converting from codon design to AA frequencies
  c.cd_to_aa(first = {"A": 1}, second = {"T": 1}, third = {"G": 1})
  # Out: {'M': 1}

  # converting from AA frequency to codon design
  c.aa_to_cd(aa={'M': 1})
  # Out: ({'A': 1.0}, {'T': 1.0}, {'G': 1.0})

Development tools
-----------------

The documentation website is automatically updated thanks to `Sphinx <https://www.sphinx-doc.org/>`_ and this `GitHub Action <https://github.com/JamesIves/github-pages-deploy-action>`_.
