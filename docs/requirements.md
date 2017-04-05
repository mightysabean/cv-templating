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

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-82399329-2', 'auto');
  ga('send', 'pageview');

</script>