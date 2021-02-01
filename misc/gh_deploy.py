#!/usr/bin/env python
 
import sys
import os
import re
import datetime

langs = ['en']

  
def cmd(s):
  print("")
  print(s)
  print("----------------------------")
  r = os.system(s)
  if r != 0: 
    print("Exit update due to previous error")
    exit(-1)
    
cmd("git config alias.ci commit")
cmd("git config alias.br branch")
cmd("git clean -fdX")
cmd("git restore .")
cmd("git checkout script")
cmd("git pull origin script")
    
    
for br in [ 'dev', 'latest', 'release/v7' ]:
  tmpdir = "_docs_tmp_" + re.sub('/', '_', br)
  urlpath = re.sub('release/', '', br)

  print("")
  print("Update " + br)
  print("========================")


  cmd("git checkout " + br + " --")
  cmd("git clean -fdX")
  cmd("git restore .")
  cmd("git pull origin " + br)
  cmd("git submodule update")
  cmd("./build.py trans")
  os.system("git commit -am 'Rebuild'")
  cmd("rm -fr ../" + tmpdir)

  for l in langs:
    if os.path.isdir("./" + l):
      cmd("mkdir -p  ../" + tmpdir + "/" + l + "/")
      cmd("cp -r " + l +"/ ../" + tmpdir + "/")
    
  cmd("git restore .")
  cmd("git checkout script")
  cmd("git clean -fdX")
  
  for l in langs:
    cmd("rm -rf " + urlpath + "/" + l)
  
  cmd("mkdir -p build_output")
  cmd("cp -r ../" + tmpdir + "/. build_output/" + urlpath + "/")

cmd("mkdir -p build_output")
cmd("cp index.html build_output/index.html")
cmd(f'echo "<!-- {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} -->" >> build_output/index.html')
