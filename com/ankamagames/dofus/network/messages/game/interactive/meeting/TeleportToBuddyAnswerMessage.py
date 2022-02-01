from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportToBuddyAnswerMessage(NetworkMessage):
    dungeonId:int
    buddyId:int
    accept:bool
    
    
