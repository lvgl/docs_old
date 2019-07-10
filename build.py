#!/usr/bin/env python

import sys
import os


cmd_clean = " echo '--------\nClean up...\n--------'; rm -r html xetex; "
cmd_html =  " echo '--------\nBuild HTML...\n--------'; sphinx-build -b html . html; "
cmd_pdf =   " echo '--------\nBuild_PDF...\n--------'; sphinx-build -b latex . xetex && cd xetex; xelatex *.tex; cp LittlevGL.pdf ../LittlevGL.pdf; cd ..; "

cmd_build = cmd_clean +  cmd_html + cmd_pdf + " "
cmd_en = " echo '********\nStart English\n********'; cd en; " + cmd_build + " cd ..; "
cmd_tr = " echo '********\nStart Turkish\n********'; cd tr; " + cmd_build + " cd ..; "
cmd_zh = " echo '********\nStart Chinese\n********'; cd zh; " + cmd_build + " cd ..; "

os.system(cmd_en + cmd_tr + cmd_zh)
