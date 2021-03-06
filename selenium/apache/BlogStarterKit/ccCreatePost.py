#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class BlogStarterKit_cc_CreatePost(apacheTestCase):
    apacheTestCaseId = 710104
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/BlogStarterKit/Admin/Login.aspx?ReturnUrl=%2fBlogStarterKit%2fAdmin%2fDefault.aspx")
            sel.type("ctl00_Content_Login1_UserName", "test")
            sel.type("ctl00_Content_Login1_Password", "test")
            sel.click("ctl00_Content_Login1_RememberMe")
            sel.click("ctl00_Content_Login1_LoginButton")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("link=Manage posts"))
            sel.open("/BlogStarterKit/Admin")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("My Blog"))
            for i in range(60):
                try:
                    if sel.is_element_present("//html/body/form/div[2]/div[2]/div[2]/a"): break
                except: pass
                time.sleep(1)
            sel.click("link=New post")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_Content_PostForm_TitleTextBox", "Mono takes over the world")
            sel.type("ctl00_Content_PostForm_SubTitleEdit", "This is a summary of how Mono took over the world.")
            sel.select("ctl00_Content_PostForm_CategoryDropDown", "label=Technology")
            sel.click("ctl00_Content_PostForm_SaveButton")
            sel.wait_for_page_to_load("30000")
            for i in range(60):
                try:
                    if sel.is_element_present("//div[@id='ContentContainer']/h1"): break
                except: pass
                time.sleep(1)
            self.assertEqual("Posts", sel.get_text("//div[@id='ContentContainer']/h1"))
            sel.click("ctl00_HomeLink")
            sel.wait_for_page_to_load("30000")
	    for i in range(60):
                try:
                    if sel.is_element_present("ctl00_Content_BlogPosts_ctl00_TitleLink"): break
                except: pass
                time.sleep(1)
	    print("2")
            sel.click("ctl00_Content_BlogPosts_ctl00_TitleLink")
	    sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("This is a summary of how Mono took over the world"))
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
