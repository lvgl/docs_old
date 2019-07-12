#!/usr/bin/env python

import sys
import os

src_dir = 'trans_txt'
folders = ['overview', 'get-started', 'object-types', 'porting'];
files = ['index.md'];

os.system("rm -r " + src_dir);
os.system("mkdir " + src_dir);

for f in folders:
  cmd = "cp -r " + f + " " + src_dir + "/" + f
  print(cmd)
  os.system(cmd);


for f in files:
  cmd = "cp " + f + " " + src_dir + "/" + f
  print(cmd)
  os.system(cmd);


cmd = "rename 's/\.md/\.md\.txt/' " + src_dir + "/**/*.md"
print(cmd)
os.system(cmd);

cmd = "rename 's/\.md/\.md\.txt/' " + src_dir + "/*.md"
print(cmd)
os.system(cmd);
  
  
cmd = "zanata-cli push --file-types PLAIN_TEXT -B"
print(cmd)
os.system(cmd);

  
  
