#!/usr/bin/python

#############Written by Srinivas Karthik##################
# Usage ./findhtmltags.py <siteurl>  <tagname>
# Eg:To display all a-tags, #./findhtmltags.py https://google.com a
#


from bs4 import BeautifulSoup

import urllib
import sys

input_url = sys.argv[1]
res= urllib.urlopen("https://demo.testfire.net/index.jsp")

bt = BeautifulSoup(res.read(), "lxml")

input_tag = sys.argv[2]
atags= bt.find_all(input_tag)
print "-----------------------------------------------------------------"
print "*********Showing all \""+input_tag+"\" tags for the site: "+input_url
print "****************************************************************"
print "-----------------------------------------------------------------"
for i in range(len(atags)):
    print atags[i]
print "------------------------------------------------------------------"
print "Site Entered was: "+ input_url
print "tag Entered was: " +input_tag+" tag"
print"-------------------------------------------------------------------"




