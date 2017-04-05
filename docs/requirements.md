# Install requirements

I do not explain how to install all the possibilities between operating systems and versions of libraries, but at least pointing out how to proceed.

## Python

If you are on Linux or Mac, you already have python (probably a 2.7.x version, but if it is a 3.5.x version, it is alright). If you are a Windows user then [follow this instruction] (for what flavour to install, 2 or 3, see [related info](https://wiki.python.org/moin/Python2orPython3)).

### Python modules

We need `yaml`, `os`, `datetime`, `argparse` and `jinja2`. Probably they are already installed with your python distribution. If you install `cv-templating` (see the [tutorial](tutorial.html), `pip` takes care of installing the dependencies. If some of them are missing, the easiest way to install it is with:

On Linux or OS X:

```sh
pip install yaml jinja2 csv
```

On Windows:

```sh
python -m pip install yaml jinja2 csv
```

If you have not `pip` installed, then please refer to the instructions for your platform and Python distribution for help [installing pip](https://packaging.python.org/installing/#requirements-for-installing-packages).

It is very convenient if you use `virtual environment`.
