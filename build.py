#!/usr/bin/env python

import sys
import os

cmd_build = "rm -r html latex; make html && make latexpdf;  cp ./latex/LittlevGL.pdf LittlevGL.pdf;"
cmd_en = "cd en; " + cmd_build + " cd .."

os.system(cmd_en)
