import os
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP
import random
import math
import hashlib


def getBlockSize(key:RSA.RsaKey):
   return (key.n.bit_length() + 7) // 8

def cipherMd5str(self, pwd:str) -> str:
   return  hashlib.md5(pwd + self._salt)

def byteArrtoIntArr(ba:bytearray) -> list[int]:
   ret = []
   for i in range(len(ba)):
      ret.append(int.from_bytes(ba[i:i+1], "big", signed=True))
   return ret

def intArrToBytesArr(int_arr:list[int]):
   """Converts an array of signed 8bits integers to an array of bytes
   """
   res = bytearray()
   for nbr in int_arr:
      res += nbr.to_bytes(1, "big", signed=True)
   return res
     
def generateRandomAESKey(key_length) -> bytearray:
   ba:bytearray = bytearray()
   for _ in range(key_length):
      rb = math.floor(random.random() * 256)
      ba += rb.to_bytes(1, "big")
   return ba
   
def decodeWithAES(key:bytearray, ba:bytearray) -> bytearray:
   aesCipher = AES.new(key, AES.MODE_CBC)
   result = key + ba
   aesCipher.decrypt(result)
   return result
   
def pkcs1unpad(m, block_size, type=2):
   '''removes padding returns none if padding is invalid'''
   if len(m) != block_size: return
   if m[0] != 0 or m[1] != type: return
   #first nonzero byte (after 00 02) marks end of padding
   i = 2
   while i < len(m) and m[i] != 0:
      i += 1
   #check that 00 byte was actually found
   if i >= len(m): return
   pad_len = i - 2
   #must have at least 8 bytes of random padding
   if pad_len < 8: return
   return m[3 + pad_len:]

def verifyRSASign(key:RSA.RsaKey, src:bytearray):
   block_size = getBlockSize(key)
   block = int.from_bytes(src, "big", signed=False)
   # de decrypt
   chunk = pow(block, key.e, key.n)
   b:bytearray = chunk.to_bytes(block_size, "big", signed=False)
   dst = pkcs1unpad(b, block_size, 1)
   if dst is None:
      raise Exception("Decrypt error - padding function returned None!")
   return dst

def encryptWithRSA(key:RSA.RsaKey, src:bytearray):
   block_size = getBlockSize(key)
   block = int.from_bytes(pkcs1pad(src, block_size), "big", signed=False)
   # do encrypt
   cypher_msg = pow(block, key.e, key.n)
   return cypher_msg.to_bytes(block_size, "big", signed=False)

def pkcs1pad(message: bytes, block_size: int) -> bytes:
    r"""Pads the message for encryption, returning the padded message.
    :return: 00 02 RANDOM_DATA 00 MESSAGE
    >>> block = _pad_for_encryption(b'hello', 16)
    >>> len(block)
    16
    >>> block[0:2]
    b'\x00\x02'
    >>> block[-6:]
    b'\x00hello'
    """

    max_msglength = block_size - 11
    msglength = len(message)

    if msglength > max_msglength:
        raise OverflowError(
            "%i bytes needed for message, but there is only"
            " space for %i" % (msglength, max_msglength)
        )

    # Get random padding
    padding = b""
    padding_length = block_size - msglength - 3

    # We remove 0-bytes, so we'll end up with less padding than we've asked for,
    # so keep adding data until we're at the correct length.
    while len(padding) < padding_length:
        needed_bytes = padding_length - len(padding)
        # Always read at least 8 bytes more than we need, and trim off the rest
        # after removing the 0-bytes. This increases the chance of getting
        # enough bytes, especially when needed_bytes is small
        new_padding = os.urandom(needed_bytes + 5)
        new_padding = new_padding.replace(b"\x00", b"")
        padding = padding + new_padding[:needed_bytes]

    assert len(padding) == padding_length

    return b"".join([b"\x00\x02", padding, b"\x00", message])