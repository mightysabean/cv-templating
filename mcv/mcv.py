# -*- coding: utf-8 -*-
"""
    tablib.core
    ~~~~~~~~~~~
    This module implements the central Tablib objects.
    :copyright: (c) 2017 by Vicente Ramirez Perea.
    :license: MIT, see LICENSE for more details.
"""

from __future__ import print_function

import argparse
import os

import yaml

from .GenTask import GenTask
from .Process import Process


def create_cml_parser():
    """Create command line parser using argparse
    @return object argparse, list of arguments (now only name of config file)
    """
    cml = argparse.ArgumentParser(
        description="This program generate a .tex or .html file of a Curriculum"
                    " Vitae using templates made with jinja "
                    "and data stored as .yaml. To see an example and tutorial"
                    "visit http://victe.github.com/cv-templating",
        formatter_class=argparse.RawTextHelpFormatter
    )
    cml.add_argument(
        "cv_file",
        help="File .yaml with specifications of the data and template to use."
             "You must have one of this CV config file for each combination of "
             "format, language or data contents. You have examples of "
             "CV config files in the directory examples."
    )
    return cml


def makecv(config_file):
    if not os.path.exists(config_file) or config_file == '.':
        raise RuntimeError('Can not be found the file "%s" . The path must be '
                           'relative from where you are '
                           'executing the program, as well as a full path.' % config_file)
    config = yaml.load(open(config_file, 'r'))
    cvg = GenTask(config)
    cvr = Process(cvg.taskConfig, cvg.docdata)
    cvr.render()
    print("Generated {name}".format(name=cvg.taskConfig.fullOutFileName))
    return cvg.taskConfig.fullOutFileName


def main():
    """ Main function load a config file with the info of what template and
    where find it, and the data to pass to it.
    @return nothing, generates files.
    """
    CML_ARGS = create_cml_parser().parse_args()
    makecv(CML_ARGS.cv_file)

# TODO check for variables in template not used or data not used in template. jinja2.meta.find_undeclared_variables(ast)

if __name__ == "__main__":

    main()
