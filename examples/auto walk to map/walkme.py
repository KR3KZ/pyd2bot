from core import env
from core.bot import Walker

character_name = "John-shooter"

bot = Walker(character_name)

env.focusDofusWindow(character_name)

# bot.moveToMap((-20, -20))
# bot.moveToMap((-19, -11))
bot.moveToMap((-17, -47))

