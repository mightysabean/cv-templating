import os
import glob
import pytest
import mcv_c
import yaml
import mcv

pathtest = os.path.dirname(os.path.realpath(__file__))
minimalConfigFile = os.path.join(pathtest, 'eucv_en_latex_min.yaml')

def loadMinimalCase(pathtest, minimalConfigFile):
    """Test of class CVGenerator.
            loads a minimal config example."""
    config = yaml.load(open(minimalConfigFile, 'r'))
    config['config']['base_dir'] = pathtest
    return mcv_c.CVGenerator(config)


def test_file_config_not_exists_then_raise_runtime_error():
    with pytest.raises(RuntimeError):
        mcv.main("ocnwonvcWOIFNWOVN")


def test_file_config_open():
    """Given minimal config file, open the file and get some info."""

    with open(minimalConfigFile, 'r') as mcf:
        l = mcf.readline().split(sep=' ')[5]
        assert l == 'test.\n'


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

def test_pdf_is_generated():
    # arara: true in config file and arara must be installed
    cvg = loadMinimalCase(pathtest,minimalConfigFile)
    cvg.render()
    name = cvg.fullPDFFileName
    assert os.path.exists(name) == True
    if (cvg.fullOutFileNameWOExt is not None) and (cvg.fullOutFileNameWOExt != '') and (cvg.fullOutFileNameWOExt != '/'):
        for f in glob.glob(cvg.fullOutFileNameWOExt + '*'):
            os.remove(f)

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