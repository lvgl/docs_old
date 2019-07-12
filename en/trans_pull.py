#!/usr/bin/env python

import sys
import os

langs = ['tr', 'zh-CN', 'hu']
folders = ['overview', 'get-started', 'object-types', 'porting'];
files = ['index.md'];

for lang in langs:
  for f in folders:
    cmd = "rm -r " + "../" + lang + "/" + f
    print(cmd)
    os.system(cmd);
    
  for f in files:
    cmd = "rm "  + "../" + lang + "/" + f
    print(cmd)
    os.system(cmd);
    
    
cmd = "zanata-cli pull -B"
print(cmd)
os.system(cmd);


for lang in langs:
  cmd = "rename -f 's/\.txt//g' ../" + lang + "/**/*.txt"
  print(cmd)
  os.system(cmd);

  cmd = "rename -f 's/\.txt//g' ../" + lang + "/*.txt"
  print(cmd)
  os.system(cmd);

  
  
