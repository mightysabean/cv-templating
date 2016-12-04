
from __future__ import print_function
import os
import argparse
import datetime
import yaml
import jinjatex
import mcv_utils
import mcv_c

def create_parser():
    cml = argparse.ArgumentParser(
        description="This program generate a .tex or .html file of a Curriculum"
                    " Vitae using templates made with jinja "
                    "and data stored as .yaml. To see an example and tutorial"
                    "visit http://victe.github.com/cv-templating",
        formatter_class=argparse.RawTextHelpFormatter
        )
    cml.add_argument(
        "config_file",
        help="File .yaml with specifications of the data and template to use."
             "You must have one of this config file for each combination of "
             "format, language or data contents. You have various examples of "
             "config files in the directory examples."
        )
    return cml


def main(configFile):
    if not os.path.exists(configFile):
        raise RuntimeError('Can not be found the file "%s" . The path must be relative from where you are "'
                           'executing the program, as well a full path.' % configFile)
    config = yaml.load(open(configFile, 'r'))
    cvg = mcv_c.CVGenerator(config)
    cvg.render()


if __name__ == "__main__":
    args = create_parser().parse_args()
    main(args.config_file)
