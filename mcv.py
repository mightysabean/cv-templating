
from __future__ import print_function
import os
import argparse
import yaml
import jinjatex
import datetime

cml = argparse.ArgumentParser(
    description="This program genrate a .tex or .html file of a Curriculum Vitae using templates mades with jinja "
                "and data stored as .yaml. To see an example and tutorial see "
                "http://victe.github.com/cv-templating",
    formatter_class=argparse.RawTextHelpFormatter)
cml.add_argument("config_file", help="File .yaml with specifications of the data and template to use. You must have "
                                "one of this config file for each combination of format, language or data "
                                "contents. You have various examples of config files in the directory examples.")



if __name__ == "__main__":
    args=cml.parse_args()
    config = yaml.load(open(args.config_file, 'r'))
    cf=config['config']
    lang='.'+cf['language']
    output_dir= os.path.join(cf['base_dir'],cf['output_dir']) \
        if cf['output_dir'] != '' or cf['output_dir'] is None \
        else cf['base_dir']
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    doc = config['doc']
    # Cargar info de yaml de datos adicionales For each entry in dict doc
    for d in doc:
        print(d, doc.get(d))
        if exist file para cada key, sustituir key with the info in file



    ext = 'tex' if cf['type'] == 'latex' else 'html'
    outputfile=os.path.join(config.doc.pers_info.name + datetime.datetime.now() + '.' + ext)

    with open(outputfile, 'w') as o:
        o.write(jinjatex.render_tex(config.config.template, doc=doc))
