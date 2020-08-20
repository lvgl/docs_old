#!/usr/bin/env python
 
import sys
import os
import re

langs = ['en']

  
def cmd(s):
  print("")
  print(s)
  print("----------------------------")
  r = os.system(s)
  if r != 0: 
    print("Exit update due to previous error")
    exit(-1)
    
        
cmd("git pull origin master")
    
br_arr = sys.argv[1:]
    
for br in br_arr:
  
  tmpdir = "_docs_tmp_" + re.sub('/', '_', br)
  urlpath = re.sub('release/', '', br)

  print("")
  print("Update " + br)
  print("========================")


  cmd("git co " + br)
  cmd("git clean -fd")
  cmd("git pull origin " + br)
  cmd("git submodule update")
  cmd("./build.py trans")
  os.system("git ci -am 'Rebuild'")
  cmd("git push origin " + br)
  cmd("rm -fr ../" + tmpdir)

  for l in langs:
    if os.path.isdir("./" + l):
      cmd("mkdir -p  ../" + tmpdir + "/" + l + "/")
      cmd("cp -r " + l +"/ ../" + tmpdir + "/")
    
  cmd("git co master")
  cmd("git clean -fd")
  
  for l in langs:
    cmd("rm -rf " + urlpath + "/" + l)
  
  cmd("cp -r ../" + tmpdir + "/. " + urlpath + "/")
  cmd("git add " + urlpath)
  os.system("git ci -m 'Update " + urlpath + "'")
  
cmd("git push origin master")
