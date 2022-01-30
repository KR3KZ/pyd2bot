from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterCreationResultMessage(INetworkMessage):
    protocolId = 110
    result:int
    
    
