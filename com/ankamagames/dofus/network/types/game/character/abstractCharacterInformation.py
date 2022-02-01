from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AbstractCharacterInformation(INetworkMessage):
    protocolId = 2714
    id:int
    
    
