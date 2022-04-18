import base64
from com.ankamagames.dofus.logic.shield.ShieldCertifcate import ShieldCertifcate
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.hurlan.crypto.symmetric.AESKey import AESKey
from com.hurlan.crypto.symmetric.ECBMode import ECBMode

logger = Logger(__name__)

mycert = ShieldCertifcate()
mycert.content = "testtesttesttesttesttesttessdfsdfsdfsdfsdfttesttesttest"
logger.debug("content : " + mycert.content)
logger.debug(f"bytes len of content : {len(mycert.content.encode('utf-8'))}")
mycert.useBasicInfo = True
mycert.useBasicNetworkInfo = False
mycert.useAdvancedNetworkInfo = False
mycert.useUserInfo = True
hex_hash = mycert.getHash(True)
key = ByteArray(bytes.fromhex(hex_hash))
logger.debug(f"length of the Key : {key.length}")
aesKey: AESKey = AESKey(key)
ecb: ECBMode = ECBMode(aesKey)


cryptedData: ByteArray = ByteArray(bytes(mycert.content, "utf-8"))

ecb.encrypt(cryptedData)
logger.debug("message encrypted : " + str(cryptedData))
crypted_base64 = ByteArray(base64.b64encode(cryptedData))

logger.debug("crypted_base64 : " + str(crypted_base64))
decrypted = mycert.decrypt(crypted_base64)
logger.debug("message decrypted : " + decrypted)
assert mycert.content == decrypted
