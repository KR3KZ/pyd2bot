import atexit
import os
from core.bot import MobsFarmer


def tearDown(thread):
    thread.interrupt()
    thread.join()


if __name__ == "__main__":
    from core import utils, Zone, env
    import logging

    work_dir = os.path.dirname(os.path.abspath(__file__))
    graph_file = os.path.join(work_dir, 'cache.yaml')
    log_file = os.path.join(work_dir, 'bot.log')

    red_worms_patterns_dir = os.path.join(work_dir, "larve_patterns")

    logging.basicConfig(filename=log_file,
                        level=logging.DEBUG,
                        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S')

    red_worm_patterns = utils.loadPatternsFromDir(red_worms_patterns_dir)

    sournoiserie = {
        "range": 6,
        "nbr": 3,
        "shortcut": "z"
    }

    lancer_de_piece = {
        "range": 15,
        "nbr": 5,
        "shortcut": "z"
    }

    # tl = (8, -21)
    # br = (12, -15)

    top_left = (3, -14)
    bot_right = (11, -9)
    zone = Zone(top_left, bot_right)

    bot = MobsFarmer(zone, lancer_de_piece, red_worm_patterns, graph_file, "John-shooter")
    atexit.register(tearDown, bot)

    env.focusDofusWindow()
    bot.start()
    bot.join()
    env.focusIDEWindow()
