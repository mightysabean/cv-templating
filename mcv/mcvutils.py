import csv
import os

# MIT Licence
import shutil
from distutils.dir_util import copy_tree, mkpath


def get_variable_from_list(search_dict, l):
    dc = search_dict.copy()
    for k in l:
        dc = dc.get(k)
    return dc


def fullname(name, family):
    return name + ' ' + family


def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy.
    http://stackoverflow.com/a/26853961"""
    z = x.copy()
    z.update(y)
    return z


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    http://stackoverflow.com/a/26853961
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def fileext(f):
    name,  ext = os.path.splitext(f)
    return ext


def csv2dict(f):
    """Convert data in csv format to  list of dicts for each row.

    No se hacen comprobaciones de correccion del csv

    El csv debe tener header con nombres que vayan a ser compatibles con variables
    en el template de jinja2. Lo que se hace es una traduccion de cada fila a una
    entrada de diccionario con keys los nombres de columna y value el de las celdas."""
    list_data = []
    reader = csv.DictReader(f)
    for row in reader:
        list_data.append(row)
    return list_data


def copy_resources(src_dir, dest_dir, rscs):
    """Copy resources to temp directory for building, or to output for accompanying results"""

    for src, dest in rscs:

        ffsrc = os.path.join(src_dir, src)
        if not (os.path.exists(ffsrc) or os.path.isdir(ffsrc)):
            raise RuntimeError("Do not find %s", )
        if os.path.isdir(ffsrc):
            copy_tree(ffsrc, os.path.join(dest_dir, dest))
        else:
            fdestdir = os.path.join(dest_dir, os.path.dirname(dest))
            if not os.path.isdir(fdestdir):
                mkpath(fdestdir)
            shutil.copy(ffsrc, os.path.join(fdestdir, os.path.basename(dest)))
    return True

