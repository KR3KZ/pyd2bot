from pyd2bot.utils.crypto import AESKey, CBCMode, SimpleIVMode, NullPad, signature
from pyd2bot.logic.managers import AuthentificationManager
from pyd2bot.utils.binaryIO import ByteArray


am = AuthentificationManager()

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def testSignedIntToArr():
    z = [10, -13, 24, -55, -66]
    x = ByteArray()
    for i in z:
        x.writeByte(i, signed=True)
    y = x.to_int8Arr()
    assert y == z
    
def testCryptDecrypt(msg):
    original_msg = msg
    padded_msg = pad(original_msg)
    msgBytes = ByteArray(bytes(padded_msg, 'utf-8'))
    aescipher = SimpleIVMode(CBCMode(AESKey(am._AESKey), NullPad()))
    aescipher.encrypt(msgBytes)
    aescipher = SimpleIVMode(CBCMode(AESKey(am._AESKey), NullPad()))
    aescipher.decrypt(msgBytes)
    decryped_msg = unpad(msgBytes.decode('utf-8'))
    assert decryped_msg == original_msg

def encryptDecryptTicket(ticket):
    ticket_str = ticket
    # server side 
    msgBytes = ByteArray(bytes(ticket_str, 'utf-8'))
    aescipher = SimpleIVMode(CBCMode(AESKey(am._AESKey), NullPad()))
    aescipher.encrypt(msgBytes)
    encticket_integers = msgBytes.to_int8Arr()
    # client side
    aescipher = SimpleIVMode(CBCMode(AESKey(am._AESKey), NullPad()))
    result = am.decodeWithAES(encticket_integers)
    assert result.decode() == ticket_str

testSignedIntToArr()
testCryptDecrypt("Hello World!")
encryptDecryptTicket('1d3ab614975022927febb53c66273374')
