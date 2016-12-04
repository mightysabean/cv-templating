# cv-templating

Tools for automatic generation of curriculum vitae from data.


## Motivation

Update a [Europass CV online](https://europass.cedefop.europa.eu/editors/en/cv/compose), or made it for the first time, is error and time consuming if you have several entries. Even worst if you need to put all your *resume* in another format (for instance in HTML) or in another language.

## Solution

We can manage the generation of the CV quickly from data conveniently stored using templates based in [jinja2](http://jinja.pocoo.org/docs/dev/).

In this solution, I use data stored in plain text files, facilitating the utilisation of any tool for modifying them. Also, it is very convenient for putting your CV information under control version.

Note: If you only need the europass format (in latex) in only one language, then probably is better that you edit a new document using the document class *europasscv* provided by tex distributions or getting the last version from [github repo](https://github.com/gmazzamuto/europasscv).

## What do you need

To use this solution you need (see [installation of requirements](requirements.html) if it is needed):

- Python (>2.7, >3.5) with modules yaml, jinja2, argparse, datetime and os installed. (Probably already installed with you Python).
- A recent LaTeX distribution (I use texlive-2016) if you want to generate the CV in PDF format (mandatory if you want a Europass CV).

It is possible that this solution works with previous versions of the tools, but I did not test that.

Also, if you want the Europass format (for PDF only), probably you need to download the last version of the [europasscv](https://github.com/gmazzamuto/europasscv) class document from GitHub (thanks, Giacomo Mazzamuto). Texlive distribution already includes the document class, but the last version has some nice improvements.

## Making the 'omelette'

You only need to map the name of the variables used in the template with the variables in the data files. The format of the data files follows [yaml](http://www.yaml.org/refcard.html) \[[1](#Why YAML)\].

The information to feed the templates can be structured as you want, but it is preferable to follow some folder structure. For instance, probably is a good idea to have a folder for all the data (for example, you guest, exactly: `data`). Inside some file for general information, a folder for projects and inside it a file for each project, or a folder for each (if you want to store other info related to the project as photos).

If you want to make an HTML-based CV, the syntax to use in the templates is the [jinja standard](http://jinja.pocoo.org/docs/dev/templates/).

In the LaTeX case, the syntax for templating is a customization based on [this snippet](http://flask.pocoo.org/snippets/55/) of [flask framework](http://flask.pocoo.org/).

There are examples of each type in the `examples` directory, `excvhtml.jinja` in the `html` folder and `europass-someone.tex` in the `latex` folder.

See the [tutorial](tutorial.html) based on these examples showing how to proceed. You can use the structure of files and directories as a seed for your strucuture, modifying the templates provided as necessary.

Atention!: If the specified combination of base directory and output directory does not exists, then the program makes a new one if the user has permission to do that.

## Problems and bugs

If you find something wrong, please write an [issue](https://github.com/victe/cv-templating/issues) in the repo. I do not have many time to spend in this project, but I will try to respond to all your enquiries (maybe not so fast, please be indulgent with me). 

## License

The example based on europasscv is subject to the LaTeX Project Public License Version 1.3.

The rest of the code, examples and tutorial follows MIT [licence](license.html) or it has an unknown license. You must consider citing the authors.

## Next steps to do

- example html.
- example Word (workaround make html and load in Word).
- example markdown.
- example knitr.
- tutorial converting with pandoc.
- tox, behave.
- Dockerize.
- Java, freemarker.

<!--TODO 
- make links to final page in github
-->

## Notes

<a name="Whay YAML">1</a>: YAML is more human readable than JSON or other possibilities as CSV, that could be better for part of the data, but not to integrate all in only one format.