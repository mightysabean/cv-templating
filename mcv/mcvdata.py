import os

import yaml


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
        data = {}
        for d in self.__data_files:
            f = os.path.join(
                self.__baseDir,
                self.__data_files.get(d)
            )
            data.update({d: yaml.load(open(f, 'r'))})
        return data
