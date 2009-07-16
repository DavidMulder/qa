#!/usr/bin/python

import sys,os
import unittest
import traceback
import subprocess
import uuid

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(filepath))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)
import common.monotesting as mono
from smokeTestCase import smokeTestCase
from common.helpers import *


####################################################################
#
#    xsp1TestCase class
#

class gmcs2TestCase(smokeTestCase):
    testcaseid = 0

    def test(self):
        u = uuid.uuid1()
        greeting = "Hello World %s" % u.hex # Generate a unique Hello world greeting
        code = '''
using System;
using System.Collections.Generic;
using System.IO;
using System.Net;

class m
{
    public static void Main(){
        List<string> l = new List<string>();
        l.Add("%s");

        foreach (string s in l)
        {
            Console.WriteLine(s);
        }
    }
}
''' % greeting

        f = open('list.cs','w')
        f.write(code)
        f.close()

        executeCmd('gmcs -out:list_cs.exe list.cs')
        out = executeCmd('mono list_cs.exe')
        self.assertEqual(greeting,out[0].strip())

    def tearDown(self):
        self.remove('list.cs')
        self.remove('list_cs.exe')


if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab: