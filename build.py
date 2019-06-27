import sys
import os

cmd_build = "rm -r html latex && make html && make latexpdf"
cmd_en = "cd en && " + cmd_build

os.system(cmd_en)
