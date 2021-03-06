#!/usr/bin/env python

import sys
import os
import unittest
import traceback
import subprocess
import uuid
import tempfile

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import *


####################################################################
#
#    gmcsTestCase class
#

class gmcsTestCase(smokeTestCase):
    testcaseid = 875238

    def setUp(self):
        self.tmpDir = tempfile.mkdtemp()
        self.startDir = os.getcwd()
        os.chdir(self.tmpDir)

    def test(self):
        u = uuid.uuid1()
        greeting = "Hello World %s" % u.hex # Generate a unique Hello world greeting
        code = '''
using System;
class m
{
    public static void Main(){
        Console.WriteLine("%s");
    }
}
''' % greeting

        f = open('helloworld.cs','w')
        f.write(code)
        f.close()

        executeCmd('gmcs -out:helloworld_cs.exe helloworld.cs')
        out = executeCmd('mono helloworld_cs.exe')
        self.assertEqual(greeting,out[0].strip())

    def tearDown(self):
        self.remove('helloworld.cs')
        self.remove('helloworld_cs.exe')
        os.chdir(self.startDir)
        os.rmdir(self.tmpDir)


if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
