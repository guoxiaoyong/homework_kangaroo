import glob
import re
import os

def normalize_name(name):
  pattern = '[a-zA-Z0-9]+'
  return '_'.join(seg.lower() for seg in re.findall(pattern, name[:-4])) + '.mp4'

all_files = glob.glob('*.mp4')
for fn in all_files:
  new_fn = normalize_name(fn)
  if fn != new_fn:
    os.rename(fn, new_fn)
