import base64
from zlib import decompress
import struct


class ByteArray(bytearray):
    def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs)
        self.position = 0

    @property
    def length(self):
        return len(self)
    
    def to_string(self):
        return base64.b64encode(self).decode("utf")

    def remaining(self):
        return len(self) - self.position

    def hex(self):
        return self.hex()

    @classmethod
    def fromhex(cls, hex):
        return cls(bytearray.fromhex(hex))

    def verif(self, l):
        if len(self) < self.position + l:
            raise IndexError(self.position, l, len(self))

    def read(self, l):
        self.verif(l)
        pos = self.position
        self.position += l
        return self[pos : pos + l]

    def write(self, l):
        self += l

    def uncompress(self):
        self = bytearray(decompress(self))

    def readBoolean(self):
        ans = self.read(1)
        assert ans[0] in [0, 1]
        return bool(ans[0])

    def writeBoolean(self, b):
        if b:
            self += b"\x01"
        else:
            self += b"\x00"

    def readByte(self):
        return int.from_bytes(self.read(1), "big", signed=True)

    def writeByte(self, b, signed=True):
        self += b.to_bytes(1, "big", signed=signed)

    def readByteArray(self):
        lon = self.readVarInt()
        return self.read(lon)

    def writeBytes(self, ba):
        self.writeVarInt(len(ba))
        self += ba

    def readDouble(self):
        return struct.unpack("!d", self.read(8))[0]

    def writeDouble(self, d):
        self += struct.pack("!d", d)

    def readFloat(self):
        return struct.unpack("!f", self.read(4))[0]

    def writeFloat(self, f):
        self += struct.pack("!f", f)

    def readInt(self):
        return int.from_bytes(self.read(4), "big", signed=True)

    def writeInt(self, i):
        self += i.to_bytes(4, "big", signed=True)

    def readShort(self):
        return int.from_bytes(self.read(2), "big", signed=True)

    def writeShort(self, s):
        self += s.to_bytes(2, "big", signed=True)

    def readUTF(self):
        lon = self.readUnsignedShort()
        return self.read(lon).decode()

    def writeUTF(self, ch):
        dat = ch.encode()
        self.writeUnsignedShort(len(dat))
        self += dat

    def readUnsignedByte(self):
        return int.from_bytes(self.read(1), "big")

    def writeUnsignedByte(self, b):
        self += b.to_bytes(1, "big")

    def readUnsignedInt(self):
        return int.from_bytes(self.read(4), "big")

    def writeUnsignedInt(self, ui):
        self += ui.to_bytes(4, "big")

    def readUnsignedShort(self):
        return int.from_bytes(self.read(2), "big")

    def writeUnsignedShort(self, us):
        self += us.to_bytes(2, "big")

    def readBytes(self, offset=0, len=None):
        self.position += offset
        return self.read(len)
    
    def readUTFBytes(self, len):
        return self.read(len).decode()
    
    def _writeVar(self, i):
        if not i:
            self.writeUnsignedByte(0)
        while i:
            b = i & 0b01111111
            i >>= 7
            if i:
                b |= 0b10000000
            self.writeUnsignedByte(b)

    def readVarInt(self):
        ans = 0
        for i in range(0, 32, 7):
            b = self.readUnsignedByte()
            ans += (b & 0b01111111) << i
            if not b & 0b10000000:
                return ans
        raise Exception("Too much data")

    def writeVarInt(self, i):
        assert i.bit_length() <= 32
        self._writeVar(i)

    def readVarUhInt(self):
        return self.readVarInt()

    def writeVarUhInt(self, i):
        self.writeVarInt(i)

    def readVarLong(self):
        ans = 0
        for i in range(0, 64, 7):
            b = self.readUnsignedByte()
            ans += (b & 0b01111111) << i
            if not b & 0b10000000:
                return ans
        raise Exception("Too much data")

    def writeVarLong(self, i):
        assert i.bit_length() <= 64
        self._writeVar(i)

    def readVarUhLong(self):
        return self.readVarLong()

    def writeVarUhLong(self, i):
        self.writeVarLong(i)

    def readVarShort(self):
        ans = 0
        for i in range(0, 16, 7):
            b = self.readByte()
            ans += (b & 0b01111111) << i
            if not b & 0b10000000:
                return ans
        raise Exception("Too much data")

    def writeVarShort(self, i):
        assert i.bit_length() <= 16
        self._writeVar(i)

    def readVarUhShort(self):
        return self.readVarShort()

    def writeVarUhShort(self, i):
        self.writeVarShort(i)
    
    def to_int8Arr(ba:bytearray) -> list[int]:
        ret = []
        for i in range(len(ba)):
            ret.append(int.from_bytes(ba[i:i+1], "big", signed=True))
        return ret

    @staticmethod
    def from_int8Arr(int_arr:list[int]) -> bytearray:
        res = ByteArray()
        for nbr in int_arr:
            res += nbr.to_bytes(1, "big", signed=True)
        return res
    
    def writeBytes(self, data, offset=0, size=None):
        self.position += offset
        if size is None:
            size = len(data)
        if len(data) <= size:
            self += data
        else:
            self += data[:size]
        self.position += len(data)
        
        
class Buffer(ByteArray):
    def end(self):
        del self[:self.position]
        self.position = 0

    def reset(self):
        self.__init__()
