from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterLevelUpMessage(INetworkMessage):
    protocolId = 6501
    newLevel:int
    
    
