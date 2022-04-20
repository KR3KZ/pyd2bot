import site
import os

ROOTDIR = CURR_DIR = os.getcwd()
SITEDIR = site.getsitepackages()[0]
print(SITEDIR)
with open(os.path.join(SITEDIR, "pyd2bot.pth"), "w+") as fp:
    fp.write(ROOTDIR)
