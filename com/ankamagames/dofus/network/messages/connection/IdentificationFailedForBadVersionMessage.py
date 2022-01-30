from com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import IdentificationFailedMessage
from com.ankamagames.dofus.network.types.version.Version import Version


class IdentificationFailedForBadVersionMessage(IdentificationFailedMessage):
    protocolId = 7294
    requiredVersion:Version
    
    
