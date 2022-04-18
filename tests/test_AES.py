from com.ankamagames.dofus.logic.connection.managers.AuthentificationManager import (
    AuthentificationManager,
)
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.hurlan.crypto.symmetric.AESKey import AESKey
from com.hurlan.crypto.symmetric.CBCMode import CBCMode
from com.hurlan.crypto.symmetric.NullPAd import NullPad
from com.hurlan.crypto.symmetric.SimpleIVMode import SimpleIVMode


am = AuthentificationManager()
am.initAESKey()
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(
    BLOCK_SIZE - len(s) % BLOCK_SIZE
)
unpad = lambda s: s[: -ord(s[len(s) - 1 :])]


def testSignedIntToArr():
    z = [10, -13, 24, -55, -66]
    x = ByteArray()
    for i in z:
        x.writeByte(i, signed=True)
    y = x.to_int8Arr()
    assert y == z


def testCryptDecrypt(msg):
    original_msg = msg
    padded_msg = pad(original_msg)
    msgBytes = ByteArray(bytes(padded_msg, "utf-8"))
    aescipher = SimpleIVMode(CBCMode(AESKey(am._AESKey), NullPad()))
    aescipher.encrypt(msgBytes)
    aescipher = SimpleIVMode(CBCMode(AESKey(am._AESKey), NullPad()))
    aescipher.decrypt(msgBytes)
    decryped_msg = unpad(msgBytes.decode("utf-8"))
    assert decryped_msg == original_msg


testSignedIntToArr()
testCryptDecrypt("Hello World!")
