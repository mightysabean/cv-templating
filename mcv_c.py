import os
import datetime
import yaml
import mcv_utils
import jinjatex

class CVGenerator():
    """Generator of cv from templates in jinja"""

    __validTemplateTypes = ('html', 'latex')
    __extensions = {
        'html': '.html',
        'latex': '.tex'
    }
    __requiredSections = ('config', 'doc', 'data')
    __requiredKeysInConfigSection = (
        'base_dir','output_dir', 'template_file', 'template_base_dir', 'template_type', 'output_filename'
    )

    def __init__(self,config):
        """Constructor for CVGenerator"""

        # config section
        self.check_config_sections(config)
        self.__cf = config['config']
        self.check_config_data(self.__cf)
        self.__mapConfigData(self.__cf)

        # Doc section
        self.__doc = config['doc']

        # Data section
        self.__data_files = config['data']
        self.__data = self.__extractData()
        self.__docdata = mcv_utils.merge_two_dicts(self.__doc, self.__data)


    def __mapConfigData(self, cf):
        """Assign values from config section in config file to private variables"""
        # TODO raise exception and finish if something is missing
        self.__templateBaseDir = cf['template_base_dir']
        self.__templateFile = cf['template_file']
        self.__templateType = cf['template_type'].lower()  # TODO check if valid type
        if self.__templateType not in self.__validTemplateTypes:
            raise RuntimeError('Unknown type of template type. Valid types are %s .', self.__validTemplateTypes)
        self.__baseDir = cf['base_dir']
        self.__outputDir = cf['output_dir']
        self.__fullOutputDir = os.path.join(
            self.__baseDir,
            self.__outputDir
        )
        self.__outFile = cf['output_filename']
        self.__date = datetime.datetime.strftime(
                            datetime.datetime.now(),
                            "%Y-%m-%d-T-%H-%M")
        self.__fullOutFileName = os.path.join(self.__fullOutputDir,
                                              self.__outFile + self.__date + self.__extensions.get(self.__templateType))


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


    def render(self):
        """Produce the destination file from template and data. Chose what method to use from template type."""
        renders = {'html': self.render_html, 'latex': self.render_latex}
        self.__streamProduced = renders.get(self.__templateType, "")

        with open(self.__fullOutFileName, 'w') as o:
            o.write(self.__streamProduced)


    def render_latex(self):
        """"""
        return jinjatex.render_tex(self.__templateBaseDir, self.__templateFile, doc=self.__docdata)


    def render_html(self):
        """"""

    def check_config_sections(self, dictconfig):
        """Check config section has the three main sections"""
        for k in self.__requiredSections:
            if k not in dictconfig:
                raise RuntimeError("Config file must have these sections: %s" % ", ".join(self.__requiredSections))

    def check_config_data(self, cf):
        """Check data in config section is correct"""

        # All main section keys are in config section
        for k in self.__requiredKeysInConfigSection:
            if k not in cf:
                raise RuntimeError("Config file must have the key: %s" % k)

        # Exists base_dir
        if not os.path.exists(cf['base_dir']):
            raise RuntimeError('base_dir %s in config file does not exists' % cf['base_dir'])

        # Exists output_dir
        if not os.path.exists(os.path.join(cf['base_dir'], cf['output_dir'])):
            raise RuntimeError(
                'base_dir + output_dir (%s + %s) in config file is not valid. If not exists, please make it.' % cf['config'])

        # Exists template_file
        # if not os.path.exists(os.path.join(cf['base_dir'], cf['template_dir'], cf['template_file'])):
        #     raise RuntimeError(
        #         'base_dir + template_dir + template_file (%s + %s + %s) in config file is not valid. If not exists, please make it.' % cf['config'])