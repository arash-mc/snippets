import sys
# change file extension
import re
import shutil
import os
args = sys.argv
from_ = args[1]
to = args[2]
for file in os.listdir('.'):
    if file[-3:] == from_:
        print(file)
        new_file = file[:-3] + to
        print(new_file)
        shutil.move(file, new_file)
