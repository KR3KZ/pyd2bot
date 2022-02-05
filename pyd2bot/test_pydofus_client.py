from pathlib import Path
from time import sleep
import json
from com.ankamagames.atouin.data.map.map import Map
from com.ankamagames.dofus import Constants
import com.ankamagames.dofus.kernel.Kernel as krnl
from com.ankamagames.dofus.logic.connection.actions.ServerSelectionAction import ServerSelectionAction
import com.ankamagames.dofus.logic.connection.managers.AuthentificationManager as auth
import com.ankamagames.dofus.kernel.net.ConnectionsHandler as connh
from com.ankamagames.dofus.logic.game.approach.actions.CharacterSelectionAction import CharacterSelectionAction
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import PlayedCharacterManager
from com.ankamagames.dofus.modules.utils.pathFinding.world.WorldPathFinder import WorldPathFinder
from com.ankamagames.jerakine.data.I18nFileAccessor import I18nFileAccessor
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.resources.events.ResourceLoadedEvent import ResourceLoadedEvent
from pyd2bot.events.BotEventsManager import BotEventsManager
logger = Logger(__name__)


PORT = 5555
AUTH_SERVER = "54.76.16.121"
SERVER_ID = 210
CHARACTER_ID = 290210840786
CREDS = json.load(Path("tests/creds.json").open("r"))
CONN = {
    "host": AUTH_SERVER,
    "port": PORT,
}


class TestBot:

    def __init__(self):
        # Load language file to be able to translate ids to actual text
        I18nFileAccessor().init(Constants.LANG_FILE_PATH)
        WorldPathFinder().init()

    def main(self):
        krnl.Kernel().init()
        auth.AuthentificationManager().setCredentials(**CREDS)
        connh.ConnectionsHandler.connectToLoginServer(**CONN)
        BotEventsManager().add_listener(BotEventsManager.SERVER_SELECTION, self.onServerSelection)
        BotEventsManager().add_listener(BotEventsManager.CHARACTER_SELECTION, self.onCharacterSelection)
        BotEventsManager().add_listener(BotEventsManager.SERVER_SELECTED, self.onServerSelectionSuccess)
        BotEventsManager().add_listener(BotEventsManager.CHARACTER_SELECTED, self.onCharacterSelectionSuccess)
        BotEventsManager().add_listener(BotEventsManager.SWITCH_TO_ROLEPLAY, self.onRolePlayContextEntred)
        BotEventsManager().add_listener(BotEventsManager.SWITCH_TO_FIGHT, self.onRolePlayContextEntred)
        BotEventsManager().add_listener(BotEventsManager.MAP_DATA_LOADED, self.onMapDataLoaded)

    def onServerSelection(self, event):
        krnl.Kernel().getWorker().process(ServerSelectionAction.create(serverId=SERVER_ID))

    def onCharacterSelection(self, event):
        krnl.Kernel().getWorker().process(CharacterSelectionAction.create(characterId=CHARACTER_ID, btutoriel=False))

    def onServerSelectionSuccess(self, event):
        logger.info("Server selected")

    def onCharacterSelectionSuccess(self, event):
        logger.info("Character selected")

    def onRolePlayContextEntred(self, event):
        logger.info("RolePlay context entered")
        pass

    def onGameFightContextEntered(self, event):
        logger.info("Fight context entered")
        pass

    def onMapDataLoaded(self, e:ResourceLoadedEvent):
        logger.info(f"Bot is currently in the map {PlayedCharacterManager().currentMap}")
    
    def onPathFound(self, result):
        logger.info("sheesh")


if __name__ == "__main__":
    bot = TestBot()
    bot.main()
