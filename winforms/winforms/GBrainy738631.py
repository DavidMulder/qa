#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_GBrainy738631Test(winformsTestCase):
    testcaseid = 738631
    command = 'gbrainy'
    message = 'Play a memory game'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
