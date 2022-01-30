from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaddockInformationsForSell(NetworkMessage):
    protocolId = 1249
    guildOwner:str
    worldX:int
    worldY:int
    subAreaId:int
    nbMount:int
    nbObject:int
    price:int
    
    
