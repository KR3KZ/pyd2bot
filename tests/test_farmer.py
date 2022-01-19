import logging
import os
workdir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(workdir, 'bot.log')
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S')
from pyd2bot.logic.bot.resourceFarmer import ResourceFarmer 
from pyd2bot.logic.world.zone import Zone
from pyd2bot.logic.world import env
spell = {
    "range": 13,
    "nbr": 4,
    "shortcut": "z"
}
zone = Zone("testZone")
zone_zaap = {
    "name": "plaines rocheuses",
    "coords": (-17, -47)
}
zone.addSquare((-15, -59), (-12, -45))
myBot = ResourceFarmer(zone, zone_zaap, spell, workdir, "testbot")
myBot.zone = zone
myBot.startZaap = zone_zaap
myBot.start()    
myBot.join()
env.focusIDEWindow()

