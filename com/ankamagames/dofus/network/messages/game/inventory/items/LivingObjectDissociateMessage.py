from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LivingObjectDissociateMessage(NetworkMessage):
    protocolId = 9254
    livingUID:int
    livingPosition:int
    
    
