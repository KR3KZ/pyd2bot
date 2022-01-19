import random
import logging
import math
from typing import Any
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Util import number
from Cryptodome.Cipher import AES, PKCS1_OAEP, PKCS1_v1_5
from typing import Any
import hashlib
from . import crypto_utils 
from network.message.msg import Msg

logger = logging.getLogger("bot")

class TrustCertificate:
    pass

class AuthentificationManager:
    AES_KEY_LENGTH = 32
    PUB_KEY = "-----BEGIN PUBLIC KEY-----\n" + "MIIBUzANBgkqhkiG9w0BAQEFAAOCAUAAMIIBOwKCATIAgucoka9J2PXcNdjcu6CuDmgteIMB+rih" \
		"2UZJIuSoNT/0J/lEKL/W4UYbDA4U/6TDS0dkMhOpDsSCIDpO1gPG6+6JfhADRfIJItyHZflyXNUj" \
		"WOBG4zuxc/L6wldgX24jKo+iCvlDTNUedE553lrfSU23Hwwzt3+doEfgkgAf0l4ZBez5Z/ldp9it" \
		"2NH6/2/7spHm0Hsvt/YPrJ+EK8ly5fdLk9cvB4QIQel9SQ3JE8UQrxOAx2wrivc6P0gXp5Q6bHQo" \
		"ad1aUp81Ox77l5e8KBJXHzYhdeXaM91wnHTZNhuWmFS3snUHRCBpjDBCkZZ+CxPnKMtm2qJIi57R" \
		"slALQVTykEZoAETKWpLBlSm92X/eXY2DdGf+a7vju9EigYbX0aXxQy2Ln2ZBWmUJyZE8B58CAwEA" \
		"AQ==" + "\n-----END PUBLIC KEY-----"
    _publicKey:str
    _salt:str
    _gameServerTicket:str
    _AESKey:bytearray 
    _certificate:TrustCertificate
    username:str
    nextToken:str
    tokenMode:bool
    
    def __init__(self):
        super()
    
    def getInstance(self):
        if self is None:
            self = AuthentificationManager()
        return self
    
    def getGameServerTicket(self) -> str:
        return self._gameServerTicket
    
    def setGameServerTicket(self, value:str) -> None:
        self._gameServerTicket = value
    
    def getSalt(self) -> str:
        return self._salt
    
    def generateRandomAESKey(self) -> bytearray:
        ba:bytearray = bytearray()
        for _ in range(self.AES_KEY_LENGTH):
            rb = math.floor(random.random() * 256)
            ba += rb.to_bytes(1, "big")
        return ba
    
    def initAESKey(self) -> None:
        self._AESKey = self.generateRandomAESKey()
    
    def decodeWithAES(self, byteArray:Any) -> bytearray:
        aesCipher = AES.new(self._AESKey, AES.MODE_CBC)
        result = bytearray()
        result += self._AESKey
        result += byteArray
        aesCipher.decrypt(result)
        return result
    
    def setSalt(self, salt:str) -> None:
        self._salt = salt
        if len(self._salt) < 32:
            logger.warn("Authentification salt size is lower than 32 ")
        while len(self._salt) < 32:
            self._salt += " "
    
    def setPublicKey(self, enc_publicKey:list[int]):
        baSignedKey = bytearray()
        for sb in enc_publicKey:
            baSignedKey += sb.to_bytes(1, "big", signed=True)
        myPkey = RSA.importKey(bytes(self.PUB_KEY, 'utf'))
        ba_pubKey = crypto_utils.verify(myPkey, baSignedKey)
        self._publicKey = "-----BEGIN PUBLIC KEY-----\n" + base64.b64encode(ba_pubKey).decode('utf') + "\n-----END PUBLIC KEY-----"
        print(len(self._publicKey))
        print(len(self.PUB_KEY))
    
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
        imsg["credentials"] = self.cipherRsa(login, pwd)
        return Msg.from_json(imsg)
    
    def cipherMd5str(self, pwd:str) -> str:
        return  hashlib.md5(pwd + self._salt)
    
    def cipherRsa(self, login:str, pwd:str) -> list:
        baIn = bytearray()
        baIn += bytes(self._salt, 'utf')
        baIn += self._AESKey
        baIn += len(login).to_bytes(1, "big")
        baIn += bytes(login, 'utf')
        baIn += bytes(pwd, 'utf')
        myPkey = RSA.importKey(bytes(self._publicKey, 'utf'))
        baOut = PKCS1_OAEP.new(myPkey).encrypt(baIn)
        ret:list[int] = []
        for i in range(len(baOut)):
            ret.append(int.from_bytes(baOut[i:i+1], "big", signed=True))
        return ret




