from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP
import random
import math
import hashlib


def cipherMd5str(self, pwd:str) -> str:
   return  hashlib.md5(pwd + self._salt)
    
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
   
def pkcs1_unpad(m, mod_len, type=2):
   '''removes padding returns none if padding is invalid'''
   if len(m) != mod_len: return
   print(m[0], m[1])
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
   chunk = pow(block, key.e, key.n)
   b:bytearray = chunk.to_bytes(block_size, "big", signed=False)
   dst = pkcs1_unpad(b, block_size, 1)
   if dst is None:
      raise Exception("Decrypt error - padding function returned None!")
   return dst

def getBlockSize(key:RSA.RsaKey):
   return (key.n.bit_length() + 7) // 8
