import logging
from .binrw import Data, Buffer
from ..protocol import DofusProtocol
from pathlib import Path

logger = logging.getLogger("labot")

protocol_json_f = Path(__file__).parent / "../protocol.json"
dofusProtocol = DofusProtocol(protocol_json_f)
class Msg:
    def __init__(self, m_id, data, count=None):
        self.id = m_id
        if isinstance(data, bytearray):
            data = Data(data)
        self.data = data
        self.count = count

    def __str__(self):
        ans = str.format(
            "{}(m_id={}, data={}, count={})",
            self.__class__.__name__,
            self.id,
            self.data.data,
            self.count,
        )
        return ans

    def __repr__(self):
        ans = str.format(
            "{}(m_id={}, data={!r}, count={})",
            self.__class__.__name__,
            self.id,
            self.data.data,
            self.count,
        )
        return ans

    @staticmethod
    def fromRaw(buf: Buffer, from_client):
        """Read a message from the buffer and
        empty the beginning of the buffer.
        msg fields spec: 
            id     |   len    |   data
           2 bits  |  2 bits  |  len bits
        """
        if not buf:
            return
        try:
            header = buf.readUnsignedShort()
            if from_client:
                count = buf.readUnsignedInt()
            else:
                count = None
            lenData = int.from_bytes(buf.read(header & 3), "big")
            id = header >> 2
            data = Data(buf.read(lenData))
        except IndexError:
            buf.pos = 0
            raise Exception("Unable to parse the msg because of missing data")

        if id == 2:
            logger.debug("Message is NetworkDataContainerMessage! Uncompressing...")
            newbuffer = Buffer(data.readByteArray())
            newbuffer.uncompress()
            msg = Msg.fromRaw(newbuffer, from_client)
            if msg is None or newbuffer.remaining():
                raise Exception("Unable to parse Message")
            return msg
        
        buf.end()

        return Msg(id, data, count)

    def lenlenData(self):
        if len(self.data) > 65535:
            return 3
        if len(self.data) > 255:
            return 2
        if len(self.data) > 0:
            return 1
        return 0

    def bytes(self):
        header = 4 * self.id + self.lenlenData()
        ans = Data()
        ans.writeUnsignedShort(header)
        if self.count is not None:
            ans.writeUnsignedInt(self.count)
        ans += len(self.data).to_bytes(self.lenlenData(), "big")
        ans += self.data
        return ans.data

    @property
    def msgType(self):
        return dofusProtocol.getMsgById(self.id)

    def json(self):
        logger.debug("Getting json representation of message %s", self)
        if not hasattr(self, "parsed"):
            self.parsed = dofusProtocol.read(self.msgType["name"], self.data)
        return self.parsed

    @staticmethod
    def from_json(json, count=None, random_hash=True):
        type_name: str = json["__type__"]
        msg_type: dict = dofusProtocol.getMsgTypeByName(type_name)
        type_id: int = msg_type["protocolId"]
        data = dofusProtocol.write(type_name, json, random_hash=random_hash)
        return Msg(type_id, data, count)
