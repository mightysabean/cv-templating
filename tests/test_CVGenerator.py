import os

import pytest
import yaml

from context import mcv
import context
from mcv.GenTask import GenTask
from mcv.Process import Process
from mcv.TaskConfig import TaskConfig
import mcv.mcv

path_where_run_test = os.path.dirname(os.path.realpath(__file__))
minimalConfigFileLatex = os.path.join(path_where_run_test, 'eucv_en_latex_min.yaml')
minimalConfigFileHTML = os.path.join(path_where_run_test, 'eucv_en_html_min.yaml')
examples_config_file_html = os.path.join(context.absparentpath, 'mcv/examples/eucv_en_html.yaml')
examples_config_file_latex = os.path.join(context.absparentpath, 'mcv/examples/eucv_en_latex.yaml')


def load_config_dict(config_file):
    return yaml.load(open(config_file, 'r'))


def load_case(pathtest, config_file):
    """Test of class CVGenerator.
            loads a minimal config example."""
    config = yaml.load(open(config_file, 'r'))
    config['config']['base_dir'] = pathtest
    return GenTask(config)


def test_file_config_not_exists_then_raise_system_exit_error():
    with pytest.raises(RuntimeError):
        mcv.mcv.main()


def test_file_config_open():
    """Given minimal config file, open the file and get some info."""

    with open(minimalConfigFileLatex, 'r') as mcf:
        l = mcf.readline().split(sep=' ')[5]
        assert l == 'test.\n'


def test_check_absence_of_one_of_the_config_sections_raises_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_config_f = {'config': 'a', 'doc': 'b'}  # falta 'data'
    with pytest.raises(RuntimeError):
        TaskConfig(t_config_f)


def test_check_config_variables_in_config_section_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir': 'a',
              'template_dir': 'b'}  # faltan 'output_dir', 'template_file', 'template_type', 'output_filename'
    with pytest.raises(RuntimeError):
        TaskConfig(t_cf_f)


def test_check_bad_base_dir_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir': None,
              'template_dir': 'b',
              'output_dir': '',
              'template_file': '',
              'template_type': '',
              'output_filename': ''}
    with pytest.raises(RuntimeError):
        TaskConfig(t_cf_f)


def test_check_bad_base_dir_plus_output_dir_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir': path_where_run_test,
              'template_dir': 'b',
              'output_dir': None,
              'template_file': '',
              'template_type': '',
              'output_filename': ''}
    with pytest.raises(RuntimeError):
        TaskConfig(t_cf_f)


def test_check_not_found_template_raise_exception():
    """Check RuntimeError if not all sections in config dict"""
    t_cf_f = {'base_dir': path_where_run_test,
              'template_dir': None,
              'output_dir': 'output/latex',
              'template_file': '',
              'template_type': '',
              'output_filename': ''}
    with pytest.raises(RuntimeError):
        TaskConfig(t_cf_f)


def test_html_example_is_generated():
    config = yaml.load(open(examples_config_file_html, 'r'))
    cvg = mcv.mcv.GenTask(config)
    cvr = mcv.mcv.Process(cvg.taskConfig, cvg.docdata)
    cvr.render()
    name = cvg.taskConfig.fullOutFileName
    assert os.path.exists(name) is True


def test_latex_example_is_generated():
    config = yaml.load(open(examples_config_file_latex, 'r'))
    cvg = mcv.mcv.GenTask(config)
    cvr = mcv.mcv.Process(cvg.taskConfig, cvg.docdata)
    cvr.render()
    name = cvg.taskConfig.fullOutFileName
    assert os.path.exists(name) is True


def test_data_csvfile_is_loaded():
    config = yaml.load(open(minimalConfigFileLatex, 'r'))
    config['config']['base_dir'] = path_where_run_test
    cvg = mcv.mcv.GenTask(config)
    assert cvg.docdata['acadinfocurses'][1]['name'] == " 4065 the csv"


def test_pdf_is_generated():
    """ If arara: true in config file with arara installed then check PDF is generated.
    If there are resources (images for instance) specified, check they are copied to output dir and folder."""
    cvg = load_case(path_where_run_test, minimalConfigFileLatex)
    cvr = mcv.mcv.Process(cvg.taskConfig, cvg.docdata)
    cvr.render()
    name = cvg.taskConfig.fullPDFFileName
    assert os.path.exists(name) is True


# def test_main():
#     config = os.path.join(path_where_run_test, examples_config_file_latex)
#     name = mcv.mcv.makecv(config)
#     assert os.path.exists(name) is True
