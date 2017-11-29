# ==============================================================================
# File Name:    setup.py
# Summary:
#    Defines the python wheel package details for Azure CLI extension.
# Reference: 
#    https://packaging.python.org/tutorials/distributing-packages/#setup-py
#    https://github.com/pypa/sampleproject/blob/master/setup.py
#    https://packaging.python.org/en/latest/distributing.html
# ==============================================================================

# To use a consistent encoding
from codecs import open #pylint: disable-msg=W0622
from os import path

HERE = path.abspath(path.dirname(__file__))

VERSION = "0.1.2"

# Get the long description from the README file
with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
