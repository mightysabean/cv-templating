
from __future__ import print_function
import os
import argparse
import yaml
import jinjatex
import datetime
import mcv_utils

cml = argparse.ArgumentParser(
    description="This program genrate a .tex or .html file of a Curriculum Vitae using templates mades with jinja "
                "and data stored as .yaml. To see an example and tutorial see "
                "http://victe.github.com/cv-templating",
    formatter_class=argparse.RawTextHelpFormatter)
cml.add_argument("config_file", help="File .yaml with specifications of the data and template to use. You must have "
                                "one of this config file for each combination of format, language or data "
                                "contents. You have various examples of config files in the directory examples.")


def getVariableFromList(search_dict, l):
    dc = search_dict.copy()
    for k in l:
        dc = dc.get(k)
    return dc

if __name__ == "__main__":
    args=cml.parse_args()
    config = yaml.load(open(args.config_file, 'r'))
    cf=config['config']
    lang='.'+cf['language']
    output_dir=mcv_utils.output_dir(cf['base_dir'],cf['output_dir'])

    doc = config['doc']
    # Cargar info de yaml de datos For each entry in dict data
    data_files= config['data']
    data = {}
    for d in data_files:
        f = os.path.join(cf['base_dir'],data_files.get(d))
        data.update({d: yaml.load(open(f, 'r'))})
    print(data)
    docdata = mcv_utils.merge_two_dicts(doc, data)


    fullnameperson=getVariableFromList(search_dict=docdata,l=cf['person_name_key_for_filename'])

    ext = 'tex' if cf['type'] == 'latex' else 'html'
    outputfile=os.path.join(output_dir,fullnameperson + datetime.datetime.strftime(datetime.datetime.now(),
                                                                                 "%Y-%m-%d") + '.' + ext)

    tex = jinjatex.render_tex(
        cf['base_dir'],
        cf['template_file'],  # relativo al directorio base
        doc=docdata)
    with open(outputfile, 'w') as o:
        o.write(tex)
