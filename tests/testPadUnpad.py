from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.hurlan.crypto.symmetric.PKCS5 import PKCS5


padding = PKCS5(16)
s = ByteArray(b"a" * 16)
padding.pad(s)
padding.unpad(s)
print(len(s))
print(s.decode("utf-8"))
