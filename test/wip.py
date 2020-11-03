import pywinauto as pywinauto
import win32con
import win32gui
import yaml
from core.log import Log

log = Log()
try:
    1/0
except Exception as e:
    log.info(exc_info=True)
