# -*- coding: utf-8 -*-
import csv
import os

import sys
import yaml

from mcv.mcvutils import fileext


class CVData():
    """Data extractor to feed CVGenerator
    It can be easy to modify this class for obtain the data from other sources,
    for instance, from databases."""

    def __init__(self, basedir, datafiles):
        """Constructor for CVData
        Require list of files
        """
        self.__baseDir = basedir
        self.__data_files = datafiles
        self.__data = self.__extractData()

    def get(self):
        """Devuelve el diccionario necesario para que se integre en el context a pasar
        al render de jinja2.
        Los nombres de las variables deben coincidir con los usados en los templates
        de jinja2."""
        return self.__data

    def __extractData(self):
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
                datadictsinglefile = {d: self.__csv2dict(f)}
            else:
                datadictsinglefile = {d: yaml.load(open(f, 'r'))}

            datadict.update(datadictsinglefile)
        return datadict

    def __csv2dict(self, f):
        """Convert data in csv format to YAML list.

        No se hacen comprobaciones de correccion del csv

        El csv debe tener header con nombres que vayan a ser compatibles con variables
        en el template de jinja2. Lo que se hace es una traduccion de cada fila a una
        entrada de diccionario con keys los nombres de columna y value el de las celdas."""

        listRows = []
        if (sys.version_info[0] > 2):
            kw = {'delimiter': ','}
        else:
            kw = {'delimiter': ',', 'encoding': 'utf-8'}
        rows = csv.reader(f, **kw)
        for i, row in enumerate(rows):

            if (i == 0):
                headers = row
            else:
                listRows.append(row)

        listData = []
        for row in listRows:
            listData.append(dict(zip(headers, row)))
        return listData