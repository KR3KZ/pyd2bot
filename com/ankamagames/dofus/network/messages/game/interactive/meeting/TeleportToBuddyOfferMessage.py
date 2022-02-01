from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportToBuddyOfferMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    timeLeft:int
    
    
