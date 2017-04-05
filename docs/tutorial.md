# Tutorial

The use of `cv-templating` is very easy. But you must know what `yaml` and `jinja2` are, and how to use it. It is not neccesary to be an expert, but a minimum of knowledge is required.

The full specification of `yaml` are at [yaml specs](http://www.yaml.org/spec/1.2/spec.html) (see *Chapter 2* for a quick intro) or see [yaml basics](http://docs.ansible.com/ansible/YAMLSyntax.html).

For `jinja2` you should consult [jinja documentation](http://jinja.pocoo.org/docs/2.9/).

## Install cv-templating

Clone the project or download the [dist](https://github.com/victe/cv-templating/releases) file and extract their content. You can install to the system or use it without installing it. For install, you must go to the folder when you download or extract the code and do (it is convinient to use [virtual environment](https://virtualenv.pypa.io/en/stable/) ):

If you downloaded the dist file:

```sh
pip install cv-templating-x.y.z.tar.gz
```

Donde x.y.z corresponderán a la versión descargada

Or, if you clone the repository or extract the download file:

```sh
python setup.py install
```

If you extracted or cloned `cv-templating`, you know yet where it is, if you installed it then run this:

```sh
python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
```

And go to the directory `mcv` inside the result of the last command.

To execute the program if you instaled it you must do:

```sh
mcv path/to/config/file.yaml
```

or if you downloaded:

```sh
python mcv.py path/to/config/file.yaml
```

Where `path/to/config/file.yaml` is the name and path of a config file in `YAML` format (see below).

## Check the examples

To check the examples, go to the directory of the program, then you must do, for HTML:

```sh
python mcv.py examples/eucv_en_html.yaml
```

And for LaTeX:

```sh
python mcv.py examples/eucv_en_latex.yaml
```

The names of the config files can be anything. Althogth, it is better if is something that help you to easy remember their content. It could be your name, date and place or company you are applying.

## Config file

The config file is the `yaml` file you pass as a parameter to `mcv.py` program. Each config file has three main sections: **config**, **doc**, and **data**.

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

You must put in this first section, **config**,  information related to the generation, from where the program can find anything else (*base_dir*), where you want the output (*output_dir*), which template want to use (*template_file*), what kind of template is it (*type*), which is the template base directory (*template_base_dir*), and the output file name (*output_filename*). You can not change the name of these variables in the section **config**. You can not change also the name of the three main sections (config, doc and data). The content and name of the variables inside the other two section (doc and data) is up to you. You can see in the examples and this tutorial how easy is to map variables in data files with the variables in the template files.

The program appends the date to the content of the *output_filename* variable when the output is generated. *base_dir* refers to the directory from where the rest of the information in the config file is reachable, *template_base_dir* refers to the directory from which *jinja* can infers the position of other templates when *extends* (if you use hereditance in your templates) will be used.

### doc section

The **doc** section is intended to be used for information related with the configuration of the document itself. For instance, to especify the paper size, orientation, title, keywords, etc. that you could easely change from one type of CV to other (just copy your config.yaml file and change the values).

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

You just need to put the name of the variable between a pair of curly barckets. In the output file, the content of the variable will be substituted.

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
family_name: "Familyname"
name: "Name"
fullname: "Family_name, name"
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
Family_name, name
</h1>
<h2>
Dark wizard
</h2>

...
```

## Templates

You can use the full power of `jinja` in your templates. You can, for instance, check if a variable is defined, or if the variable store multiples values (arrays, lists) repeat the block of text varying the contents. From the same example, the data about emails in `data/pers_info-en.yaml`:

```yaml
...

emails:
  - "someone@example.com"
  - "name.familyname@example.com"

...
```

The use in the html template:

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

<aside>Tip: The use of hypen ("-") at the start or end of a block permits delete white spaces or newlines between the exterior and the interior of the block.</aside>

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

The format of `jinja2` variables and blocks in the latex templates has been changed because the use of curly brackets in LaTeX.

You must change one { or } by two (( or )).

### HTML

Note: if the final objective of the html file generate is to be putted in a web page, then I suggest you don't put any sensible information in the CV. For instance, do not include your address and telephone. For the email, it is better to add an obfuscating trap for bots, or use a new dedicated account with a good spam filter. For good spam filter I mean that it is configurable, because in this case, it is better not to have false positives, althogth that implies getting more spam in the main mail folder (but you don't want to lose some contractor request in the darkness of the spam folder).

## Tips

- When modifying the template save and compile frequently to check if you do not forget to close some block. Even better if you use Git or a control version software.

- When the value of your variable does not appears in the document generated, check if you has forgotten putting your variable inside the markers used in your template (for html {{ variable }} and for latex ((( variable ))) ).

- If you need to write a variable inside parenthesis, see for example *country* in europasscv and the use of "-".
    ```latex
    \ecvaddress{((( persinfo.address ))), ((( persinfo.postal_code ))) ((( persinfo.village ))) ( (((- persinfo.country -))) ) }
    ```

- If you need to store some of your data already formated, then better if you make a subdivision of that data using the name of the format as name of the variable subdivision. In that case is preferable that the variable in YAML will be stored using the | style. That permits to write in several lines using the final document syntax. As you are writing final code syntax, you must not escape never the variable in the template. For instance see personal skills.

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

  You write directly markup for both html and LaTeX in two different variables behind the same parent variable `about`. You then use it in the template as:

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