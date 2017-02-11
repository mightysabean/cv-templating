# -*- coding: utf-8 -*-

import os
import yaml

from mcv.mcvutils import fileext, csv2dict


class DataExtractor:
    """Data extractor to feed CVGenerator
    It can be easy to modify this class for obtain the data from other sources,
    for instance, from databases."""

    def __init__(self, basedir, datafiles):
        """Constructor for CVData
        Require list of files
        """
        self.__baseDir = basedir
        self.__data_files = datafiles
        self.__data = self.__extract_data()

    def get(self):
        """Devuelve el diccionario necesario para que se integre en el context a pasar
        al render de jinja2.
        Los nombres de las variables deben coincidir con los usados en los templates
        de jinja2."""
        return self.__data

    def __extract_data(self):
        """Extract data from data YAML files referenced in data section in config file"""
        # TODO raise exception and finish if something is missing or no data
        datadict = {}
        for d in self.__data_files:
            f = os.path.join(
                self.__baseDir,
                self.__data_files.get(d)
            )
            # Add otros formatos de archivo si se necesita.
            if fileext(f) == '.csv':
                datadictsinglefile = {d: csv2dict(open(f, 'r'))}
            else:
                datadictsinglefile = {d: yaml.load(open(f, 'r'))}

            datadict.update(datadictsinglefile)
        return datadict

