
from __future__ import print_function
import os
import argparse
import yaml
import mcv_c


def create_parser():
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
        "config_file",
        help="File .yaml with specifications of the data and template to use."
             "You must have one of this config file for each combination of "
             "format, language or data contents. You have various examples of "
             "config files in the directory examples."
        )
    return cml


def main(config_file):
    """ Main function load a config file with the info of what template and
    where find it, and the data to pass to it.
    @return nothing, generates file.
    """
    if not os.path.exists(config_file):
        raise RuntimeError('Can not be found the file "%s" . The path must be '
                           'relative from where you are '
                           'executing the program, as well a full path.' % config_file)
    config = yaml.load(open(config_file, 'r'))
    cvg = mcv_c.CVGenerator(config)
    cvg.render()


if __name__ == "__main__":
    CML_ARGS = create_parser().parse_args()
    main(CML_ARGS.config_file)
