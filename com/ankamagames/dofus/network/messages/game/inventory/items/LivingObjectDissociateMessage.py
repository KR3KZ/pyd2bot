from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LivingObjectDissociateMessage(INetworkMessage):
    protocolId = 9254
    livingUID:int
    livingPosition:int
    
    
