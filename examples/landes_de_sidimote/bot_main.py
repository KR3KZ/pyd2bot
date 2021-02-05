import atexit
import datetime
import os

import yaml

from core.bot import ResourceFarmer


def tearDown(thread):
    thread.interrupt()
    thread.join()


if __name__ == "__main__":
    from core import Zone, env
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
    today_save_file = os.path.join(saves_dir, "sidimote_11_12_2020.yaml")

    lancer_de_piece = {
        "range": 13,
        "nbr": 4,
        "shortcut": "z"
    }

    sidimote = Zone("sidimote")

    zone_zaap_coords = (-25, 12)

    sidimote.loadFromFile(today_save_file, patterns_dir)

    # sidimote.cleanEmptyMaps()
    # #
    # sidimote.save(today_save_file)
    #
    # print(sidimote.canFarmAll())

    bot = ResourceFarmer(sidimote, zone_zaap_coords, lancer_de_piece, work_dir, "John-shooter")
    bot.mapChangeTimeOut = 12
    bot.memoTime = 60 * 5
    bot.famPatternThreshold = 0.85

    atexit.register(tearDown, bot)
    bot.start()
    bot.join()
    env.focusIDEWindow()
