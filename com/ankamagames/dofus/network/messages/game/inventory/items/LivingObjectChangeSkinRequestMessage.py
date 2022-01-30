from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LivingObjectChangeSkinRequestMessage(NetworkMessage):
    protocolId = 7679
    livingUID:int
    livingPosition:int
    skinId:int
    
