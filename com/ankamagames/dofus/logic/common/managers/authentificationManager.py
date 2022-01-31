from argparse import ArgumentError
import os
import logging
from com.ankamagames.jerakine.metaclasses.singleton import Singleton
from com.ankamagames.jerakine.network.customDataWrapper import ByteArray
from com.hurlan.crypto.symmetric.aESKey import AESKey
from com.hurlan.crypto.symmetric.cBCMode import CBCMode
from com.hurlan.crypto.symmetric.nullPAd import NullPad
from com.hurlan.crypto.symmetric.pKCS1 import PKCS1
from com.hurlan.crypto.symmetric.rSAKey import RSACipher
from com.hurlan.crypto.symmetric.simpleIVMode import SimpleIVMode
from Cryptodome.PublicKey import RSA
logger = Logger(__name__)
ROOTDIR = os.path.dirname(__file__)


class ClientPubKeyNotFoundError(Exception):
    pass


CLIENT_PUBLIC_KEY_P = os.path.join(ROOTDIR, "public_key.pk")
if not os.path.exists(CLIENT_PUBLIC_KEY_P):
    raise ClientPubKeyNotFoundError(f"{CLIENT_PUBLIC_KEY_P} file not found")

    
class AuthentificationManager(metaclass=Singleton):
    with open(CLIENT_PUBLIC_KEY_P, 'r') as fp:
        CLIENT_PUB_KEY = RSA.import_key(fp.read())
    AES_KEY_LENGTH = 32
    _publicKey:str = None
    _salt:str = None
    gameServerTicket:str = None
    _AESKey:str = None
    nextToken:str = None
    tokenMode:bool = None
    username = None
    
    def initAESKey(self):
        self._AESKey = AESKey.generateRandomAESKey(self.AES_KEY_LENGTH)
    
    def setSalt(self, salt:str) -> None:
        if len(salt) < 32:
            logger.warn("Authentification salt size is lower than 32 ")
        while len(salt) < 32:
            salt += " "
        self._salt = salt

    def setPublicKey(self, enc_publicKey:list[int]):
        baSignedKey = ByteArray.from_int8Arr(enc_publicKey)
        rsacipher = RSACipher(self.CLIENT_PUB_KEY, PKCS1())
        ba_pubKey = ByteArray()
        if not rsacipher.verify(baSignedKey, ba_pubKey):
            raise Exception("Pubkey Sign validation failed!")
        self._publicKey = "-----BEGIN PUBLIC KEY-----\n" + str(ba_pubKey) + "\n-----END PUBLIC KEY-----"

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