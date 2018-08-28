from __future__ import print_function
from .utils import nop
from .xrandr import Xrandr


class Monitors(object):
    """Abstraction of active monitors. Functions called apply to all monitors equally."""
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.pv = print if verbose else nop
        # self.brightness = Xrandr().get_brightness()


    @property
    def active(self):
        return Xrandr().get_connected()

    @property
    def brightness(self):
        return Xrandr().get_brightness()

    @brightness.setter
    def brightness(self, val):
        xr = Xrandr()
        [xr.set_brightness(mon, val) for mon in self.active]


