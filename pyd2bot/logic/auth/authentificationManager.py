import os
import logging
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import pyd2bot.utils.crypto as crypto_utils
from pyd2bot.network.message import Msg

logger = logging.getLogger("bot")
ROOTDIR = os.path.dirname(__file__)

class ClientPubKeyNotFoundError(Exception):
    pass

class AuthentificationManager:
    AES_KEY_LENGTH = 32
    CLIENT_PUBLIC_KEY_P = os.path.join(ROOTDIR, "public_key.pk")
    if not os.path.exists(CLIENT_PUBLIC_KEY_P):
        raise ClientPubKeyNotFoundError(f"{CLIENT_PUBLIC_KEY_P} file not found")
    with open(CLIENT_PUBLIC_KEY_P, 'r') as fp:
        CLIENT_PUB_KEY = RSA.importKey(fp.read())
    _publicKey:str
    _salt:str
    _gameServerTicket:str
    _AESKey:bytearray
    nextToken:str
    tokenMode:bool
    
    def __init__(self):
        self._AESKey = crypto_utils.generateRandomAESKey(self.AES_KEY_LENGTH)
    
    def setSalt(self, salt:str) -> None:
        self._salt = salt
        if len(self._salt) < 32:
            logger.warn("Authentification salt size is lower than 32 ")
        while len(self._salt) < 32:
            self._salt += " "
            
    def setPublicKey(self, enc_publicKey:list[int]):
        baSignedKey = crypto_utils.intArrToBytesArr(enc_publicKey)
        ba_pubKey = crypto_utils.verifyRSASign(self.CLIENT_PUB_KEY, baSignedKey)
        b64_pubkey = base64.b64encode(ba_pubKey)
        self._publicKey = "-----BEGIN PUBLIC KEY-----\n" + b64_pubkey.decode('utf') + "\n-----END PUBLIC KEY-----"
    
    def getCanAutoConnectWithToken(self) -> bool:
        return self.nextToken != None

    def getIdentificationMessage(self, login, pwd):
        imsg = {
            '__type__': 'IdentificationMessage',
            'autoconnect': False,
            'credentials': [],
            'failedAttempts': [],
            'lang': 'fr',
            'serverId': 0,
            'sessionOptionalSalt': 0,
            'useCertificate': False,
            'useLoginToken': False,
            'version': {
                '__type__': 'Version',
                'build': 11,
                'buildType': 0,
                'code': 5,
                'major': 2,
                'minor': 62
            }
        }
        imsg["credentials"] = self.getAuthCredentials(login, pwd)
        return Msg.from_json(imsg)
    
    def getAuthCredentials(self, login:str, pwd:str) -> list[int]:
        baIn = bytearray()
        baIn += bytes(self._salt, 'utf')
        baIn += self._AESKey
        baIn += len(login).to_bytes(1, "big")
        baIn += bytes(login, 'utf')
        baIn += bytes(pwd, 'utf')
        rsa_key = RSA.importKey(bytes(self._publicKey, 'utf'))
        baOut = crypto_utils.encryptWithRSA(rsa_key, baIn)
        return crypto_utils.byteArrtoIntArr(baOut)
