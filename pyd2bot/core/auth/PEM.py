
from Cryptodome.PublicKey import RSA
import base64

class PEM:
    RSA_PRIVATE_KEY_HEADER:str = "-----BEGIN RSA PRIVATE KEY-----"
    RSA_PRIVATE_KEY_FOOTER:str = "-----END RSA PRIVATE KEY-----"
    RSA_PUBLIC_KEY_HEADER:str = "-----BEGIN PUBLIC KEY-----"
    RSA_PUBLIC_KEY_FOOTER:str = "-----END PUBLIC KEY-----"
    CERTIFICATE_HEADER:str = "-----BEGIN CERTIFICATE-----"
    CERTIFICATE_FOOTER:str = "-----END CERTIFICATE-----"

    @staticmethod
    def extractBinary(header:str, footer:str, somestr:str) -> bytearray:
        i = somestr.find(header)
        if i == -1:
            return None
        i += len(header)
        j = somestr.find(footer)
        if j == -1:
            return None
        b64 = somestr[i:j]
        b64 = b64.replace(" ", "")
        return base64.b64decode(b64)
    
    @staticmethod
    def readRSAPrivateKey(s:str) -> RSA:
        der = PEM.extractBinary(PEM.RSA_PRIVATE_KEY_HEADER, PEM.RSA_PRIVATE_KEY_FOOTER, s)
        private_key = RSA.importKey(der)
        return private_key
    
    def readRSAPublicKey(pk_str:str) -> RSA:
        der:bytearray = PEM.extractBinary(PEM.RSA_PUBLIC_KEY_HEADER, PEM.RSA_PUBLIC_KEY_FOOTER, pk_str)
        public_key = RSA.importKey(der)
        return public_key
    
    @staticmethod
    def readCertIntoArray(s:str) -> bytearray:
        return PEM.extractBinary(PEM.CERTIFICATE_HEADER, PEM.CERTIFICATE_FOOTER, s)

