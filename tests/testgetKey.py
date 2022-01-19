
import hashlib
from pyd2bot.utils.signature import SignatureKey, Signature
from pyd2bot.network.customDataWrapper import Data
from Cryptodome.PublicKey import RSA

k1_path = r"C:\Users\majdoub\OneDrive\Documents\pyd2bot\pyd2bot\gameData\binaryData\ServerControlFrame_PUBLIC_KEY_V1.bin"
k2_path = r"C:\Users\majdoub\OneDrive\Documents\pyd2bot\pyd2bot\gameData\binaryData\ServerControlFrame_PUBLIC_KEY_V2.bin"
rdmsg_path = r"C:\Users\majdoub\OneDrive\Documents\pyd2bot\tests\rawd.bin"

with open(k1_path, 'rb') as fp:
    data = Data(fp.read())
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
    print(content)
    # l = Loader()
    # l.uncaughtErrorEvents.addEventListener(UncaughtErrorEvent.UNCAUGHT_ERROR, this.onUncaughtError, false, 0, true)
    # lc = LoaderContext(false, ApplicationDomain(ApplicationDomain.currentDomain))
    # AirScanner.allowByteCodeExecution(lc, true)
    # l.loadBytes(content, lc)
                        