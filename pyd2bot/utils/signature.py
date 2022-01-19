
import hashlib
from pyd2bot.network.customDataWrapper import Data
from Cryptodome.PublicKey import RSA
import pyd2bot.utils.crypto as crypto_utils

class SignatureError(Exception):
    pass

class SignatureKey:
    PUBLIC_KEY_HEADER:str = "DofusPublicKey"
    PRIVATE_KEY_HEADER:str = "DofusPrivateKey"
    
    @staticmethod
    def import_key(input:Data): 
        header:str = input.readUTF()
        if header != SignatureKey.PUBLIC_KEY_HEADER and header != SignatureKey.PRIVATE_KEY_HEADER:
            raise Exception("Invalid public or private header")
        if header == SignatureKey.PUBLIC_KEY_HEADER:
            N = input.readUTF()
            N = int.from_bytes(bytes(N, 'utf'), "big")
            E = input.readUTF()
            E = int.from_bytes(bytes(E, 'utf'), "big")
            return RSA.RsaKey(n=N, e=E)
        
class Signature:
    ANKAMA_SIGNED_FILE_HEADER:str = "AKSF"
    SIGNATURE_HEADER:str = "AKSD"
    
    def __init__(self, key1:SignatureKey, key2:RSA.RsaKey):
        self.key1 = key1
        self.key2= key2

    def verify(self, input:bytearray) -> bytearray: 
        input:Data = Data(input)
        headerSize:int = 0
        header:str = None
        headerPosition = 0
        headerSize = input.readUnsignedShort()
        if headerSize != len(self.ANKAMA_SIGNED_FILE_HEADER):
            input.position = 0
            headerPosition = input.remaining() - len(self.ANKAMA_SIGNED_FILE_HEADER)
            input.position = headerPosition
            header = input.readUTFBytes(len(self.ANKAMA_SIGNED_FILE_HEADER))
            if header == self.ANKAMA_SIGNED_FILE_HEADER:
                return self.verifyV2Signature(input, headerPosition)
        else:
            header = input.readUTFBytes(len(self.ANKAMA_SIGNED_FILE_HEADER))
            if header == self.ANKAMA_SIGNED_FILE_HEADER:
                return self.verifyV1Signature(input)
        raise SignatureError("Invalid header")

    def verifyV2Signature(self, input:Data, headerPosition:int) -> bool:
        if not self.key2:
            raise SignatureError("No key for self signature version")
        try:
            input.position = headerPosition - 4
            signedDataLenght = input.readShort()
            input.position = headerPosition - 4 - signedDataLenght
            cryptedData = input.readBytes(0, signedDataLenght)
            sigData = Data(crypto_utils.verifyRSASign(self.key2, cryptedData))
            sigData.position = 0
            sigHeader = sigData.readUTF()
            if sigHeader != self.SIGNATURE_HEADER:
                return None
            sigVersion = sigData.readByte()
            sigData.readInt()
            sigData.readInt()
            sigFileLenght = sigData.readInt()
            if sigFileLenght != headerPosition - 4 - signedDataLenght:
                return None
            hashType = sigData.readByte()
            sigHash = sigData.readUTF()
            input.position = 0
            output = input.readBytes(0, headerPosition - 4 - signedDataLenght)
            if hashType == 0:
                contentHash = hashlib.md5(output).hexdigest()
            elif hashType == 1:
                contentHash = hashlib.sha256(output).hexdigest()
            else:
                return None
            if sigHash != contentHash:
                return None
        except Exception as e:
            return None
        return output

    def verifyV1Signature(self, input:Data) -> bytearray:
        len:int = 0
        try:
            len = input.readInt()
            sigData = input.readBytes(0, len)
        except Exception as e:
            raise SignatureError("Invalid signature format, not enough data.")
        
        try:   
            decryptedHash = Data(crypto_utils.verifyRSASign(self.key1, sigData))
        except Exception as e:
            return None
        
        decryptedHash.position = 0
        ramdomPart:int = decryptedHash.readByte()
        for i in range(len(decryptedHash)):
            decryptedHash[i] ^= ramdomPart
        
        contentLen:int = decryptedHash.readUnsignedInt()
        testedContentLen:int = input.remaining()
        signHash:str = decryptedHash.readUTFBytes(decryptedHash.remaining())[1:]
        output = Data(input.readBytes())
        contentHash:str = hashlib.md5(output.readUTFBytes(output.remaining())).hexdigest()[1:]
        if signHash and signHash == contentHash and contentLen == testedContentLen:
            return output
        else:
            return None
      