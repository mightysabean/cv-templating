# cv-templating

Tools for automatic generation of curriculum vitae from data.


## Motivation

Update a [Europass CV online](https://europass.cedefop.europa.eu/editors/en/cv/compose), or made it for the first time, is error and time consuming if you have several entries. Even worst if you need to put all your *resume* in another format (for instance in HTML) or in another language.

## Solution

We can manage the generation of the CV quickly from data conveniently stored using templates based in [jinja2](http://jinja.pocoo.org/docs/dev/).

In this solution, I use data stored in plain text files, facilitating the utilisation of any tool for modifying them. Also, it is very convenient for putting your CV information under control version.

Note: If you only need the europass format (in latex) in only one language, then probably is better that you edit a new document using the document class *europasscv* provided by tex distributions or getting the last version from [github repo](https://github.com/gmazzamuto/europasscv).

## What do you need

To use this solution you need (for installation see below):

- Python (>2.7, >3.5) with modules yaml, jinja2 and csv installed.
- A recent LaTeX distribution (I use texlive-2016) if you want to generate the CV in PDF format (mandatory if you want a Europass CV).

It is possible that this solution works with previous versions of the tools, but I did not test that.

Also, if you want the Europass format (for PDF only), probably you need to download the last version of the [europasscv](https://github.com/gmazzamuto/europasscv) class document from GitHub (thanks, Giacomo Mazzamuto). Texlive distribution already includes the document class, but the last version has some nice improvements.

## Install requirements

I do not explain how to install all the possibilities between operating systems and versions of libraries, but at least pointing out how to proceed.

### Python

If you are on Linux or Mac, you already have python (probably a 2.7.x version, but if it is a 3.5.x version, it is alright). If you are a Windows user then [follow this instruction] (for what flavour to install, 2 or 3, see [related info](https://wiki.python.org/moin/Python2orPython3)).


### Python modules

We need `yaml`, `csv` and `jinja2`. Probably they are already installed with your python distribution. If some of them are missing, the easiest way to install it is with:

On Linux or OS X:
```sh
pip install yaml jinja2 csv
```

On Windows:
```sh
python -m pip install yaml jinja2 csv
```

If you have not `pip` installed, then please refer to the instructions for your platform and Python distribution for help [installing pip](https://packaging.python.org/installing/#requirements-for-installing-packages).

## Making the 'omelette'

You only need to map the name of the variables used in the template with the variables in the data files. The format of the data files follows [yaml](http://www.yaml.org/refcard.html) and [csv](https://en.wikipedia.org/wiki/Comma-separated_values) (you can chose in the master file if separation between fields is ',', 'tab', or ';' and the decimal separator).

The information to feed the templates can be structured as you want, but it is preferable to follow some folder structure. For instance, probably is a good idea to have a folder for all the data (for example, you guest, exactly: `data`). Inside some file for general information, a folder for projects and inside it a file for each project, or a folder for each (if you want to store other info related to the project as photos) or if you have only a resume of projects maybe it is better to have only a `.csv` file. 

If you want to make an HTML-based CV, the syntax to use in the templates is the [jinja standard](http://jinja.pocoo.org/docs/dev/templates/). 

In the LaTeX case, the syntax for templating is a customization based on [this snippet](http://flask.pocoo.org/snippets/55/) of [flask framework](http://flask.pocoo.org/).

There are examples of each type in the `example` directory, [excvhtml.jinja](excvhtml.jinja) in the `html` folder and [excvlatex.jinja](excvlatex.jinja) the `latex` folder. 

See the [tutorial](tutorial.html) based on these examples showing how to proceed. You can use the structure of files and directories as a seed for your strucuture, modifying the templates provided as necessary.

## License

The example based on europasscv is subject to the LaTeX Project Public License Version 1.3.

## Next steps to do
- example html
- example word
- example markdown
- example knitr / pandoc
- tox, behave.
- Dockerize.
- Java, freemarker

<!--TODO 
- make links to final page in github
-->
