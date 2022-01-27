#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import OrderedDict
from pyd2bot.utils.binaryIO import BinaryStream
from io import BytesIO
# Exceptions


class InvalidD2OFile(Exception):
    def __init__(self, message):
        super(InvalidD2OFile, self).__init__(message)
        self.message = message



class D2OReader:
    """Read D2O files"""
    def __init__(self, stream:BytesIO):
        """Init the class with the informations about files in the D2P"""

        # Attributes
        self._stream = stream
        self._stream_start_index = 7
        self._classes = dict[str, GameDataClassDefinition]()
        self._counter = 0

        # Load the D2O
        raw = BinaryStream(self._stream, True)
        self._raw = raw

        string_header = raw.readBytes(3)
        base_offset = 0

        if string_header != b'D2O':
            self._stream.seek(0)
            string_header = raw.readUTF()
            if string_header != "AKSF":
                raise InvalidD2OFile("Malformated game data file.")
            raw.readShort()
            base_offset = raw.readInt()
            self._stream.seek(base_offset, 1)
            self._stream_start_index = self._stream.position + 7
            string_header = raw.readBytes(3)
            if string_header != b'D2O':
                raise InvalidD2OFile("Malformated game data file.")

        offset = raw.readInt()
        self._stream.seek(base_offset + offset)
        index_number = raw.readInt()
        index = 0
        index_dict = OrderedDict()

        while index < index_number:
            index_id = raw.readInt()
            offset = raw.readInt()
            index_dict[index_id] = base_offset + offset
            self._counter += 1
            index = index + 8

        class_number = raw.readInt()
        class_index = 0

        while class_index < class_number:
            class_id = raw.readInt()
            self.readClassDefinition(class_id, raw)
            class_index += 1

        if raw.remaining():
            self._game_data_processor = GameDataProcess(raw)

    def getObjects(self):
        if not self._counter:
            return None
        counter = self._counter
        classes = self._classes
        raw = self._raw
        raw.position(self._stream_start_index)
        objects = list()
        i = 0
        while i < counter:
            objects.append(classes[raw.readInt()].read(raw))
            i += 1
        return objects

    def getClassDefinition(self, object_id):
        return self._classes[object_id]

    def readClassDefinition(self, class_id, raw:BinaryStream):
        class_name = raw.readUTF()
        class_pkg = raw.readUTF()
        class_def = GameDataClassDefinition(class_pkg, class_name, self)
        field_number = raw.readInt()
        field_index = 0

        while field_index < field_number:
            field = raw.readUTF()
            class_def.addField(field, raw)
            field_index += 1

        self._classes[class_id] = class_def


class GameDataClassDefinition:
    def __init__(self, class_pkg:bytes, class_name:bytes, d2o_reader:D2OReader):
        names = class_name.decode('utf-8').split('.')
        self._name = names[-1]
        self._pckg = class_pkg.decode('utf-8') + ".".join(names[:-1])
        self._fields = list[GameDataField]()
        self._d2o_reader = d2o_reader

    def fields(self):
        return self._fields

    def read(self, raw):
        as_dict = dict[str, GameDataField]({field.name: field.readData(raw) for field in self._fields})
        return type(self._name, (object,), as_dict)

    def addField(self, name, raw):
        field = GameDataField(name, self._d2o_reader)
        field.readType(raw)
        self._fields.append(field)


class GameDataField:
    def __init__(self, name:bytes, d2o_reader:D2OReader):
        self.name = name.decode('utf-8')
        self._inner_read_methods = list()
        self._inner_type_names = list()
        self._d2o_reader = d2o_reader

    def readType(self, raw:BinaryStream):
        read_id = raw.readInt()
        self.readData = self.getReadMethod(read_id, raw)

    def getReadMethod(self, read_id, raw:BinaryStream):
        if read_id == -1:
            return self._read_integer
        elif read_id == -2:
            return self._read_boolean
        elif read_id == -3:
            return self._read_string
        elif read_id == -4:
            return self._read_number
        elif read_id == -5:
            return self._read_i18n
        elif read_id == -6:
            return self._read_unsigned_integer
        elif read_id == -99:
            self._inner_type_names.append(raw.readUTF())
            self._inner_read_methods = [self.getReadMethod(raw.readInt(), raw)] + self._inner_read_methods
            return self._read_vector
        else:
            if read_id > 0:
                return self._read_object
            raise Exception("Unknown type \'" + read_id + "\'.")

    def _read_integer(self, raw:BinaryStream, vec_index=0):
        return raw.readInt()

    def _read_boolean(self, raw:BinaryStream, vec_index=0):
        return raw.readbool()

    def _read_string(self, raw:BinaryStream, vec_index=0):
        string:bytes = raw.readUTF()
        if string == 'null':
            string = None
        return string.decode('utf-8')

    def _read_number(self, raw:BinaryStream, vec_index=0):
        return raw.readDouble()

    def _read_i18n(self, raw:BinaryStream, vec_index=0):
        return raw.readInt()

    def _read_unsigned_integer(self, raw:BinaryStream, vec_index=0):
        return raw.readInt()

    def _read_vector(self, raw:BinaryStream, vec_index=0):
        vector_size = raw.readInt()
        vector = list()
        i = 0
        while i < vector_size:
            vector.append(self._inner_read_methods[vec_index](raw, vec_index + 1))
            i += 1
        return vector

    def _read_object(self, raw:BinaryStream, vec_index=0):
        object_id = raw.readInt()
        if object_id == -1431655766:
            return None
        obj = self._d2o_reader.getClassDefinition(object_id)
        return obj.read(raw)


class GameDataProcess:
    def __init__(self, raw:BinaryStream):
        self._stream = raw
        self._sort_index = OrderedDict()
        self._queryable_field = list()
        self._search_field_index = OrderedDict()
        self._search_field_type = OrderedDict()
        self._search_field_count = OrderedDict()
        self.parseStream()

    def parseStream(self):
        length = self._stream.readInt()
        off = self._stream.position() + length + 4
        while length:
            available = self._stream.remaining()
            string = self._stream.readUTF()
            self._queryable_field.append(string)
            self._search_field_index[string] = self._stream.readInt() + off
            self._search_field_type[string] = self._stream.readInt()
            self._search_field_count[string] = self._stream.readInt()
            length = length - (available - self._stream.remaining())