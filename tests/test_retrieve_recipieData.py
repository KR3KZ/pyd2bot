from time import perf_counter
from com.ankamagames.dofus import Constants
from com.ankamagames.dofus.datacenter.jobs.Recipe import Recipe
from com.ankamagames.jerakine.data.I18nFileAccessor import I18nFileAccessor
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.data.GameDataFileAccessor import GameDataFileAccessor

logger = Logger(__name__)
t = perf_counter()
I18nFileAccessor().init(Constants.LANG_FILE_PATH)
logger.info(f"Time to load I18n: {perf_counter() - t}")

t = perf_counter()
GameDataFileAccessor().initFromModuleName(Recipe.MODULE)
logger.info(f"Time to load GameData: {perf_counter() - t}")

t = perf_counter()
r = Recipe.getRecipeByResultId(44)
logger.info(f"Time to load Recipe: {perf_counter() - t}")

t = perf_counter()
logger.info(r.resultName)
logger.info(f"Time to load resultName: {perf_counter() - t}")

for ingredient in r.ingredients:
    logger.debug(ingredient.name)
