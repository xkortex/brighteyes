from __future__ import print_function
from utils import nop

class Macros(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.pv = print if verbose else nop


