import os
import sys

absparentpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.insert(0, absparentpath)

import mcv.mcv as mcv