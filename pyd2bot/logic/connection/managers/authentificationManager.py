from argparse import ArgumentError
import math
import os
import logging
import random
from pyd2bot.utils.crypto import RSACipher, RSA, PKCS1
from pyd2bot.network.message import Msg
from pyd2bot.utils.binaryIO import ByteArray
from pyd2bot.utils.crypto import CBCMode, NullPad, AESKey, SimpleIVMode

logger = logging.getLogger("bot")
ROOTDIR = os.path.dirname(__file__)

class ClientPubKeyNotFoundError(Exception):
    pass


CLIENT_PUBLIC_KEY_P = os.path.join(ROOTDIR, "public_key.pk")
if not os.path.exists(CLIENT_PUBLIC_KEY_P):
    raise ClientPubKeyNotFoundError(f"{CLIENT_PUBLIC_KEY_P} file not found")

    
class AuthentificationManager:
    with open(CLIENT_PUBLIC_KEY_P, 'r') as fp:
        CLIENT_PUB_KEY = RSA.import_key(fp.read())
    AES_KEY_LENGTH = 32
    
    def __init__(self):
        self._publicKey:str = None
        self._salt:str = None
        self.gameServerTicket:str = None
        self._AESKey:str = self.generateRandomAESKey(self.AES_KEY_LENGTH)
        self.nextToken:str = None
        self.tokenMode:bool = None
    
    def setSalt(self, salt:str) -> None:
        self._salt = salt
        if len(self._salt) < 32:
            logger.warn("Authentification salt size is lower than 32 ")
        while len(self._salt) < 32:
            self._salt += " "
            
    def setPublicKey(self, enc_publicKey:list[int]):
        baSignedKey = ByteArray.from_int8Arr(enc_publicKey)
        rsacipher = RSACipher(self.CLIENT_PUB_KEY, PKCS1())
        ba_pubKey = ByteArray()
        if not rsacipher.verify(baSignedKey, ba_pubKey):
            raise Exception("Pubkey Sign validation failed!")
        self._publicKey = "-----BEGIN PUBLIC KEY-----\n" + ba_pubKey.to_string() + "\n-----END PUBLIC KEY-----"
    
    def getCanAutoConnectWithToken(self) -> bool:
        return self.nextToken != None

    def getIdentificationMessage(self, login, pwd):
        imsg = {
            '__type__': 'IdentificationMessage',
            'autoconnect': False,
            'credentials': self.getAuthCredentials(login, pwd),
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
        return imsg
    
    def getAuthCredentials(self, login:str, pwd:str) -> list[int]:
        baIn = bytearray()
        baIn += bytes(self._salt, 'utf')
        baIn += self._AESKey
        baIn += len(login).to_bytes(1, "big")
        baIn += bytes(login, 'utf')
        baIn += bytes(pwd, 'utf')
        rsa_key = RSA.importKey(bytes(self._publicKey, 'utf'))
        rsacipher = RSACipher(rsa_key, PKCS1())
        baOut = rsacipher.encrypt(baIn)
        return baOut.to_int8Arr()
    
    @staticmethod
    def generateRandomAESKey(key_length) -> ByteArray:
        ba = ByteArray()
        for _ in range(key_length):
            rb = math.floor(random.random() * 256)
            ba.writeByte(rb, signed=False)
        ba.position = 0
        return ba

    def decodeWithAES(self, byteArrayOrVector) -> ByteArray:
        aescipher = SimpleIVMode(CBCMode(AESKey(self._AESKey), NullPad()))
        result = ByteArray()
        result.writeBytes(self._AESKey, 0, 16)
        
        if type(byteArrayOrVector) == list:
            for i in byteArrayOrVector:
                result.writeByte(i, signed=True)
                
        else:     
            if not isinstance(byteArrayOrVector, ByteArray):
                raise ArgumentError("Argument must be a bytearray or a vector of int/uint")
            result.writeBytes(byteArrayOrVector)
            
        aescipher.decrypt(result)
        return result