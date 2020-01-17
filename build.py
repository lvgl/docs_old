#!/usr/bin/env python

import sys
import os


langs = ['en', 'tr', 'zh-CN', 'hu', 'fr']

clean = 0
args = sys.argv[1:]
if len(args) == 1:
  if args[0] == "clean": clean = 1
  else:
    print("Unknown option. Usage: ./build.py [clean]") 


if clean:
  cmd_clean = " echo 'Clean up...\n'; rm -r html xetex; "
else: 
  cmd_clean = ""
  
cmd_pdf =   " echo '------------\nBuild PDF...\n------------'; sphinx-build -b latex . xetex && cd xetex; xelatex -interaction=batchmode *.tex; xelatex -interaction=batchmode *.tex;  cp -f LittlevGL.pdf ../LittlevGL.pdf; cd ..; "
cmd_html =  " echo '------------\nBuild HTML...\n------------'; sphinx-build -b html . html; "

cmd_build = cmd_clean + cmd_pdf + cmd_html + " "

for lang in langs:
  cmd = " echo '\n\n************\nStart " + lang + "\n************'; cd " + lang + "; " + cmd_build + " cd ..; "
  os.system(cmd)
  
  
