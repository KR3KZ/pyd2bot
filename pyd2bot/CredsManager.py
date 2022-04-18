import json
from pathlib import Path
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import base64

from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray

KEYS_DIR = Path("D:\RSA-KEYS\password-crypting")
CREDS_DB = Path("pyd2bot\creds.json")
pubkey_p = KEYS_DIR / "id_rsa.pub"
privatekey_p = KEYS_DIR / "id_rsa"


class CredsManager:
    with open(pubkey_p, "rb") as fp:
        _pubkey = RSA.import_key(fp.read())
    with open(privatekey_p, "rb") as fp:
        _privatekey = RSA.import_key(fp.read())
    with open(CREDS_DB, "r") as fp:
        _creds = json.load(fp)

    @staticmethod
    def addEntry(name, username, password):
        password = CredsManager.encryptPasssword(password)
        CredsManager._creds.update({name: {"username": username, "password": password}})
        with open(CREDS_DB, "w") as fp:
            json.dump(CredsManager._creds, fp, indent=4)

    @staticmethod
    def getEntry(name):
        result = CredsManager._creds.get(name)
        result["password"] = CredsManager.decryptPasssword(result["password"])
        return result

    @staticmethod
    def encryptPasssword(password: str) -> list[int]:
        rsacipher = PKCS1_OAEP.new(CredsManager._pubkey)
        baIn = bytes(password, "utf-8")
        encryptedPass = ByteArray(rsacipher.encrypt(baIn))
        return encryptedPass.to_int8Arr()

    @staticmethod
    def decryptPasssword(encryptedPass: list[int]) -> str:
        cipher = PKCS1_OAEP.new(CredsManager._privatekey)
        encryptedPass = ByteArray.from_int8Arr(encryptedPass)
        password_ba = cipher.decrypt(encryptedPass)
        password = password_ba.decode("utf-8")
        return password


if __name__ == "__main__":
    with open("pyd2bot/creds.json", "r") as fp:
        creds = json.load(fp)
    print(CredsManager.decryptPasssword(creds["password"]))
