from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class InteractiveUseEndedMessage(INetworkMessage):
    protocolId = 4234
    elemId:int
    skillId:int
    
    
