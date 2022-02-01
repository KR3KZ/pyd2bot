from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TeleportToBuddyAnswerMessage(INetworkMessage):
    protocolId = 5687
    dungeonId:int
    buddyId:int
    accept:bool
    
    
