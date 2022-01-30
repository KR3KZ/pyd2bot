from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DungeonPartyFinderPlayer(INetworkMessage):
    protocolId = 5806
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    
    
