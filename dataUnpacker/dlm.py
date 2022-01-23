#!/usr/bin/python3
# -*- coding: utf-8 -*-
import zlib, tempfile, io
from pyd2bot.gameData.world.map import Map
from pyd2bot.utils.binaryIO.binarystream import BinaryStream


class InvalidDLMFile(Exception):
    pass

class DLM:
    
    def __init__(self, key=None):
        if key == None:
            raise InvalidDLMFile("Map decryption key is empty.")
        self._key = key

    def read(self, raw:bytes):
        dlm_uncompressed = tempfile.TemporaryFile()
        dlm_uncompressed.write(zlib.decompress(raw))
        dlm_uncompressed.seek(0)
        dlm_raw = BinaryStream(dlm_uncompressed, True)
        
        header = dlm_raw.read_char()
        map_version = dlm_raw.read_char()
        mapId = dlm_raw.read_uint32()
        
        if map_version > 6:
            self.encrypted = dlm_raw.read_bool()
            self.encryptionVersion = dlm_raw.read_char()
            self.dataLen = dlm_raw.read_int32()

            if self.encrypted:
                self.encryptedData = dlm_raw.read_bytes(self.dataLen)
                decryptedData = bytearray()
                for i in range(self.dataLen):
                    decryptedData.append(self.encryptedData[i] ^ ord(self._key[i % len(self._key)]))
                cleanData = io.BytesIO(decryptedData)
                mapRaw = BinaryStream(cleanData, True)

        map = Map(mapRaw, mapId, map_version)
        dlm_uncompressed.close()
        del dlm_raw
        return map


