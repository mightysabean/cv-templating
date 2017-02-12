# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
from distutils.dir_util import copy_tree
from distutils.dir_util import mkpath


from mcv.mcvutils import copy_resources


class Process:
    """

    """
    def __init__(self, taskconfig, docdata):
        self.taskconfig = taskconfig
        self.docdata = docdata
        self.streamProduced = ''

    def render(self):
        """Produce the destination file from template and data. Chose what method to use from template type."""
        if self.taskconfig.templatetype == 'latex':
            self.streamProduced = self.render_latex()
        elif self.taskconfig.templatetype == 'html':
            self.streamProduced = self.render_html()

        with open(self.taskconfig.fullTmpFileName, 'w') as o:
            o.write(self.streamProduced)

        copy_resources(self.taskconfig.baseDir, self.taskconfig.tempDir, self.taskconfig.resources_to_build)

        if self.taskconfig.templatetype == 'latex' and self.taskconfig.cf['arara']:
            p = subprocess.Popen(['arara', '-v', self.taskconfig.fullTmpFileName], cwd=self.taskconfig.tempDir)
            p.wait()

        self.copy_artifacts_to_output()
        copy_resources(self.taskconfig.baseDir, self.taskconfig.full_output_dir, self.taskconfig.resources_to_output)

        return True

    def render_latex(self):
        """"""
        import mcv.jinjatex
        return mcv.jinjatex.render_tex(self.taskconfig.templateBaseDir, self.taskconfig.templateFile, doc=self.docdata)

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
        artifacts_generated = []
        if not os.path.isdir(self.taskconfig.full_output_dir):
            mkpath(self.taskconfig.full_output_dir)
        for art_type, ext in self.taskconfig.artifactExtensions.items():
            try:
                artifacts_generated.append(
                    shutil.copy(
                        self.taskconfig.fullTmpFileNameWOExt + ext,
                        self.taskconfig.full_output_dir))
            except Exception as e:
                # Avoid show as error copy of html when Latex. TODO modif comportamiento. That will no show real errors
                pass

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

