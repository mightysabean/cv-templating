# Tutorial

The use of `cv-templating` is very easy. But you must know what `yaml` and `jinja2` are, and how to use it. It is not necessary to be an expert, but a minimum of knowledge is required.

The full specification of `yaml` are at [yaml specs](http://www.yaml.org/spec/1.2/spec.html) (see *Chapter 2* for a quick intro) or see [yaml basics](http://docs.ansible.com/ansible/YAMLSyntax.html).

For `jinja2` you should consult [jinja documentation](http://jinja.pocoo.org/docs/2.9/).

For the objective of making a document using a template and a data file, you do not need all the `cv-templating` project. You just need writing a little script in `Python` like this (this example is for generating an HTML file), `script.py`:

```python
import yaml
import jinja2

data_file = 'your/data_file.yaml'
template_directory = 'base/template_directory'  # where template files refer as root for to be used internally in the templates, not in the python script
template_file = 'base/template_directory/template_file.html'
data = yaml.load(open(data_file, 'r'))
output_file = 'your/output_file.html'

env = jinja2.Environment(loader=jinja2.FileSystemLoader(templateBaseDir),
                         lstrip_blocks=True, 
                         trim_blocks=True)
template = env.get_template(template_file)
stream_produced = template.render(data)
with open(output_file, 'w') as o:
            o.write(stream_produced)
```

With a data file like this (in the python code `your/data_file.yaml`):

```yaml
title: My CV
emails:
  - yo@aqui.com
  - me@here.com
```

Using this template (in the python code `base/template_directory/template_file.html`):

```html
<!doctype html>
<html>
    <head>
      <meta charset="utf-8"/>
      <title>{{ title }}</title>
    </head>
    <body>
      <h1>{{ title }}</h1>
      <ul>
        {% for email in emails %}
          <li>{{ email }}</li>
        {% endfor %}
      </ul>
    </body>
</html>
```

Executing the python `script.py`

```sh
python script.py
```

You will obtain the file `your/output_file.html`:

```html
<!doctype html>
<html>
    <head>
      <meta charset="utf-8"/>
      <title>My CV</title>
    </head>
    <body>
      <h1>My CV</h1>
      <ul>
          <li>yo@aqui.com</li>
          <li>me@here.com</li>
      </ul>
    </body>
</html>
```

To do the same with LaTeX, you need to change the syntax tokens of jinja. See this [explanation](http://flask.pocoo.org/snippets/55/) that is used in `cv-templating` (se file jinjatex.py).

The **cv-templating** project takes care of the type of render and checks a lot of things necessary for me. You can modify it to reach your goals.

## Install cv-templating

Download the [dist file](https://github.com/victe/cv-templating/releases) and do:

```sh
pip install  cv-templating-x.y.z.tar.gz
```

Where x.y.z should be the numbers of the downloaded version. It is better if you use [virtual environment](https://virtualenv.pypa.io/en/stable/).

For knowing where the program is installed, run this:

```sh
python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
```

And go to the directory `mcv` inside the result of the last command. Here is a directory named `examples` that you should review following the tutorial.

To execute the program:

```sh
mcv path/to/config/file.yaml
```

Where `path/to/config/file.yaml` is the name and path of a config file in `YAML` format (see below).

## Check the examples

To examine the examples, go to the directory of the program, then you must do, for HTML:

```sh
mcv examples/eucv_en_html.yaml
```

You can see the [HTML document generated](Someone.html).

And for LaTeX:

```sh
mcv examples/eucv_en_latex.yaml
```

You can see the [PDF document generated](Someone.pdf).


## Config file

The config file is the `yaml` file you pass as a parameter to the `mcv.py` program. The names of the config files can be anything. Although, it is better if it is something that helps you to easy remember their content. It could be your name, date and place or company you are applying.

Each config file has three main sections: **config**, **doc**, and **data**.

### Config section of the config file

This is the content of the **config** section of the `eu_en_html.yaml` file in the examples directory (in all `yaml` files avoid the use of *TABs*):

```yaml
config:
  base_dir: '/home/vicente/projects/pro/cv-templating/mcv/examples' # you must change this to the directory where you have your data and templates structure
  output_dir: 'output/html'
  template_base_dir: 'html'
  template_file: 'flat_en.html'
  template_type: html
  output_filename: "Someone"
  resources: # Will be copied to tmp dir inside the directories specified by the name of the variable.
    build: # Resources to be copied to "tmp" before building final doc. "src" Relative to base directory, "dst" relative to "tmp" directory to build if it is the case.
      - ["data/figures/bobo.png", "images/bobo.png"]
      - ["html/flat_en_resources", ""]  # if "dst" is empty, files will be copied to "tmp" folder. In this example, the program copies the content of a whole directory.
    output: # Will be copied to de output folder inside a directory with the name as the variable.
      - ["data/figures/bobo.png", "images/bobo.png"]
      - ["html/flat_en_resources", "css"]
```

You must put in this first section, **config**,  information related to the generation, from where the program can find anything else (*base_dir*), where you want the output (*output_dir*), which template want to use (*template_file*), what kind of template is it (*type*), which is the template base directory (*template_base_dir*), and the output file name (*output_filename*). You can not change the name of these variables in the section **config**. You can not also change the name of the three sections (config, doc and data). The content and name of the variables inside the other two section (doc and data) are up to you. You can see how easy is to map variables in data files with the variables in the template files in the examples, and in this tutorial.

The program appends the date to the content of the *output_filename* variable when the output is generated. *base_dir* refers to the directory from where the rest of the information in the config file is reachable, *template_base_dir* relates to the directory from which *Jinja* can infer the position of other templates when *extends* (if you use heritance in your templates) will be employed.

### doc section

The **doc** section is intended to be used for information related to the configuration of the document itself. For instance, to specify the paper size, orientation, title, keywords, etc. that you could easily change from one type of CV to other (just copy your config.yaml file and change the values).

This is the **doc** section content of the same config file used before:

```yaml
doc:
  language: "en"
  title: "Curriculum vitae"
  bigitem:
    - "Personal statement"  # Also, it could be 'Job applied for', 'Position', 'Preferred job', 'Studies applied for'
    - "Something good about Bobo."
```

And this is where you use the variable in the template file (from the config section, the file must be `flat_en.html` inside the template base dir `html` inside of the base structure in `/home/vicente/projects/pro/cv-templating/mcv/examples`):

```html
<!DOCTYPE html>
<!-- Based on http://themes.jsonresume.org/theme/flat -->
<html lang={{ language }}><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<meta name="viewport" content="width=device-width, user-scalable=no, minimal-ui">
<title>{{ title }}</title>
...
```

You just need to put the name of the variable between a pair of curly brackets. In the output file, the content of the variable will be substituted.

### data section

The **data** section must point to the files that have the stored data. You can use `yaml` files for unstructured or semi-structured data or `csv` files for tabular. From the same config file used before:

```yaml
data: # list of data files with a variable name to refer them in the template file.
  persinfo: "data/pers_info-en.yaml"
  profinfo: "data/prof_info-en.yaml"
  acadinfo: "data/acad_info-en.yaml"
  persskills: "data/pers_skills-en.yaml"
  additinfo: "data/addit_info-en.yaml"
  references: "data/references.yaml"
  curses: "data/acad_info_curses-en.csv"
```

In the templates, you must prefix variables in your data file with the variable asigned to it in the config file. The content of the `data/pers_info-en.yaml` is:

```yaml
family_name: "Without Name"
name: "Name"
fullname: "Without Name, Someone"
address: "One Address street"
postal_code: "00000"
village: "The Village"
country: "The Country"
telephone: "+01 234 567 890"
mobile: "+01 234 567 890"
emails:
  - "someone@example.com"
  - "name.familyname@example.com"

...
```

And the use in the template file is:

```html
<h1>
{{ persinfo.fullname }}
</h1>
<h2>
{{ persinfo.profession }}
</h2>

...
```

The result will be:

```html
...
...
<h1>
Without Name, Someone
</h1>
<h2>
Dark wizard
</h2>

...
```

## Templates

You can use the full power of `Jinja` in your templates. You can, for instance, check if a variable is defined, or if the variable store multiples values (arrays, lists) repeat the block of text varying the contents. From the same example, the data about emails in `data/pers_info-en.yaml`:

```yaml
...

emails:
  - "someone@example.com"
  - "name.familyname@example.com"

...
```

The use of the data in the HTML template:

```html
...

{% if persinfo.emails|length>0 %}
    <div class="col-sm-6">
        <strong>
        {%- if persinfo.emails|length>1 %}
            Emails
        {% else %}
            Email
        {% endif -%}
        </strong>
        <div class="email">
            <ul>
            {% for email in persinfo.emails %}<li>{{ email }}</li>{% endfor %}
            </ul>
        </div>
    </div>
{% endif %}

...
```

<aside>Tip: The use of a hyphen ("-") at the start or end of a block permits delete white spaces or newlines between the exterior and the interior of the block.</aside>

The result is:

```html
<div class="col-sm-6">
    <strong>Emails</strong>
    <div class="email">
        <ul>
          <li>someone@example.com</li>
          <li>name.familyname@example.com</li>
        </ul>
    </div>
</div>
```

### Latex

The format of `jinja2` variables and blocks in the latex templates has been changed because of the use of curly brackets in LaTeX.

You must change one { or } by two (( or )).

### HTML

Note: if the final objective of the HTML file generated is to be put on a web page, then I suggest you don't put any sensitive information on the CV. For instance, do not include your address and telephone. For the email, it is better to add an obfuscating trap for bots or use a new dedicated account with a good spam filter. For good spam filter I mean that it is configurable, because in this case, it is better not to have false positives, although that implies getting more spam in the main mail folder (but you don't want to lose some contractor request in the darkness of the spam folder).

## Tips

- When modifying the template save and compile frequently to check if you do not forget to close some block. Even better if you use Git or a control version software.

- When the value of your variable does not appear in the document generated, check if you have forgotten to put your variable inside the markers used in your template (for HTML {{ variable }} and LaTeX ((( variable ))) ).

- If you need to write a variable inside some parenthesis, see for example *country* in europasscv and the use of "-".
    ```latex
    \ecvaddress{((( persinfo.address ))), ((( persinfo.postal_code ))) ((( persinfo.village ))) ( (((- persinfo.country -))) ) }
    ```
- Because this workflow is in principle for your own use, you do not need to escape content of variables. If you can read about is good for you. Avoid using shell escape (\write18{}) in LaTeX and probably you are save.

- If you need to store some of your data already formatted, then it is better if you make a subdivision of that data using the name of the format as the name of the variable. In this case, it is preferable that the variable in YAML will be stored using the | style. That permits to write in several lines using the final document syntax. As you are writing final code syntax and you control what is inside the data, you do not need to escape the variable in the template. For instance, see personal skills.

  For example, in the `data/pers_info-en.yaml` file, at the end:

  ```yaml
  ...

  profession: "Dark wizard"
  about: 
    html: |
      I am, of course, the <strong>best in the world</strong> in the things I do. I was born sometime ago in a place where "the rule is not born by your own means", your mother was there with you. My mother told me, this should be the last time that you born all by yourself (homage to <a href="https://en.wikipedia.org/wiki/Miguel_Gila">Miguel Gila</a>). 
      When I was a little kid, I also started to walk alone. When I was a teenager, you know... After that, I never started a startup, I was never the best in anything, so, if you want to hire me, you must know who I am. 
    latex: |
      I am, of course, the \textbf{best in the world} in the things I do. I was born sometime ago in a place where "the rule is not born by your own means", your mother was there with you. My mother told me, this should be the last time that you born all by yourself (homage to \href{https://en.wikipedia.org/wiki/Miguel_Gila}{Miguel Gila}). 
      When I was a little kid, I also started to walk alone. When I was a teenager, you know... After that, I never started a startup, I was never the best in anything, so, if you want to hire me, you must know who I am.
  
  ...
  ```

  You write markup directly for both HTML and LaTeX in two different variables behind the same parent variable `about`. You then use it in the template as:

  ```html
  {% if persinfo.about.html is defined %}
    <section id="about" class="row">
      <aside class="col-sm-3">
      <h3>About</h3>
      </aside>
      <div class="col-sm-9">
      <p>{{ persinfo.about.html }}</p>
      </div>
    </section>
  {% endif %}
  ```

- For use `csv` tabular data, see the example file `acad_info_curses-en.csv`:

    ```csv
    name,year
    How to make cakes, 2000
    How to not eat the cakes you cooked, 2001
    ```

    It is declared in the data section of the config file as `curses`, and it is used in the html template example:

    ```html
    {% if curses is defined %}

    <section id="curses" class="row">
    <aside class="col-sm-3">
      <h3>Curses</h3>
    </aside>
    {% for curse in curses %}
      <h4 class="strike-through">
      <span>{{ curse.name }}</span>
      <span class="date">
      {{ curse.year }}
      </span>
      </h4>
    {% endfor %}
    </section>
    {% endif %}
    ```

    And the result:

    ```html
    <section id="curses" class="row">
      <aside class="col-sm-3">
        <h3>Curses</h3>
      </aside>
      <h4 class="strike-through">
      <span>How to make cakes</span>
      <span class="date">
        2000
      </span>
      </h4>
      <h4 class="strike-through">
      <span>How to not eat the cakes you cooked</span>
      <span class="date">
        2001
      </span>
      </h4>  
    ```

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-82399329-2', 'auto');
  ga('send', 'pageview');

</script>