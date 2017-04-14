import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from distutils.dir_util import copy_tree
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'mcv/VERSION')) as version_file:
    version = version_file.read().strip()

# Copy build documentation to docs dir for GH.
copy_tree('sphinx/_build/html', 'docs')


#VERSION = '0.0.20'

setup(
    name='cv-templating',
    version=version,
    packages=find_packages(),
    package_dir={'mcv': 'mcv'},
    url='https://github.com/victe/cv-templating',
    license='MIT',
    author='Vicente Ramirez Perea',
    author_email='victe@ramper.net',

    # Include additional files into the package
    include_package_data=True,

    # Dependent packages (distributions)
    install_requires=[
        "jinja2",
        "PyYAML",
        "pytest"
    ],
    entry_points={
        "console_scripts": ["mcv=mcv.mcv:main"],
    },
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=['pytest',
    ],
)
