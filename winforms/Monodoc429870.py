#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_Monodoc429870Test(winformsTestCase):
    testcaseid = 429870
    command = 'Monodoc'
    message = 'Search for WriteLine in the Search tab'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
