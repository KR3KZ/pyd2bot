import logging
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.ankamagames.jerakine.network.parser.ProtocolSpec import ProtocolSpec
from com.ankamagames.jerakine.network.parser.TypeEnum import TypeEnum
import com.ankamagames.jerakine.network.parser.NetworkMessageClassDefinition as nmcd

logger = Logger("bot")


class NetMsgDataField:

    TRACE = False

    dataReader = {
        TypeEnum.INT: "readInt",
        TypeEnum.UNSIGNEDINT: "readUnsignedInt",
        TypeEnum.SHORT: "readShort",
        TypeEnum.UNSIGNEDSHORT: "readUnsignedShort",
        TypeEnum.BYTE: "readByte",
        TypeEnum.UNSIGNEDBYTE: "readUnsignedByte",
        TypeEnum.FLOAT: "readFloat",
        TypeEnum.DOUBLE: "readDouble",
        TypeEnum.BOOLEAN: "readBoolean",
        TypeEnum.VARINT: "readVarInt",
        TypeEnum.VARLONG: "readVarLong",
        TypeEnum.UTF: "readUTF",
        TypeEnum.VARUHSHORT: "readVarUhShort",
        TypeEnum.VARUHINT: "readVarUhInt",
        TypeEnum.VARSHORT: "readVarShort",
        TypeEnum.VARUHLONG: "readVarUhLong",
    }

    def __init__(self, spec: dict, raw: ByteArray):
        self._spec = spec
        self._raw = raw

    @property
    def isDynamicObj(self):
        return self._spec.get("dynamicType")

    @property
    def isPrimitive(self):
        return TypeEnum(self._spec["typeId"]) != TypeEnum.OBJECT

    def getFieldTypeLength(self):
        if self.TRACE:
            logger.debug("getting field type length")
        l = self._spec.get("length")
        if l is None:
            if self.TRACE:
                logger.debug("field has no length")
            lTypeId = self._spec.get("lengthTypeId")
            if lTypeId is not None:
                if self.TRACE:
                    logger.debug("field has length type id " + str(lTypeId))
                return self.readPrimitive(TypeEnum(lTypeId))
        return l

    def deserialize(self):
        self.length = self.getFieldTypeLength()
        if self.length is not None:
            return self.readVector()
        if self.TRACE:
            logger.debug("self is primitive ? ", self.isPrimitive)
        if self.isPrimitive:
            if self.TRACE:
                logger.debug(
                    "self is primitive of type " + str(TypeEnum(self._spec["typeId"]))
                )
            return self.readPrimitive()
        else:
            return self.readObject()

    def readPrimitive(self, typeId=None):
        if typeId is None:
            typeId = TypeEnum(self._spec["typeId"])
        dataReader = NetMsgDataField.dataReader.get(typeId)
        if dataReader is None:
            raise Exception(f"Type id {typeId} not found in known types ids")
        ret = getattr(self._raw, dataReader)()
        if self.TRACE:
            logger.debug(f"read primitive {typeId} found {ret}")
        return ret

    def readObject(self):
        className = self._spec["type"]
        if self.TRACE:
            logger.debug("Is dynamic object ? ", self.isDynamicObj)
        if self.isDynamicObj:
            if self.TRACE:
                logger.debug("Retrieving dynamic type Spec")
            typeId = self._raw.readUnsignedShort()
            classSpec = ProtocolSpec.getTypeSpecById(typeId)
            if self.TRACE:
                logger.debug("Dynamic type has name " + classSpec["name"])
            className = classSpec["name"]
        obj = nmcd.NetworkMessageClassDefinition(className, self._raw).deserialize()
        return obj

    def readVector(self):
        if self.TRACE:
            logger.debug("reading vector of length " + str(self.length))
        ret = []
        for _ in range(self.length):
            if self.TRACE:
                logger.debug("self is primitive ? ", self.isPrimitive)
            if self.isPrimitive:
                ret.append(self.readPrimitive())
            else:
                ret.append(self.readObject())
        return ret
