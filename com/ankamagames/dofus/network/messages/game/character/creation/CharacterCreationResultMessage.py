from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterCreationResultMessage(INetworkMessage):
    protocolId = 110
    result:int
    
    
