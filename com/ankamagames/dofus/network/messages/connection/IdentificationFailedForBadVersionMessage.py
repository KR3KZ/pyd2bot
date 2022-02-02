from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import IdentificationFailedMessage
from com.ankamagames.dofus.network.types.version.Version import Version


@dataclass
class IdentificationFailedForBadVersionMessage(IdentificationFailedMessage):
    requiredVersion:Version
    
    
    def __post_init__(self):
        super().__init__()
    