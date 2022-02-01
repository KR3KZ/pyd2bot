from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterReplayRequestMessage(INetworkMessage):
    protocolId = 9614
    characterId:int
    
    
