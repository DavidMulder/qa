#!/usr/bin/env python
import sys,os

sys.path.append('..')
from common.monotesting import *
from common.helpers import *

# sub directories
# Add child test suites to test suite

from all.alltests import *

# Depending on your OS, import the proper subdirectory
myOS = whichOS()
if myOS == 'win32':
    print "Importing Win32 tests"
    from win32.alltests import *
elif myOS == 'linux':
    if not isAppliance():
        print "Importing Linux tests"
    else:
        appType = whichAppliance()
        if appType == "vmware":
            print "Importing VMware Appliance tests"
        elif appType == "vpc":
            print "Importing VirtualPC Appliance tests"
        elif appType == "livecd":
            print "Importing LiveCD Appliance tests"
        else:
            raise Exception("Unknown Appliance Type")
        from appliances.alltests import *
    from linux.alltests import *
elif myOS  == 'macos':
    print "Importing Mac OSX tests"
    from linux.alltests import *
    from macos.alltests import *
    from appliances.alltests import *
else:
    raise Exception("Unknown OS to run smoke tests on")


if __name__ == '__main__':
    monotesting_main()


# vim:ts=4:expandtab:
