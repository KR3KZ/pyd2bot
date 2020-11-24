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
    today_save_file = os.path.join(saves_dir, "23_11_2020.yaml")

    lancer_de_piece = {
        "range": 12,
        "nbr": 4,
        "shortcut": "z"
    }

    pandala = Zone("lac_de_cania")
    # lac_de_cania.addSquare((19, -38), (28, -19))
    pandala.loadFromFile(today_save_file, patterns_dir)
    # lac_de_cania.resetExcludedSpots()
    bot = ResourceFarmer(pandala, 'pandala', lancer_de_piece, work_dir, "John-shooter")

    atexit.register(tearDown, bot)
    bot.start()
    bot.join()
    env.focusIDEWindow()
