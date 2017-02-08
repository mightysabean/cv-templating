# Tutorial

Clone the project or download a zip and extract their content.

To check the examples, go to the directory of the program, then you must do, for HTML:

```sh
python mcv.py examples/eucv_en_html.yaml
```

And for LaTeX:

```sh
python mcv.py examples/eucv_en_latex.yaml
```

The names of the config files can be anything. Althogth, it is better if is something that could rememeber you their content. It could be your name, date and place or company you are applying.

## Config file

This is the file you pass as a parameter to `mcv.py` program. Each config file has three main sections: config, doc, and data.

You must put in the first section info related to the generation, from where the program can find anything else (*base_dir*), where you want the output (*output_dir*), which template want to use (*template_file*), what kind of template is it (*type*), which is the template base directory (*template_base_dir*), and the output file name (*output_filename*). You can not change these variables in the section *config*. You can not change also the name of the three main sections. To the content of the *output_filename* variable is appended the date when the output is generated. *base_dir* refers to the directory from where the rest of the information in the config file is reachable, *template_base_dir* refers to the directory from which *jinja* can infers the position of other templates when *extends* will be used.

The content and name of the variables inside the other two section is up to you. You can see in the examples and this tutorial how easy is to map variables in data files with the variables in the template files.

## Data

## Template

### Latex

!!!El formato de plantilla europasscv de ejemplo no es completo. Usando la clase hay más campos que los empleados.
!!! Se usa la versión de europasscv que viene instalada con Texlive 2016. La nueva versión en Github es mejor pero hay que cambiar xxx por yyy para que se compile.

### HTML

Note: if the final objective of the html file generate is to be putted in a web page, then I suggest you don't put any sensible information in the CV. For instance, the html example provided do not include the address and telephone. For the email, it is better to add an obfuscating trap for bots, or use a new dedicated account with a good spam filter. For good spam filter I mean that it is configurable, because in this case, it is better not to have false positives, althogth that implies getting more spam in the main mail folder (but you don't want to lose some contractor request in the darkness of the spam folder).

## Tips

- When modifying the template save and compile frequently to check if you do not forget to close some block. Even better if you use Git or a control version software.

- When the value of your variable does not appears in the document generated, check if you has not forgotten putting your variable inside the markers used in your template (for html {{ variable }} and for latex ((( variable ))) ).

- If you need to write a variable inside parenthesis see for example *country* in europasscv or html template examples.

- If you need to store some of your data already formated, then better if you make a subdivision of that data using the name of the format as name of the variable subdivision. See xxx for an example. In that case is preferable that the variable in YAML will be stored using the | format. That permits to write in several lines using the final syntax. As you are writing final code syntax, you must not escape never the variable in the template. For instance see personal skills.

## Test
