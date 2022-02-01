from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockInformationsForSell(NetworkMessage):
    guildOwner:str
    worldX:int
    worldY:int
    subAreaId:int
    nbMount:int
    nbObject:int
    price:int
    
    
