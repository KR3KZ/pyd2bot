from argparse import ArgumentError
import os
import logging
from pyd2bot.utils.crypto import RSACipher, RSA, PKCS1
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
    _publicKey:str = None
    _salt:str = None
    gameServerTicket:str = None
    _AESKey:str = None
    nextToken:str = None
    tokenMode:bool = None
    username = None
    
    @staticmethod
    def initAESKey():
        AuthentificationManager._AESKey = AESKey.generateRandomAESKey(AuthentificationManager.AES_KEY_LENGTH)
    
    
    @staticmethod
    def setSalt(salt:str) -> None:
        if len(salt) < 32:
            logger.warn("Authentification salt size is lower than 32 ")
        while len(salt) < 32:
            salt += " "
        AuthentificationManager._salt = salt
    

    @staticmethod    
    def setPublicKey(enc_publicKey:list[int]):
        baSignedKey = ByteArray.from_int8Arr(enc_publicKey)
        rsacipher = RSACipher(AuthentificationManager.CLIENT_PUB_KEY, PKCS1())
        ba_pubKey = ByteArray()
        if not rsacipher.verify(baSignedKey, ba_pubKey):
            raise Exception("Pubkey Sign validation failed!")
        AuthentificationManager._publicKey = "-----BEGIN PUBLIC KEY-----\n" + str(ba_pubKey) + "\n-----END PUBLIC KEY-----"
    

    @staticmethod
    def getCanAutoConnectWithToken() -> bool:
        return AuthentificationManager.nextToken != None


    @staticmethod
    def getIdentificationMessage(login, pwd):
        imsg = {
            '__type__': 'IdentificationMessage',
            'autoconnect': False,
            'credentials': AuthentificationManager.getAuthCredentials(login, pwd),
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
    

    @staticmethod
    def getAuthCredentials(login:str, pwd:str) -> list[int]:
        baIn = bytearray()
        baIn += bytes(AuthentificationManager._salt, 'utf')
        baIn += AuthentificationManager._AESKey
        baIn += len(login).to_bytes(1, "big")
        baIn += bytes(login, 'utf')
        baIn += bytes(pwd, 'utf')
        rsa_key = RSA.importKey(bytes(AuthentificationManager._publicKey, 'utf'))
        rsacipher = RSACipher(rsa_key, PKCS1())
        baOut = rsacipher.encrypt(baIn)
        return baOut.to_int8Arr()


    @staticmethod
    def decodeWithAES(byteArrayOrVector) -> ByteArray:
        aescipher = SimpleIVMode(CBCMode(AESKey(AuthentificationManager._AESKey), NullPad()))
        result = ByteArray()
        result.writeBytes(AuthentificationManager._AESKey, 0, 16)
        
        if type(byteArrayOrVector) == list:
            for i in byteArrayOrVector:
                result.writeByte(i, signed=True)
                
        else:     
            if not isinstance(byteArrayOrVector, ByteArray):
                raise ArgumentError("Argument must be a bytearray or a vector of int/uint")
            result.writeBytes(byteArrayOrVector)
            
        aescipher.decrypt(result)
        return result