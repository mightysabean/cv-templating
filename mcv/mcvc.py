import datetime
import os
import shutil
import subprocess
import tempfile
from distutils.dir_util import copy_tree
from distutils.dir_util import mkpath

import yaml

import jinjatex
from mcv import mcvutils


class CVGenerator():
    """Generator of CV from templates in jinja2"""

    __validTemplateTypes = ('html', 'latex')

    __extensions = {
        'html': '.html',
        'latex': '.tex',
    }

    __artifactExtensions = dict.copy(__extensions)

    __artifactExtensions.update({
        'pdf': '.pdf'
    })

    __requiredSections = ('config', 'doc', 'data')

    __requiredKeysInConfigSection = (
        'base_dir','output_dir', 'template_file', 'template_base_dir', 'template_type', 'output_filename'
    )

    __nonRequiredKeysInConfigSection = ('arara', "resources")


    def __init__(self, config):
        """Constructor for CVGenerator

            :param config YAML file or stream with 3 requiered sections for config the task, the document and data for the template."""

        # Config section --------------------------------------------------------------------------------------------

        # Check no errors in config file
        self.check_config_file_sections(config)

        # Map values of config section to private variables of class CVGenerator for use easy in code
        self.__map_config_section(config['config'])
        self.__check_config_section_data()

        # Doc section -----------------------------------------------------------------------------------------------
        # Do not check in generic use. If customize code, this is the place to insert some checks that depends of the
        # type of document and specific use of it.

        # Add info of document section to context
        self.__doc = config['doc']  # TODO juntar aquí, no dejar para el merge de después

        # Data section  # TODO refactor to mcvdata
        self.__data_files = config['data']
        self.__data = self.__extractData()
        # Add data to context
        self.__docdata = mcvutils.merge_two_dicts(self.__doc, self.__data)  # Ocultar


    def __map_config_section(self, cf):
        """Assign values from config section in config file to private variables"""
        # TODO raise run time exception and finish if something is missing

        self.__cf = cf

        # base directory
        self.__baseDir = cf['base_dir']

        # template
        # address of template dir relative to base dir
        self.__templateBaseDir = os.path.join(self.__baseDir, cf['template_base_dir'])

        # address of template file relative to base dir
        self.__templateFile = cf['template_file']

        self.__templateType = cf['template_type'].lower()

        # temp directory
        if tempfile.gettempdir() == os.getcwd():
            self.__tempDir = os.path.join(os.getcwd(), 'tmp')
            os.mkdir(self.__tempDir)
        else:
            self.__tempDir = os.path.join(tempfile.gettempdir(),'mcv')
            if not os.path.exists(self.__tempDir):
                os.mkdir(self.__tempDir)

        # output
        self.__outFile = cf['output_filename']
        self.__date = datetime.datetime.strftime(
            datetime.datetime.now(),
            "%Y-%m-%d-T-%H-%M-%S")
        self.__OutFileNameWOExt = self.__outFile + self.__date

        self.__outputDir = cf['output_dir']
        self.__full_output_dir = os.path.join(
            self.__baseDir,
            self.__outputDir,
            self.__OutFileNameWOExt
        )


        self.fullTmpFileNameWOExt = os.path.join(self.__tempDir, self.__OutFileNameWOExt)
        self.fullTmpFileName = os.path.join(self.fullTmpFileNameWOExt + self.__extensions.get(self.__templateType))
        self.fullTmpPDFFileName = self.fullTmpFileNameWOExt + '.pdf'
        self.fullOutFileNameWOExt = os.path.join(self.__outputDir, self.__OutFileNameWOExt)
        self.fullOutFileName = os.path.join(
            self.__full_output_dir,
            self.__OutFileNameWOExt + self.__extensions.get(self.__templateType))
        self.fullPDFFileName = os.path.join(self.__full_output_dir,self.__OutFileNameWOExt + '.pdf')


        # resources
        self.__resources = cf['resources']
        self.__resources_to_build = self.__resources['build']
        # self.__resources_to_same_build_dir = self.__resources_to_build['build_directory']
        # self.__resources_to_build.pop('build_directory')
        self.__resources_to_output = self.__resources['output']

#        self.check_resources_exists()


    def __copy_resources(self, src_dir, dest_dir, rscs):
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
                shutil.copy(ffsrc, os.path.join(fdestdir,os.path.basename(dest)))
        return True


    def __copy_resources_from_temp_to_output(self):

        for d, fs in self.__resources_to_output.items():
            if not os.path.exists(os.path.join(self.__outputDir,d)):
                os.mkdir(os.path.join(self.__outputDir,d))
            for f in fs:
                if os.path.isdir(f):
                    copy_tree(os.path.join(self.__tempDir, d, os.path.basename(f)),
                        os.path.join(self.__outputDir, d, os.path.basename(f)))
                else:
                    shutil.copy(
                        os.path.join(self.__tempDir, d, os.path.basename(f)),
                        os.path.join(self.__outputDir, d, os.path.basename(f)))


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
        if self.__templateType=='latex':
            self.__streamProduced = self.render_latex()
        elif self.__templateType=='html':
            self.__streamProduced = self.render_html()

        with open(self.fullTmpFileName, 'w') as o:
            o.write(self.__streamProduced)

        self.__copy_resources(self.__baseDir, self.__tempDir, self.__resources_to_build)

        if self.__templateType=='latex' and self.__cf['arara']:
            p = subprocess.Popen(['arara', '-v', self.fullTmpFileName], cwd=self.__tempDir)
            p.wait()

        self.copy_artifacts_to_output()
        self.__copy_resources(self.__baseDir, self.__full_output_dir, self.__resources_to_output)

        return True


    def render_latex(self):
        """"""
        return jinjatex.render_tex(self.__templateBaseDir, self.__templateFile, doc=self.__docdata)


    def render_html(self):
        """"""
        import jinja2
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(self.__templateBaseDir), lstrip_blocks=True, trim_blocks=True)
        # Render
        template = env.get_template(self.__templateFile)

        return template.render(self.__docdata)

    def copy_artifacts_to_output(self):
        """Copy results in temp to output dir"""
        artifactsGenerated=[]
        if not os.path.isdir(self.__full_output_dir):
            mkpath(self.__full_output_dir)
        for type, ext in self.__artifactExtensions.items():
            try:
                artifactsGenerated.append(
                    shutil.copy(
                        self.fullTmpFileNameWOExt + ext,
                        self.__full_output_dir))
            except:
                pass

    def check_config_file_sections(self, dictconfig):
        """Check config section has the three main sections"""
        for k in self.__requiredSections:
            if k not in dictconfig:
                raise RuntimeError("Config file must have these sections: %s" % ", ".join(self.__requiredSections))

    def __check_config_section_data(self):
        """Check data in config section is correct"""

        # All main section keys are in config section
        for k in self.__requiredKeysInConfigSection:
            if k not in self.__cf:
                raise RuntimeError("Config file must have the key: %s" % k)

        # Exists base_dir
        if not os.path.exists(self.__cf['base_dir']):
            raise RuntimeError('base_dir %s in config file does not exists' % self.__cf['base_dir'])

        # Valid template_type
        if self.__cf['template_type'] not in self.__validTemplateTypes:
            raise RuntimeError('Unknown type of template type. Valid types are %s .', self.__validTemplateTypes)

        # Exists output_dir
        if not os.path.exists(os.path.join(self.__cf['base_dir'], self.__cf['output_dir'])):
            raise RuntimeError(
                'base_dir + output_dir (%s + %s) in config file is not valid. If not exists, please make it.' %
                (self.__cf['base_dir'], self.__cf['output_dir']))

        # Exists template_file
        if not os.path.exists(os.path.join(self.__cf['base_dir'], self.__cf['template_base_dir'], self.__cf['template_file'])):
            raise RuntimeError(
                'base_dir + template_dir + template_file (%s + %s + %s) in config file '
                'is not valid. If not exists, please make it.' %
                (self.__cf['base_dir'], self.__cf['template_base_dir'], self.__cf['template_file']))


    def check_resources_exists(self):
        for r, fs in self.__resources_to_build.items():
            for f in fs:
                if not os.path.exists(os.path.join(self.__baseDir, f)):
                    raise RuntimeError("%s did not finded as pointed in resource section %s" % (f, r))

