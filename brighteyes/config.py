from __future__ import print_function
import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

cfgfile = os.path.expanduser('~/.brighteyes')

if not os.path.exists(cfgfile):
    parser = configparser.SafeConfigParser()
    parser.add_section('last')
    parser.set('last', 'brightness', '1.0')
    parser.write(open(cfgfile, 'w'))

parser = configparser.SafeConfigParser()

def cfgget(section, option):
    parser.read(cfgfile)
    return parser[section][option]

def cfgset(section, option, value=None):
    parser.set(section, option, value)
    parser.write(open(cfgfile, 'w'))