# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
from distutils.dir_util import mkpath
from distutils.dir_util import copy_tree
import jinjatex



class Process:
    """

    """
    def __init__(self, taskconfig, docdata):
        self.taskconfig = taskconfig
        self.docdata = docdata


    def render(self):
        """Produce the destination file from template and data. Chose what method to use from template type."""
        if self.taskconfig.templatetype == 'latex':
            self.streamProduced = self.render_latex()
        elif self.taskconfig.templatetype == 'html':
            self.streamProduced = self.render_html()

        with open(self.taskconfig.fullTmpFileName, 'w') as o:
            o.write(self.streamProduced)

        self.__copy_resources(self.taskconfig.baseDir, self.taskconfig.tempDir, self.taskconfig.resources_to_build)

        if self.taskconfig.templatetype == 'latex' and self.taskconfig.cf['arara']:
            p = subprocess.Popen(['arara', '-v', self.taskconfig.fullTmpFileName], cwd=self.taskconfig.tempDir)
            p.wait()

        self.copy_artifacts_to_output()
        self.__copy_resources(self.taskconfig.baseDir, self.taskconfig.full_output_dir, self.taskconfig.resources_to_output)

        return True

    def render_latex(self):
        """"""
        return jinjatex.render_tex(self.taskconfig.templateBaseDir, self.taskconfig.templateFile, doc=self.docdata)

    def render_html(self):
        """"""
        import jinja2
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(self.taskconfig.templateBaseDir), lstrip_blocks=True,
                                 trim_blocks=True)
        # Render
        template = env.get_template(self.taskconfig.templateFile)

        return template.render(self.docdata)

    def copy_artifacts_to_output(self):
        """Copy results in temp to output dir"""
        artifactsGenerated = []
        if not os.path.isdir(self.taskconfig.full_output_dir):
            mkpath(self.taskconfig.full_output_dir)
        for type, ext in self.taskconfig.artifactExtensions.items():
            try:
                artifactsGenerated.append(
                    shutil.copy(
                        self.taskconfig.fullTmpFileNameWOExt + ext,
                        self.taskconfig.full_output_dir))
            except:
                pass


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
                shutil.copy(ffsrc, os.path.join(fdestdir, os.path.basename(dest)))
        return True


    def __copy_resources_from_temp_to_output(self):
        for d, fs in self.taskconfig.resources_to_output.items():
            if not os.path.exists(os.path.join(self.taskconfig.outputDir, d)):
                os.mkdir(os.path.join(self.taskconfig.outputDir, d))
            for f in fs:
                if os.path.isdir(f):
                    copy_tree(os.path.join(self.taskconfig.tempDir, d, os.path.basename(f)),
                              os.path.join(self.taskconfig.outputDir, d, os.path.basename(f)))
                else:
                    shutil.copy(
                        os.path.join(self.taskconfig.tempDir, d, os.path.basename(f)),
                        os.path.join(self.taskconfig.outputDir, d, os.path.basename(f)))

