from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterLevelUpMessage(INetworkMessage):
    protocolId = 6501
    newLevel:int
    
    
