import os

import pytest
import yaml

import mcv
from mcv import mcvc
from mcv.mcv import main

pathtest = os.path.dirname(os.path.realpath(__file__))
minimalConfigFileLatex = os.path.join(pathtest, 'eucv_en_latex_min.yaml')
minimalConfigFileHTML = os.path.join(pathtest, 'eucv_en_html_min.yaml')
examples_config_file_html = os.path.join(pathtest, '../examples/eucv_en_html.yaml')
examples_config_file_latex = os.path.join(pathtest, '../examples/eucv_en_latex.yaml')

def load_case(pathtest, config_file):
    """Test of class CVGenerator.
            loads a minimal config example."""
    config = yaml.load(open(config_file, 'r'))
    config['config']['base_dir'] = pathtest
    return mcvc.CVGenerator(config)


def test_file_config_not_exists_then_raise_runtime_error():
    with pytest.raises(RuntimeError):
        main("ocnwonvcWOIFNWOVN")


def test_file_config_open():
    """Given minimal config file, open the file and get some info."""

    with open(minimalConfigFileLatex, 'r') as mcf:
        l = mcf.readline().split(sep=' ')[5]
        assert l == 'test.\n'


def test_check_absence_of_one_of_the_config_sections_raises_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_config_f = {'config':'a','doc':'b'} # falta 'data'
    with pytest.raises(RuntimeError):
        load_case(pathtest, minimalConfigFileLatex).check_config_file_sections(t_config_f)

def test_check_config_variables_in_config_section_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir':'a','template_dir':'b'} # faltan 'output_dir', 'template_file', 'template_type', 'output_filename'
    with pytest.raises(RuntimeError):
        m = load_case(pathtest, minimalConfigFileLatex)
        m._CVGenerator__cf.pop('output_dir', None)
        m._CVGenerator__check_config_section_data()

def test_check_bad_base_dir_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir':None,'template_dir':'b', 'output_dir':'', 'template_file':'', 'template_type':'', 'output_filename':''}
    with pytest.raises(RuntimeError):
        m = load_case(pathtest, minimalConfigFileLatex)
        m._CVGenerator__cf = t_cf_f
        m._CVGenerator__check_config_section_data()

def test_check_bad_base_dir_plus_output_dir_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir':pathtest,'template_dir':'b', 'output_dir':None, 'template_file':'', 'template_type':'', 'output_filename':''}
    with pytest.raises(RuntimeError):
        m = load_case(pathtest, minimalConfigFileLatex)
        m._CVGenerator__cf = t_cf_f
        m._CVGenerator__check_config_section_data()

def test_check_not_found_template_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir':pathtest,'template_dir':None, 'output_dir':'output/latex', 'template_file':'', 'template_type':'', 'output_filename':''}
    with pytest.raises(RuntimeError):
        m = load_case(pathtest, minimalConfigFileLatex)
        m._CVGenerator__cf = t_cf_f
        m._CVGenerator__check_config_section_data()

def test_pdf_is_generated():
    """ If arara: true in config file with arara installed then check PDF is generated.
    If there are resources (images for instance) specified, check they are copied to output dir and folder."""
    cvg = load_case(pathtest, minimalConfigFileLatex)
    cvg.render()
    name = cvg.fullPDFFileName
    assert os.path.exists(name) == True

def test_html_example_is_generated():
    config = yaml.load(open(examples_config_file_html, 'r'))
    cvg= mcvc.CVGenerator(config)
    cvg.render()
    name= cvg.fullOutFileName
    assert os.path.exists(name) == True

def test_latex_example_is_generated():
    config = yaml.load(open(examples_config_file_latex, 'r'))
    cvg= mcvc.CVGenerator(config)
    cvg.render()
    name= cvg.fullOutFileName
    assert os.path.exists(name) == True