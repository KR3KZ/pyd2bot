from pathlib import Path
from time import sleep
import json
import com.ankamagames.dofus.kernel.Kernel as krnl
from com.ankamagames.dofus.logic.connection.actions.ServerSelectionAction import ServerSelectionAction
import com.ankamagames.dofus.logic.connection.managers.AuthentificationManager as auth
import com.ankamagames.dofus.kernel.net.ConnectionsHandler as connh


PORT = 5555
AUTH_SERVER = "54.76.16.121"
SERVER_ID = 210
CREDS = json.load(Path("tests/creds.json").open("r"))
CONN = {
    "host": AUTH_SERVER,
    "port": PORT,
}
class PlayerEvents:
    SERVER_SELECTION = "server_selection"

class TestBot:

    @classmethod
    def main(cls):
        krnl.Kernel().init()
        auth.AuthentificationManager().setCredentials(**CREDS)
        connh.ConnectionsHandler.connectToLoginServer(**CONN)
        conn = connh.ConnectionsHandler.getConnection()
        conn.add_listener(PlayerEvents.SERVER_SELECTION, cls.onServerSelection)

    @classmethod
    def onServerSelection(cls, event):
        krnl.Kernel().getWorker().process(ServerSelectionAction.create(serverId=SERVER_ID))
        krnl.Kernel().getWorker().processQueues()

if __name__ == "__main__":
    TestBot.main()
