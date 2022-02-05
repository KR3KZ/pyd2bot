from pathlib import Path
from time import sleep
import json
import com.ankamagames.dofus.kernel.Kernel as krnl
from com.ankamagames.dofus.kernel.net.ConnectionType import ConnectionType
from com.ankamagames.dofus.logic.connection.actions.ServerSelectionAction import ServerSelectionAction
import com.ankamagames.dofus.logic.connection.managers.AuthentificationManager as auth
import com.ankamagames.dofus.kernel.net.ConnectionsHandler as connh
from com.ankamagames.dofus.logic.game.approach.actions.CharacterSelectionAction import CharacterSelectionAction
from com.ankamagames.jerakine.data.I18nFileAccessor import I18nFileAccessor
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.network.ServerConnectionClosedMessage import ServerConnectionClosedMessage
from pyd2bot.events.BotEventsManager import BotEventsManager
from pyd2bot.events.PlayerEvents import PlayerEvents

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
        I18nFileAccessor().init(r"C:\Users\majdoub\AppData\Local\Ankama\Dofus\data\i18n\i18n_fr.d2i")

    def main(self):
        krnl.Kernel().init()
        auth.AuthentificationManager().setCredentials(**CREDS)
        connh.ConnectionsHandler.connectToLoginServer(**CONN)
        BotEventsManager().add_listener(PlayerEvents.SERVER_SELECTION, self.onServerSelection)
        BotEventsManager().add_listener(PlayerEvents.CHARACTER_SELECTION, self.onCharacterSelection)
        BotEventsManager().add_listener(PlayerEvents.SERVER_SELECTED, self.onServerSelectionSuccess)
        BotEventsManager().add_listener(PlayerEvents.CHARACTER_SELECTED, self.onCharacterSelectionSuccess)

        BotEventsManager().add_listener(PlayerEvents.SWITCH_TO_ROLEPLAY, self.onRolePlayContextEntred)
        BotEventsManager().add_listener(PlayerEvents.SWITCH_TO_FIGHT, self.onRolePlayContextEntred)

    def onServerSelection(self, event):
        krnl.Kernel().getWorker().process(ServerSelectionAction.create(serverId=SERVER_ID))

    def onCharacterSelection(self, event):
        krnl.Kernel().getWorker().process(CharacterSelectionAction.create(characterId=CHARACTER_ID, btutoriel=False))

    def onServerSelectionSuccess(self, event):
        pass

    def onCharacterSelectionSuccess(self, event):
        pass

    def onRolePlayContextEntred(self, event):
        # TODO: Treatement at the enter of tghe roleplay context
        pass

    def onGameFightContextEntered(self, event):
        # TODO: Treatement at the enter of tghe game
        pass

if __name__ == "__main__":
    bot = TestBot()
    bot.main()
