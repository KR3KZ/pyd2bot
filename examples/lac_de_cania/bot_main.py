import atexit
import datetime
import os
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

    spell = {
        "range": 12,
        "nbr": 4,
        "shortcut": "z"
    }

    character_name = "John-shooter"

    # lac_de_cania = Zone("lac de cania")
    # zone_zaap_coord = (-3, -42)
    # zone_file_path = os.path.join(saves_dir, "lac_cania_24_11_2020.yaml")
    # lac_de_cania.loadFromFile(zone_file_path, patterns_dir)

    bois_de_litneg = Zone("bois de litneg")
    zone_zaap_coords = (-17, -47)
    bois_de_litneg.addSquare((-15, -59), (-11, -45))
    bot = ResourceFarmer(bois_de_litneg, zone_zaap_coords, spell, work_dir, character_name)

    atexit.register(tearDown, bot)
    bot.start()
    bot.join()
    env.focusIDEWindow()
