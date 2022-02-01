from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildHouseRemoveMessage(NetworkMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    
    
