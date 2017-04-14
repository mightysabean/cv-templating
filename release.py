from distutils.dir_util import copy_tree
from shutil import copyfile
copy_tree('sphinx/_build/html','docs')

copyfile('sphinx/Someone.html','docs/Someone.html')
copyfile('sphinx/Someone.pdf','docs/Someone.pdf')
copy_tree('sphinx/images','docs/images')