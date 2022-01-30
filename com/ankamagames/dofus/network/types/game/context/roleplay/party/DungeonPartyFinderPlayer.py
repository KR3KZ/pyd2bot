from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderPlayer(NetworkMessage):
    protocolId = 5806
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    
    
