import os
from subprocess import PIPE, Popen

path ="com"
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        #append the file name to the list
        if file != "__init__.py" and file[0].islower():
            src = os.path.join(root, file)
            dst = os.path.join(root, file[0].upper() + file[1:])
            cmd = ["git", "mv", src, dst]
            print(cmd)
            CURRDIR = os.path.dirname(__file__)
            p = Popen(
                cmd,
                stderr=PIPE,
                stdout=PIPE,
                shell=True,
            )
            stdout, stderr = p.communicate()
            if stderr:
                raise Exception(stderr.decode("utf-8"))

