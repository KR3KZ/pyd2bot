
import hashlib
from com.hurlan.crypto.signature import SignatureKey, Signature
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from Cryptodome.PublicKey import RSA

k1_path = r"C:\Users\majdoub\OneDrive\Documents\pyd2bot\pyd2bot\gameData\binaryData\ServerControlFrame_PUBLIC_KEY_V1.bin"
k2_path = r"C:\Users\majdoub\OneDrive\Documents\pyd2bot\pyd2bot\gameData\binaryData\ServerControlFrame_PUBLIC_KEY_V2.bin"
rdmsg_path = r"C:\Users\majdoub\OneDrive\Documents\pyd2bot\tests\rawd.bin"

with open(k1_path, 'rb') as fp:
    data = ByteArray(fp.read())
    SIGNATURE_KEY_V1 = SignatureKey.import_key(data)

with open(k2_path, 'rb') as fp:
    ba = fp.read()
    SIGNATURE_KEY_V2 = RSA.import_key(ba)

with open(rdmsg_path, 'rb') as fp:
    rdMsg = fp.read()
    
signature = Signature(SIGNATURE_KEY_V1, SIGNATURE_KEY_V2)
print(f"Bytecode len: {len(rdMsg)}, hash: " + hashlib.md5(rdMsg).hexdigest())
content = signature.verify(rdMsg)

if content:
    with open("rmsg_bytecode.swf", 'wb') as fp:
        fp.write(content)
                        