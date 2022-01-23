#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io
from struct import *

class BinaryStream:
    """Allow some binary operations on a stream opened in binary mode"""
    def __init__(self, base_stream:io.BytesIO, big_endian=False):
        self._base_stream = base_stream
        self._big_endian = big_endian

    def position(self, value=None):
        if value is None:
            return self._base_stream.tell()
        else:
            self._base_stream.seek(value)

    def bytes_available(self):
        position = self._base_stream.tell()
        self._base_stream.seek(0, 2)
        eof = self._base_stream.tell()
        self._base_stream.seek(position, 0)
        return eof - position

    # Read functions

    def read_byte(self):
        return self._base_stream.read(1)

    def read_bytes(self, length=None):
        if length is None:
            bytes = self._base_stream.read()
        else:
            bytes = self._base_stream.read(length)
        return bytes

    def read_bool(self):
        bool = self._base_stream.read(1)[0]
        if bool == 1:
            return True
        else:
            return False

    def read_char(self):
        return self._unpack('b')

    def read_uchar(self):
        return self._unpack('B')

    def read_bool(self):
        return self._unpack('?')

    def read_int16(self):
        return self._unpack('h', 2)

    def read_uint16(self):
        return self._unpack('H', 2)

    def read_int32(self):
        return self._unpack('i', 4)

    def read_uint32(self):
        return self._unpack('I', 4)

    def read_int64(self):
        return self._unpack('q', 8)

    def read_uint64(self):
        return self._unpack('Q', 8)

    def read_float(self):
        return self._unpack('f', 4)

    def read_double(self):
        return self._unpack('d', 8)

    def read_string(self):
        length = self.read_uint16()
        return self._unpack(str(length) + 's', length)

    def read_string_bytes(self, length):
        return self._unpack(str(length) + 's', length)

    def _unpack(self, fmt, length=1):
        bytes = self.read_bytes(length)
        if self._big_endian:
            fmt = ">" + fmt
        else:
            fmt = "<" + fmt
        return unpack(fmt, bytes)[0]
