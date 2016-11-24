# cv-templating

Tools for automatic generation of curriculum vitae from data.


## Motivation

Update an [Europass CV online](https://europass.cedefop.europa.eu/editors/en/cv/compose), or made it for the first time, is error and time consuming if you have several entries. Even worst if you need to put all your *resume* in other format (for instance in HTML).

## Solution

Using templates based in [jinja2](http://jinja.pocoo.org/docs/dev/) we can manage the generation of the CV easily from data conveniently stored.
 
In this solution I use data stored in plain text files, facilitating the use of any tool for modifying them. Also, it is very convinient for putting your CV information under control version. 

## What do you need

To use this solution you need (to install see ):

- Python (>2.7, >3.5) with modules yaml, jinja2 and csv installed.
- A recent LaTeX distribution (I use texlive-2016) if you want to generate the CV in PDF format (mandatory if you want a europass CV).

It is possible that this solution works with previous versions of the tools, but I do not tested that.

Also, if you want the Eurospass format (for PDF only), probably you need to download the last version of the [europasscv](https://github.com/gmazzamuto/europasscv) class document from github (thanks Giacomo Mazzamuto). It is already included in the texlive distribution, but the last version have some nice improvements.

## Install requirements

I do not explain how to install all the posibilities between operating systems and versions of libraries, but at least pointing out to how proceed.

### Python

If you are on Linux or Mac, you already have python (probably a 2.7.x version, but if it is a 3.5.x version, it is allright). If you are Windows user then [follow this instructions] (for what flavour to install, 2 or 3, see [related info](https://wiki.python.org/moin/Python2orPython3)).


### Python modules

We need `yaml`, `csv` and `jinja2`. Probably they are already installed with your python distribution. If some of them is missing, the easyest way to install it is with:

On Linux or OS X:
```sh
pip install yaml jinja2 csv
```

On Windows:
```sh
python -m pip install yaml jinja2 csv
```

If you have not `pip` installed, then please refer to the instructions of your platform and python distrubution for help [installing pip](https://packaging.python.org/installing/#requirements-for-installing-packages).

## Making the 'omelette'


## License


## Next steps to do

- Dockerize.