import os

from distutils.core import setup

from shutil import copyfile

from setuptools import find_packages

try:
    os.system("pandoc --from=markdown --to=rst README.md -o README.rst")
except (IOError, ImportError):
    description = open('README.md').read()

# The output in html format has extension .md to be processed by github jeckill in raw
os.system("pandoc --from=markdown_github --to=html5 auxfiles/tutorial.md -o auxfiles/tutorial.html")
os.system("cat auxfiles/head.html auxfiles/tutorial.html auxfiles/endpart.html >docs/tutorial.html")
copyfile('README.md', 'docs/index.md')

VERSION = '0.0.20'

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
