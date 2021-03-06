#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_AderPlotter426251Test(winformsTestCase):
    testcaseid = 426251
    command = 'AderPlotter'
    message = 'Add the Plot y=sin(x)'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
