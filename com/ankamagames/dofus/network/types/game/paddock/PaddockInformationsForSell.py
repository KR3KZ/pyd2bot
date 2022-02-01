from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PaddockInformationsForSell(INetworkMessage):
    protocolId = 1249
    guildOwner:str
    worldX:int
    worldY:int
    subAreaId:int
    nbMount:int
    nbObject:int
    price:int
    
    
