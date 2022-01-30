from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AbstractCharacterInformation(INetworkMessage):
    protocolId = 2714
    id:int
    
    
