#!/usr/bin/env python

import sys, unittest, os

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import *


class verifyReposCanRefresh(smokeTestCase):
    testcaseid = 546327

    def test(self):
        self.canZypperReposBeRefreshed()

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
