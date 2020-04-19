#!/usr/bin/env python

import sys
import os


langs = ['en', 'tr', 'zh-CN', 'hu', 'fr']

clean = 0
trans = 0
args = sys.argv[1:]
if len(args) == 1:
  if "clean" in args: clean = 1
  if "trans" in args: trans = 1
  
if clean:
  cmd_clean = " echo 'Clean up...\n'; rm -r html xetex; "
else: 
  cmd_clean = ""
  
if trans:
  os.system("cd en && ./trans_push.py && ./trans_pull.py")  
  
cmd_pdf =   " echo '------------\nBuild PDF...\n------------'; sphinx-build -b latex . xetex && cd xetex; xelatex -interaction=batchmode *.tex; xelatex -interaction=batchmode *.tex;  cp -f LittlevGL.pdf ../LittlevGL.pdf; cd ..; "
cmd_html =  " echo '------------\nBuild HTML...\n------------'; sphinx-build -b html . html; "

cmd_build = cmd_clean + cmd_pdf + cmd_html + " "

for lang in langs:
  cmd = " echo '\n\n************\nStart " + lang + "\n************'; cd " + lang + "; " + cmd_build + " cd ..; "
  os.system(cmd)
  
  
