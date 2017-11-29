# ==============================================================================
# File Name:    setup.py
# Summary:
#    Defines the python wheel package details for Azure CLI extension.
# See: 
#    https://packaging.python.org/tutorials/distributing-packages/#setup-py
#    https://github.com/pypa/sampleproject/blob/master/setup.py
#    https://packaging.python.org/en/latest/distributing.html
# ==============================================================================

# To use a consistent encoding
from codecs import open #pylint: disable-msg=W0622
from os import path

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README.rst file
with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    # Set the project name.
    # See: 
    #    https://packaging.python.org/tutorials/distributing-packages/#name
    name="helloworldsample",

    # Set the current version of this project, should comply with PEP440.  
    # See:
    #    https://packaging.python.org/tutorials/distributing-packages/#version
    #    https://www.python.org/dev/peps/pep-0440/
    #    https://packaging.python.org/tutorials/distributing-packages/#choosing-a-versioning-scheme
    #    https://packaging.python.org/en/latest/single_source_version.html
    version="0.0.1",

    # Set the short and long description for this project.
    # See:
    #    https://packaging.python.org/tutorials/distributing-packages/#description
    #    http://docutils.sourceforge.net/rst.html
    description="A sample Azure CLI extension project",
    long_description=LONG_DESCRIPTION,

    # Set the project main page.
    url='https://github.com/pengzhisun/azure-cli-extension-sample',

    # Set the author details
    author='Pengzhi Sun',
    author_email='pengzhisun@live.com',

    # Set the project license
    license='MIT',

    # Set a list of classfiers that categorize this project
    # See:
    #    https://packaging.python.org/tutorials/distributing-packages/#classifiers 
    #    https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #    3 - Alpha
        #    4 - Beta
        #    5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # Set the keywords that describe this project.
    keywords='sample azure azure-cli azure-cli-extension',

    # Set the packages to be included in this project.
    # See:
    #    https://packaging.python.org/tutorials/distributing-packages/#packages
    packages=find_packages(),

    # Include the Azure CLI extension metadata data file to this packages.
    # See:
    #    https://github.com/Azure/azure-cli/blob/master/doc/extensions/metadata.md
    #    https://packaging.python.org/tutorials/distributing-packages/#package-data
    package_data={
        'azext_helloworldsample': ['azext_metadata.json'],
    },

    # Set run-time dependencies for this project.
    # These will be installed by pip when this project is installed.
    # See:
    #    https://packaging.python.org/tutorials/distributing-packages/#install-requires
    #    https://packaging.python.org/en/latest/requirements.html
    install_requires=['azure-cli-core'],
)
