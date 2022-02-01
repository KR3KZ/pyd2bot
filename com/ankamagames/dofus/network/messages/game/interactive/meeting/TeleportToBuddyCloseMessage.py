from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportToBuddyCloseMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    
    
