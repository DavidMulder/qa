#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase
import unittest, time, re

class WebControls_WebRadioButtonList(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838907
        else:
            self.testcaseid = 861814

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_radiobuttonlist")
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_checked("//*[@id=\"rbl1_0\"]"))
            sel.click("rbl1_0")
            self.failUnless(sel.is_checked("//*[@id=\"rbl1_0\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl1_1\"]"))
            sel.click("rbl1_1")
            self.failUnless(sel.is_checked("//*[@id=\"rbl1_1\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl1_0\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl1_2\"]"))
            sel.click("rbl1_2")
            self.failUnless(sel.is_checked("//*[@id=\"rbl1_2\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl1_3\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl1_3\"]"))
            sel.click("rbl1_3")
            self.failUnless(sel.is_checked("//*[@id=\"rbl1_3\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl1_2\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl1_5\"]"))
            sel.click("rbl1_5")
            self.failUnless(sel.is_checked("//*[@id=\"rbl1_5\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl1_3\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl2_0\"]"))
            sel.click("rbl2_0")
            self.failUnless(sel.is_checked("//*[@id=\"rbl2_0\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl2_1\"]"))
            sel.click("rbl2_1")
            self.failUnless(sel.is_checked("//*[@id=\"rbl2_1\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl2_0\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl2_2\"]"))
            sel.click("rbl2_2")
            self.failUnless(sel.is_checked("//*[@id=\"rbl2_2\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl2_3\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl2_3\"]"))
            sel.click("rbl2_3")
            self.failUnless(sel.is_checked("//*[@id=\"rbl2_3\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl2_2\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl2_5\"]"))
            sel.click("rbl2_5")
            self.failUnless(sel.is_checked("//*[@id=\"rbl2_5\"]"))
            self.failIf(sel.is_checked("//*[@id=\"rbl2_3\"]"))
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
