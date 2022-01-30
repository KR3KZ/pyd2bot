from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntFlag(NetworkMessage):
    protocolId = 4191
    mapId:float
    state:int
    
