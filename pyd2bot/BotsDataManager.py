import json
import os
from pathlib import Path
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray

CURRDIR = Path(__file__).parent
BOTSDB = CURRDIR / "botCharachtersDB.json"


class BotsDataManager:
    if not os.path.exists(BOTSDB):
        with open(BOTSDB, "w") as fp:
            json.dump({}, fp)
    with open(BOTSDB, "r") as fp:
        _db = json.load(fp)

    @classmethod
    def addEntry(cls, name, account, charId, serverId):
        cls._db.update(
            {
                name: {
                    "account": account,
                    "charachterId": int(charId),
                    "serverId": int(serverId),
                }
            }
        )
        with open(BOTSDB, "w") as fp:
            json.dump(cls._db, fp, indent=4)

    @classmethod
    def getEntry(cls, name):
        result = cls._db.get(name)
        return result


if __name__ == "__main__":
    import sys

    botName = sys.argv[1]
    account = sys.argv[2]
    serverId = int(sys.argv[3])
    charachterId = int(sys.argv[4])
    BotsDataManager.addEntry(botName, account, charachterId, serverId)
