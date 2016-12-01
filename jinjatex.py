from __future__ import print_function
import re
import jinja2

# Example template
# Your LaTeX template might look like this:
# \documentclass{article}
#
# \begin{document}
# Hello, ((( name|escape_tex )))!
# \end{document}
# This snippet by Clemens Kaposi can be used freely for anything you like. Consider it public domain.

# Partialy extracted (changing template syntax and escape_tex) from http://flask.pocoo.org/snippets/55/
LATEX_SUBS = (
    (re.compile(r'\\'), r'\\textbackslash'),
    (re.compile(r'([{}_#%&$])'), r'\\\1'),
    (re.compile(r'~'), r'\~{}'),
    (re.compile(r'\^'), r'\^{}'),
    (re.compile(r'"'), r"''"),
    (re.compile(r'\.\.\.+'), r'\\ldots'),
)

def escape_tex(value):
    newval = value
    for pattern, replacement in LATEX_SUBS:
        newval = pattern.sub(replacement, newval)
    return newval



def render_tex(base, template_filename, doc):
    # make new syntax
    texenv = jinja2.Environment(loader=jinja2.FileSystemLoader(base),lstrip_blocks=True,trim_blocks=True)
    texenv.block_start_string = '((*'
    texenv.block_end_string = '*))'
    texenv.variable_start_string = '((('
    texenv.variable_end_string = ')))'
    texenv.comment_start_string = '((='
    texenv.comment_end_string = '=))'
    texenv.filters['escape_tex'] = escape_tex
    # Render
    template = texenv.get_template(template_filename)
    return template.render(doc)
