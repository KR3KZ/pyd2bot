from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class InteractiveUseEndedMessage(INetworkMessage):
    protocolId = 4234
    elemId:int
    skillId:int
    
    
