# -*- coding: utf-8 -*-

"""

"""

import os
from mcv.DataExtractor import DataExtractor
from mcv.TaskConfig import TaskConfig


class Gen():
    """Generator of CV from templates in jinja2"""



    def __init__(self, config):
        """Constructor for CVGenerator

            :param config YAML file or stream with 3 requiered sections for config the task, the document and data for the template."""

        # Config section --------------------------------------------------------------------------------------------

        # Map values of config section to private variables of class CVGenerator for use easy in code
        #self.__map_config_section(config['config'])
        self.taskConfig = TaskConfig(config)


        # Doc section -----------------------------------------------------------------------------------------------
        # Do not check in generic use. If customize code, this is the place to insert some checks that depends of the
        # type of document and specific use of it.

        # Add info of document section to context
        self.docdata = config['doc']

        # Data section
        self.__data_files = config['data']
        data = DataExtractor(self.taskConfig.baseDir, self.__data_files)

        # Add data to context
        self.docdata.update(data.get())





