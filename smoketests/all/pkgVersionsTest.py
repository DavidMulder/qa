#!/usr/bin/python

import sys
import os

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)
import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import *

from pkgVersionsTest_data import *


####################################################################
#
#    pkgVersionsTestCase class
#

class pkgVersionsTestCase(smokeTestCase):
    testcaseid = 0

    def test(self):
        for pkg in pkgs.keys():
            out = executeCmd(pkg)[0]
            if out.find(pkgs[pkg]) < 0:
                self.fail("Bad version of package\n\t '%s' != '%s'" % (pkg,pkgs[pkg]))


if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab: