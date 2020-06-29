#!/usr/bin/env python
 
import sys
import os
import re

langs = ['en']

  
def cmd(s):
  print("============================================")
  print(s)
  print("============================================")
  r = os.system(s)
  if r != 0: 
    print "Exit build due to previous error"
    exit(-1)
    
    

br = "release/v7"
tmpdir = "_docs_tmp_" + br
urlpath = re.sub('release/', '', br)

cmd("git co " + br)
cmd("git clean -fd")
cmd("git pull origin " + br)
cmd("git submodule update")
cmd("./build.py")
cmd("rm -fr ../" + tmpdir)

for l in langs:
  if os.path.isdir("./" + l):
    cmd("cp -a " + l +" ../" + tmpdir)
  
cmd("git co master")
cmd("git clean -fd")
cmd("cp -a ../" + tmpdir + "/. " + br)
cmd("git ci -am 'Update " + urlpath + "'")
cmg("git push origin master")


