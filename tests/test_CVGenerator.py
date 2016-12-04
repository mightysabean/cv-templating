import os
import pytest
import mcv_c
import yaml

pathtest = os.path.dirname(os.path.realpath(__file__))
minimalConfigFile = os.path.join(pathtest, 'eucv_en_latex_min.yaml')

def loadMinimalCase(pathtest, minimalConfigFile):
    """Test of class CVGenerator.
            loads a minimal config example."""
    config = yaml.load(open(minimalConfigFile, 'r'))
    config['config']['base_dir'] = pathtest
    return mcv_c.CVGenerator(config)

# def test_render(self):
#     """Test that method render works with a minimal example"""
#     self.fail()
#
# def test_render_latex(self):
#     self.fail()
#
# def test_render_html(self):
#     self.fail()
#
# def test___init__(self):
#     self.fail()

def test_check_absence_of_one_of_the_config_sections_raises_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_config_f = {'config':'a','doc':'b'} # falta 'data'
    with pytest.raises(RuntimeError):
        loadMinimalCase(pathtest, minimalConfigFile).check_config_sections(t_config_f)

def test_check_config_variables_in_config_section_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir':'a','template_dir':'b'} # faltan 'output_dir', 'template_file', 'template_type', 'output_filename'
    with pytest.raises(RuntimeError):
        loadMinimalCase(pathtest, minimalConfigFile).check_config_data(t_cf_f)

def test_check_bad_base_dir_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir':None,'template_dir':'b', 'output_dir':'', 'template_file':'', 'template_type':'', 'output_filename':''}
    with pytest.raises(RuntimeError):
        loadMinimalCase(pathtest, minimalConfigFile).check_config_data(t_cf_f)

def test_check_bad_base_dir_plus_output_dir_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir':pathtest,'template_dir':'b', 'output_dir':None, 'template_file':'', 'template_type':'', 'output_filename':''}
    with pytest.raises(RuntimeError):
        loadMinimalCase(pathtest, minimalConfigFile).check_config_data(t_cf_f)

def test_check_not_found_template_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir':pathtest,'template_dir':None, 'output_dir':'output/latex', 'template_file':'', 'template_type':'', 'output_filename':''}
    with pytest.raises(RuntimeError):
        loadMinimalCase(pathtest, minimalConfigFile).check_config_data(t_cf_f)