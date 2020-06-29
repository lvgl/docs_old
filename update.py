#!/usr/bin/env python
 
import sys
import os

langs = ['en']

  
def cmd(s):
  print("============================================")
  print(s)
  print("============================================")
  r = os.system(s)
  if r != 0: 
    print "Exit build due to previous error"
    exit(-1)
    
    

br = "dev"
tmpdir = "_docs_tmp_" + br

cmd("git co " + br)
cmd("git clean -fd")
cmd("git submodule update")
cmd("./build.py")
cmd("rm -fr ../" + tmpdir)
cmd("cp -a en ../" + tmpdir)
cmd("git co master")
cmd("git clean -fd")
cmd("cp -a ../" + tmpdir + "/. " + br)

