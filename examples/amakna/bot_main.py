import atexit
import datetime
import os

import yaml

from core.bot import ResourceFarmer


def tearDown(thread):
    thread.interrupt()
    thread.join()


if __name__ == "__main__":
    from core import utils, Zone, env
    import logging

    work_dir = os.path.dirname(os.path.abspath(__file__))

    log_file = os.path.join(work_dir, 'bot.log')
    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S')

    patterns_dir = os.path.join(work_dir, "patterns")
    saves_dir = os.path.join(work_dir, 'saves')
    now = datetime.datetime.now()
    today_save_file = os.path.join(saves_dir, now.strftime("%d_%m_%Y") + ".yaml")

    lancer_de_piece = {
        "range": 12,
        "nbr": 4,
        "shortcut": "z"
    }

    amakna = Zone("amakna")
    amakna.loadFromFile(today_save_file, patterns_dir)

    dragoOeuf = amakna.subZone((-7, 24), (-1, 32))
    save_file = os.path.join(saves_dir, "dragooeuf_23_11_2020.yaml")
    data = dragoOeuf.toDict()
    with open(save_file, 'w') as f:
        yaml.dump(data, f, sort_keys=False)
    # bot = ResourceFarmer(zone, spell, work_dir, "John-shooter")
    #
    # atexit.register(tearDown, bot)
    # bot.start()
    # bot.join()
    # env.focusIDEWindow()
