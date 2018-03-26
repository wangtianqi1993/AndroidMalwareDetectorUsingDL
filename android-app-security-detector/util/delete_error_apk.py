#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wtq'

from numpy import *
from optparse import OptionParser
from androguard.core import androconf
from androguard.core.bytecodes import apk

option_0 = {
    'name': ('-i', '--input'),
    'help': 'file : use this filename (APK)',
    'nargs': 1,
}

option_1 = {
    'name': ('-d', '--directory'),
    'help': 'directory : use this directory',
    'nargs': 1,
}

option_2 = {
    'name': ('-t', '--tag'),
    'help': 'display tags',
    'action': 'count',

}

option_3 = {
    'name': ('-v', '--version'),
    'help': 'version',
    'action': 'count',

}

options = [option_0, option_1, option_2, option_3]


def dealapk(options, kwargs):
    print 'waiting...'
    apk_sum = 0
    if options.directory:
        for root, dirs, files in os.walk(options.directory, followlinks=True):
            if files:
                for f in files:
                    real_filename = root
                    if real_filename[-1] != "/":
                        real_filename += "/"
                    real_filename += f
                    ret_type = androconf.is_android(real_filename)
                    if ret_type == "APK":
                        # print os.path.basename(real_filename), ":"

                        try:
                            a = apk.APK(real_filename)
                            if a.is_valid_APK():
                                apk_sum += 1

                            else:
                                print "INVALID"
                                os.remove(real_filename)

                        except Exception, e:
                            print "ERROR", e
                            os.remove(real_filename)
            else:
                print "directory not exists!!!"
    print apk_sum


if __name__ == "__main__":
    parser = OptionParser()
    for option in options:
        param = option['name']
        del option['name']
        parser.add_option(*param, **option)

    options, arguments = parser.parse_args()
    sys.argv[:] = arguments
    dealapk(options, arguments)
