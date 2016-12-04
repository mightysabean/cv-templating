import os
import pytest
import mcv

pathtest = os.path.dirname(os.path.realpath(__file__))
minimalConfigFile = os.path.join(pathtest, 'eucv_en_latex_min.yaml')

def test_file_config_not_exists_then_raise_runtime_error():
    with pytest.raises(RuntimeError):
        mcv.main("ocnwonvcWOIFNWOVN")


def test_file_config_open():
    """Given minimal config file, open the file and get some info."""

    with open(minimalConfigFile, 'r') as mcf:
        l = mcf.readline().split(sep=' ')[5]
        assert l == 'test.\n'


def test_base_dir_exists():
    pass


def test_base_dir_Not_exists():
    pass


def test_base_dir_template_exists():
    pass


def test_base_dir_Not_template_exists():
    pass