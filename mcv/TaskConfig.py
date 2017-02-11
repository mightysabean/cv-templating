# -*- coding: utf-8 -*-

"""

"""

import os
import tempfile
import datetime


class TaskConfig:
    """
    Almacena los valores de la tarea que se van a emplear en varios modulos
    """
    __validTemplateTypes = ('html', 'latex')

    __extensions = {
        'html': '.html',
        'latex': '.tex',
    }

    artifactExtensions = dict.copy(__extensions)

    artifactExtensions.update({
        'pdf': '.pdf'
    })

    __requiredSections = ('config', 'doc', 'data')

    __requiredKeysInConfigSection = (
        'base_dir', 'output_dir', 'template_file', 'template_base_dir', 'template_type', 'output_filename'
    )

    __nonRequiredKeysInConfigSection = ('arara', "resources")

    def __init__(self, config):

        """Assign values from config section in config file to private variables"""
        # TODO raise run time exception and finish if something is missing

        # Check no errors in config file
        self.check_config_file_sections(config)

        self.cf = config['config']

        self.__check_config_section_data()

        # Fill fields
        # base directory
        self.baseDir = self.cf['base_dir']

        # template
        # address of template dir relative to base dir
        self.templateBaseDir = os.path.join(self.baseDir, self.cf['template_base_dir'])

        # address of template file relative to base dir
        self.templateFile = self.cf['template_file']

        self.templatetype = self.cf['template_type'].lower()

        # temp directory
        if tempfile.gettempdir() == os.getcwd():
            self.tempDir = os.path.join(os.getcwd(), 'tmp')
            os.mkdir(self.tempDir)
        else:
            self.tempDir = os.path.join(tempfile.gettempdir(), 'mcv')
            if not os.path.exists(self.tempDir):
                os.mkdir(self.tempDir)

        # output
        self.__outFile = self.cf['output_filename']
        self.__date = datetime.datetime.strftime(
            datetime.datetime.now(),
            "%Y-%m-%d-T-%H-%M-%S")
        self.__OutFileNameWOExt = self.__outFile + self.__date

        self.__outputDir = self.cf['output_dir']
        self.full_output_dir = os.path.join(
            self.baseDir,
            self.__outputDir,
            self.__OutFileNameWOExt  # for directory grouping all the output files
        )

        # files in temp directory
        self.fullTmpFileNameWOExt = os.path.join(self.tempDir, self.__OutFileNameWOExt)
        self.fullTmpFileName = os.path.join(self.fullTmpFileNameWOExt + self.__extensions.get(self.templatetype))
        self.fullTmpPDFFileName = self.fullTmpFileNameWOExt + '.pdf'

        # files in output dir
        self.fullOutFileNameWOExt = os.path.join(self.__outputDir, self.__OutFileNameWOExt)
        self.fullOutFileName = os.path.join(
            self.full_output_dir,
            self.__OutFileNameWOExt + self.__extensions.get(self.templatetype))
        self.fullPDFFileName = os.path.join(self.full_output_dir, self.__OutFileNameWOExt + '.pdf')

        # resources
        self.__resources = self.cf['resources']
        self.resources_to_build = self.__resources['build']
        # self.__resources_to_same_build_dir = self.__resources_to_build['build_directory']
        # self.__resources_to_build.pop('build_directory')
        self.resources_to_output = self.__resources['output']

    def check_config_file_sections(self, dictconfig):
        """Check config section has the three main sections"""
        for k in self.__requiredSections:
            if k not in dictconfig:
                raise RuntimeError("Config file must have these sections: %s" % ", ".join(self.__requiredSections))

    def __check_config_section_data(self):
        """Check data in config section is correct"""

        # All main section keys are in config section
        for k in self.__requiredKeysInConfigSection:
            if k not in self.cf:
                raise RuntimeError("Config file must have the key: %s" % k)

        # Exists base_dir
        if not os.path.exists(self.cf['base_dir']):
            raise RuntimeError('base_dir %s in config file does not exists' % self.cf['base_dir'])

        # Valid template_type
        if self.cf['template_type'] not in self.__validTemplateTypes:
            raise RuntimeError('Unknown type of template type. Valid types are %s .', self.__validTemplateTypes)

        # Exists output_dir
        if not os.path.exists(os.path.join(self.cf['base_dir'], self.cf['output_dir'])):
            raise RuntimeError(
                'base_dir + output_dir (%s + %s) in config file is not valid. If not exists, please make it.' %
                (self.cf['base_dir'], self.cf['output_dir']))

        # Exists template_file
        if not os.path.exists(os.path.join(
                self.cf['base_dir'], self.cf['template_base_dir'], self.cf['template_file'])):
            raise RuntimeError(
                'base_dir + template_dir + template_file (%s + %s + %s) in config file '
                'is not valid. If not exists, please make it.' %
                (self.cf['base_dir'], self.cf['template_base_dir'], self.cf['template_file']))

    def check_resources_exists(self):
        for r, fs in self.__resources_to_build.items():
            for f in fs:
                if not os.path.exists(os.path.join(self.__baseDir, f)):
                    raise RuntimeError("%s did not finded as pointed in resource section %s" % (f, r))
