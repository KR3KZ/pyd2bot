from pathlib import Path
from time import sleep
import json
import com.ankamagames.dofus.kernel.Kernel as krnl
from com.ankamagames.dofus.kernel.net.ConnectionType import ConnectionType
from com.ankamagames.dofus.logic.connection.actions.ServerSelectionAction import ServerSelectionAction
import com.ankamagames.dofus.logic.connection.managers.AuthentificationManager as auth
import com.ankamagames.dofus.kernel.net.ConnectionsHandler as connh
from com.ankamagames.dofus.logic.game.approach.actions.CharacterSelectionAction import CharacterSelectionAction
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

    @classmethod
    def main(cls):
        krnl.Kernel().init()
        auth.AuthentificationManager().setCredentials(**CREDS)
        connh.ConnectionsHandler.connectToLoginServer(**CONN)
        BotEventsManager().add_listener(PlayerEvents.SERVER_SELECTION, cls.onServerSelection)
        BotEventsManager().add_listener(PlayerEvents.CHARACTER_SELECTION, cls.onCharacterSelection)
        BotEventsManager().add_listener(PlayerEvents.SERVER_SELECTED, cls.onServerSelectionSuccess)
        BotEventsManager().add_listener(PlayerEvents.CHARACTER_SELECTED, cls.onCharacterSelectionSuccess)

    @classmethod
    def onServerSelection(cls, event):
        BotEventsManager().remove_listener(PlayerEvents.SERVER_SELECTION, cls.onServerSelection)
        krnl.Kernel().getWorker().process(ServerSelectionAction.create(serverId=SERVER_ID))

    @classmethod
    def onCharacterSelection(cls, event):
        BotEventsManager().remove_listener(PlayerEvents.CHARACTER_SELECTION, cls.onCharacterSelection)
        krnl.Kernel().getWorker().process(CharacterSelectionAction.create(characterId=CHARACTER_ID, btutoriel=False))

    @classmethod
    def onServerSelectionSuccess(cls, event):
        BotEventsManager().remove_listener(PlayerEvents.SERVER_SELECTED, cls.onServerSelectionSuccess)
    
    @classmethod
    def onCharacterSelectionSuccess(cls, event):
        print("youpi")
        BotEventsManager().remove_listener(PlayerEvents.CHARACTER_SELECTED, cls.onCharacterSelectionSuccess)
        
if __name__ == "__main__":
    TestBot.main()
