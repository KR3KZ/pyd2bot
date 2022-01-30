from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TreasureHuntFlag(INetworkMessage):
    protocolId = 4191
    mapId:int
    state:int
    
    
