import os

from distutils.core import setup

from setuptools import find_packages

try:
    os.system("pandoc --from=markdown --to=rst README.md -o README.rst")
except (IOError, ImportError):
    description = open('README.md').read()

VERSION = '0.0.19'

setup(
    name='cv-templating',
    version=VERSION,
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
