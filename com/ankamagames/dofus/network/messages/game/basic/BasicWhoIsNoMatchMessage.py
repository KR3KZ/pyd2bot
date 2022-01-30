from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class BasicWhoIsNoMatchMessage(NetworkMessage):
    protocolId = 7631
    target:AbstractPlayerSearchInformation
    
