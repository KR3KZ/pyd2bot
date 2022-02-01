from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportBuddiesRequestedMessage(NetworkMessage):
    dungeonId:int
    inviterId:int
    invalidBuddiesIds:list[int]
    
    
