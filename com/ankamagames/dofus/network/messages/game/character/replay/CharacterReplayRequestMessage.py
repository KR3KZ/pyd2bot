from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterReplayRequestMessage(INetworkMessage):
    protocolId = 9614
    characterId:int
    
    
