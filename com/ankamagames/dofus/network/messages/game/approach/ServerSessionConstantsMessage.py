from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant


class ServerSessionConstantsMessage(NetworkMessage):
    protocolId = 646
    variables:ServerSessionConstant
    
